#!/usr/bin/env python3

import os, shutil, glob, sys, math
from molecule_db import *

def run_rdf(compound, xray: bool):
    rdfout = "rdf.xvg"
    if os.path.exists(rdfout):
        return
    job    = "rdf.sh"
    with open(job, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        if xray:
            input = ( "../../../../box/solid/%s.pdb" % compound )
            outf.write("gmx rdf -bin 0.01 -sel 0 -ref 0 -f %s -s %s -o %s\n" % ( input, input, rdfout))
        else:
            tbegin = 14500
            tend   = 15000
            outf.write("gmx rdf -sel 0 -ref 0 -dt 1 -f NPT.xtc -s NPT.tpr -o %s -b %d -e %d \n" % ( rdfout, tbegin, tend ))
    os.system("sbatch %s" % job)

def do_rdf(moldb, xray:bool):
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            if xray:
                os.makedirs("xray", exist_ok=True)
                os.chdir("xray")
                run_rdf(compound, True)
                os.chdir("..")
            else:
                for temp in glob.glob("*"):
                    if os.path.isdir(temp):
                        os.chdir(temp)
                        final_gro = "NPT2.gro"                
                        if os.path.exists(final_gro):
                            run_rdf(compound, False)
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
            do_rdf(moldb, xray)
            os.chdir("..")
        os.chdir("..")
