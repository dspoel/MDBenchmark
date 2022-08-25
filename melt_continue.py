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
        if csb:
            ncore = 16
            gromacs = ("gmx mdrun -ntomp 2 -ntmpi %d -dd 2 2 2" % 8)
        else:
            ncore = 27
            gromacs = "mpirun -n 27 gmx_mpi mdrun  -ntomp 1 -dd 3 3 3"
            outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n %d\n" % ncore)
        outf.write("%s -cpi %s.cpt -deffnm %s -nsteps %d \n" % ( gromacs, target, target, nsteps ) )
    os.system("sbatch %s" % job)

def copy_ifnot_exists(src:str, dst:str) -> bool:
    if not os.path.exists(src):
        return False
    if not os.path.exists(dst):
        shutil.copy(src, dst)
    return True
    
def run_melt(mol:str, temp:float, prev:dict, nsteps:int):
    if not ((prev["host"].find("csb") >= 0 and csb) or (prev["host"].find("csb") < 0 and not csb)):
        print("Cannot continue this simulation on this host since it was run on %s earlier" % prev["host"])
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
    foundAll = True
    for fn in [ "cptfile", "edrfile", "trrfile", "tprfile", "tprfile", "logfile" ]:
        foundAll = foundAll and copy_ifnot_exists(basedir+prev[fn], prev[fn])
    if foundAll:
        write_run_job(target, nsteps)
    else:
        print("Could not find all files needed to continue simulation for %s @ %g" % ( mol, temp ))
    os.chdir("../../..")
    
def parseArguments():
    parser = argparse.ArgumentParser(
      prog='simtable.py',
      description=
"""
Script to continue melting simulations.
""")
    mtname = "melt_table.csv" 
    parser.add_argument("-mol", "--molecule", help="The molecule to run", type=str, default=None)
    parser.add_argument("-temp", "--temperature", nargs='+', help="Temperature(s) to simulate at", type=float, default=0)
    nsteps = 10000000
    parser.add_argument("-nsteps", "--nsteps", help="Number of steps to extend simulation with, default "+str(nsteps), type=int, default=nsteps)
    parser.add_argument("-v", "--verbose", help="Print debugging info", action="store_true")
    return parser.parse_args()
    
if __name__ == '__main__':
    if shutil.which("gmx") == None:
        sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")
    args  = parseArguments()
    if args.verbose:
        Debug = True

    simtabs = glob.glob("*_simtable.csv")
    simtable = get_simtable(simtabs)

    if None == args.molecule:
        print("Please provide a molecule name (use -h flag to get info)")
    elif args.nsteps <= 0:
        print("Specify a positive number of steps")
    elif args.molecule not in simtable:
        print("Molecule %s unknown. Pick one of:\n" % args.molecule)
        print(simtable.keys())
    else:
        for temp in args.temperature:
            if temp not in simtable[args.molecule]:
                print("No previous simulation at temperature %g. Try one of these:\n" % temp)
                print(sorted(simtable[args.molecule].keys()))
            else:
                run_melt(args.molecule, temp, simtable[args.molecule][temp], args.nsteps)
