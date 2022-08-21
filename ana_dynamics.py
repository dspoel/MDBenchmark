#!/usr/bin/env python3
        
import os, shutil, glob, sys, math
from molecule_db import *
from simtable    import *

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0
Debug = True

def use_sim(simtable:dict, mol:str, temp: int) -> bool:
    if not mol in simtable or not temp in simtable[mol]:
        print("Cannot find mol %s, temp %g in simtable. Sorry." % ( mol, temp ))
        return False
    if csb and simtable[mol][temp]["host"].find("csb") >= 0:
        return True
    if not csb and simtable[mol][temp]["host"].find("keb") >= 0:
        return True
    if Debug:
        boolname = { False: "False", True: "True" }
        print("csb: %s host: %s" % ( boolname[csb], simtable[mol][temp]["host"]))
    return False
        
def run_rotacf(jobname: str, compound:str, tbegin: float, tend: float, traj: str, tpr: str,
               indexdir: str, rotacfout: str, rotplane: str, msdout: str, force:bool):
    # If files exist, do nothing, except when trajectory is newer.
    planendx = ( "%s/%s_rotplane.ndx" % ( indexdir, compound ))
    if os.path.exists(rotacfout) and os.path.exists(msdout) and (os.path.exists(rotplane) or not os.path.exists(planendx)):
        if not (force or os.path.getmtime(traj) > os.path.getmtime(rotacfout)):
            return
    with open(jobname, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
        if not csb:
            outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        outf.write("gmx rotacf -d -n %s/%s_rotaxis.ndx -f %s -s %s -o %s -b %d -e %d \n" % ( indexdir, compound, traj, tpr, rotacfout, tbegin, tend ))
        if os.path.exists(planendx):
            outf.write("gmx rotacf -n %s -f %s -s %s -o %s -b %d -e %d \n" % ( planendx, traj, tpr, rotplane, tbegin, tend ))
        outf.write("echo 0 | gmx msd -f %s -s %s -o %s -b %d -e %d \n" % ( traj, tpr, msdout, tbegin, tend ))
    os.system("sbatch %s" % jobname)

def ana_dynamics(simtable_file:str):
    simtable = get_simtable(simtable_file)
    print(simtable.keys())
    pwd = os.getcwd()
    print("pwd %s" % pwd)
    os.chdir("bcc/melt")
    for molname in simtable.keys():
        os.makedirs(molname, exist_ok=True)
        os.chdir(molname)
        for temp in simtable[molname]:
            if use_sim(simtable, molname, temp):
                if Debug:
                    print("%s %f" % ( molname, temp ))
                jobname = ("%s_%g.sh" % ( molname, temp ))
                simdir  = simtable[molname][temp]["simdir"] + "/"
                traj    = simdir + simtable[molname][temp]["trrfile"]
                tpr     = simdir + simtable[molname][temp]["tprfile"]
                rotacfout = ("rotacf_%g.xvg" % temp )
                rotplane  = ("rotplane_%g.xvg" % temp )
                msdout    = ("msd_%g.xvg" % temp )
                indexdir  = "../../../index"
                length    = simtable[molname][temp]["length"]*1000
                run_rotacf(jobname, molname, length-200, length, traj, tpr,
                           indexdir, rotacfout, rotplane, msdout, False)
                if len(simtable[molname][temp]["grofile"]) > 4:
                    finalgro  = simdir + simtable[molname][temp]["grofile"] 
                    dstf      = ("final_%g.gro" % temp )
                    print("Will try to copy %s to %s if needed" % ( finalgro, dstf ) )
                    if os.path.exists(finalgro) and (not os.path.exists(dstf) or os.path.getmtime(finalgro) > os.path.getmtime(dstf)):
                        shutil.copyfile(finalgro, dstf)
        os.chdir("..")
    os.chdir(pwd)

def do_rotacf(moldb):
    tbegin    = 14000
    tend      = 15000
    traj      = "NPT.xtc"
    tpr       = "NPT.tpr"
    rotacfout = "rotacf.xvg"
    rotplane  = "rotplane.xvg"
    msdout    = "msd.xvg"
    jobname   = "rotacf.sh"
    indexdir  = "../../../../index"
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            for temp in glob.glob("*"):
                if os.path.isdir(temp):
                    os.chdir(temp)
                    final_gro = "NPT2.gro"                
                    if os.path.exists(final_gro):
                        run_rotacf(jobname, compound, tbegin, tend, traj, tpr,
                                   indexdir, rotacfout, rotplane, msdout)
                    os.chdir("..")
            os.chdir("..")

if __name__ == '__main__':

    if shutil.which("gmx") == None:
        sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")

    moldb  = get_moldb(False)

    if False:
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
    else:
        ana_dynamics("simtable.csv")

