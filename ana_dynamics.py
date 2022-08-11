#!/usr/bin/env python3
        
import os, shutil, glob, sys, math
from molecule_db import *

def run_rotacf(compound):
    rotacfout = "rotacf.xvg"
    rotplane  = "rotplane.xvg"
    msdout    = "msd.xvg"
    if os.path.exists(rotacfout) and os.path.exists(msdout) and os.path.exists(rotplane):
        return
    job    = "rotacf.sh"
    with open(job, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        tbegin = 14000
        tend   = 15000
        outf.write("gmx rotacf -d -n ../../../../index/%s_rotaxis.ndx -f NPT.xtc -s NPT.tpr -o %s -b %d -e %d \n" % ( compound, rotacfout, tbegin, tend ))
        planendx = ( "../../../../index/%s_rotplane.ndx" % compound )
        if os.path.exists(planendx):
            outf.write("gmx rotacf -n %s -f NPT.xtc -s NPT.tpr -o %s -b %d -e %d \n" % ( planendx, rotplane, tbegin, tend ))
        outf.write("gmx msd -n ../../../../index/%s_rotaxis.ndx -f NPT.xtc -s NPT.tpr -o %s -b %d -e %d \n" % ( compound, msdout, tbegin, tend ))
    os.system("sbatch %s" % job)

def do_rotacf(moldb):
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            for temp in glob.glob("*"):
                if os.path.isdir(temp):
                    os.chdir(temp)
                    final_gro = "NPT2.gro"                
                    if os.path.exists(final_gro):
                        run_rotacf(compound)
                    os.chdir("..")
            os.chdir("..")

if shutil.which("gmx") == None:
    sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")

moldb  = get_moldb(False)
for top in [ "bcc", "resp" ]:
    print("Looking for %s" % top)
    if os.path.isdir(top):
        os.chdir(top)
        phase = "solid"
        if os.path.isdir(phase):
            os.chdir(phase)
            do_rotacf(moldb)
            os.chdir("..")
        os.chdir("..")
