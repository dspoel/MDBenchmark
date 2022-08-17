#!/usr/bin/env python3
        
import os, shutil, glob, sys, math, argparse
from molecule_db      import *
from simtable         import *
from collect_dynamics import *

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0

def write_run_job(target:str, nsteps:int):
    job = target + ".sh"
    with open(job, "w") as outf:
        outf.write("#!/bin/sh\n")
        outf.write("#SBATCH -t 72:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 12\n")
        outf.write("mpirun gmx_mpi mdrun -ntomp 1 -dd  2 3 2  -cpi %s.cpt -deffnm %s -nsteps %d \n" % ( target, target, nsteps ) )
    os.system("sbatch %s" % job)

def copy_ifnot_exists(src:str, dst:str):
    if not os.path.exists(dst):
        shutil.copy(src, dst)
        
def run_melt(mol:str, temp:float, prev:dict):
    if not ((prev["host"] == "csb" and csb) or (prev["host"] != "csb" and not csb)):
        return
    meltroot = "melting"
    os.makedirs(meltroot, exist_ok=True)
    os.chdir(meltroot)
    os.makedirs(mol, exist_ok=True)
    os.chdir(mol)
    tempdir = ("%g" % temp)
    os.makedirs(tempdir, exist_ok=True)
    os.chdir(tempdir)
    basedir = prev["simdir"] + "/"
    target  = prev["trrfile"][:-4]
    for fn in [ "cptfile", "edrfile", "trrfile", "tprfile", "tprfile", "logfile" ]:
        copy_ifnot_exists(basedir+prev[fn], prev[fn])
    if not os.path.exists(target + ".sh"):
        write_run_job(target, 10000000)
    os.chdir("../../..")
    
if __name__ == '__main__':
    if shutil.which("gmx") == None:
        sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")

    simtable = get_simtable("simtable.csv")
    
    for mol in [ "furan" ]:
        for temp in ignore[mol]:
            run_melt(mol, temp, simtable[mol][temp])

