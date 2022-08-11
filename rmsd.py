#!/usr/bin/env python3

import os, shutil, glob, sys, math
from molecule_db import *

def run_rms(compound, nsolid:int):
    allrmsd = "allrmsd.xvg"
    if os.path.exists(allrmsd):
        return
    tbegin = 14500
    tend   = 15000
    short  = "short.xtc"
    job    = "rms.sh"
    with open(job, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        outf.write("echo 0 | gmx trjconv -f NPT -s NPT -pbc mol -b %d -e %d -o %s\n" % ( tbegin, tend, short ) )
        refpdb = ( "../../../../box/solid/%s.pdb" % compound )
        index  = ( "../../../../index/%s_rmsd.ndx" % compound )
        for mol in range(nsolid):
            rmsout = ( "rms%d.xvg" % mol )
            outf.write("echo %d %d | gmx rms -f %s -s %s -o %s  -fit translation -n %s\n" % ( mol, mol, short, refpdb, rmsout, index ))
            koko = "rms.koko"
            outf.write("gmx analyze -f %s > %s\n" % ( rmsout, koko ))
            outf.write("grep SS1 %s | awk '{ print $2 }' >> %s\n\n" % ( koko, allrmsd ))
            outf.write("rm %s %s" % ( koko, rmsout) )
    os.system("sbatch %s" % job)

def do_rms(moldb):
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            for temp in glob.glob("*"):
                if os.path.isdir(temp):
                    os.chdir(temp)
                    final_gro = "NPT2.gro"                
                    if os.path.exists(final_gro):
                        run_rms(compound, moldb[compound]["nsolid"])
                    os.chdir("..")
            os.chdir("..")

if shutil.which("gmx") == None:
    sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")

moldb  = get_moldb(False)
xray   = False
for top in [ "bcc", "resp" ]:
    print("Looking for %s" % top)
    if os.path.isdir(top):
        os.chdir(top)
        phase = "solid"
        if os.path.isdir(phase):
            os.chdir(phase)
            do_rms(moldb)
            os.chdir("..")
        os.chdir("..")
