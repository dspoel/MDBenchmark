#!/usr/bin/env python3
        
import os, shutil, glob, sys, math
from molecule_db import *
from ana_dynamics import *
from collect_dynamics import *

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0

def get_run_dict(topdir: str, molnames:list, useall:bool):
    if not os.path.exists(topdir):
        sys.exit("No such dir %s" % topdir)
    pwd = os.getcwd()
    os.chdir(topdir)
    lisa_name = { "acooh": "acoh", "12-ethanediamine": "ethylendiamine", "ethyleneglycol": "ethylenglycol", "ethylene": "ethene" }
    mydict = {}
    for molname in molnames:
        mol = molname
        if mol in lisa_name:
            mol = lisa_name[mol]
        if (molname in ignore or useall) and os.path.exists(mol):
            os.chdir(mol)
            mydict[mol] = {}
            for simdir in glob.glob("*%s*" % mol):
                if os.path.isdir(simdir):
                    os.chdir(simdir)
                    newest_trr  = ""
                    newest_gro  = ""
                    newest_time = None
                    for trr in glob.glob("melting*trr"):
                        mytime = os.path.getmtime(trr)
                        if None == newest_time or mytime > newest_time:
                            newest_time = mytime
                            newest_trr  = trr
                            mygro = trr[:-3] + "gro"
                            if os.path.exists(mygro):
                                newest_gro = mygro
                            else:
                                newset_gro = ""
                    if None != newest_time:
                        # Extract the temperature from the dir name
                        ptr = simdir.find(mol)
                        try:
                            temp = float(simdir[ptr+len(mol):])
                        except ValueError:
                            print("Cannot extract temperature from %s" % simdir)
                            temp = 0.0
                        # Check whether we really have to extend this one
                        if useall or int(temp) in ignore[molname]:
                            logfile = newest_trr[:-3] + "log"
                            tprfile = newest_trr[:-3] + "tpr"
                            if os.path.exists(logfile) and os.path.exists(tprfile):
                                mydict[mol][temp] = { "simdir": os.getcwd(),
                                                      "logfile": logfile,
                                                      "cptfile": newest_trr[:-3] + "cpt",
                                                      "tprfile": tprfile,
                                                      "trrfile": newest_trr,
                                                      "edrfile": newest_trr[:-3] + "edr",
                                                      "endtime": get_last_time(logfile)
                                }
                    os.chdir("..")
            os.chdir("..")
    os.chdir(pwd)
    return mydict

def write_run_job(target:str, nsteps:int):
    job = target + ".sh"
    with open(job, "w") as outf:
        outf.write("#!/bin/sh\n")
        outf.write("#SBATCH -t 72:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 12\n")
        outf.write("mpirun gmx_mpi mdrun -ntomp 1 -dd  2 3 2  -cpi %s.cpt -deffnm %s -nsteps %d -c NPT2.gro\n" % ( target, target, nsteps) )
    os.system("sbatch %s" % job)

def copy_ifnot_exists(src:str, dst:str):
    if not os.path.exists(dst):
        shutil.copy(src, dst)
        
def run_melt(mol:str, temp:float, prev:dict):
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

    moldb  = get_moldb(False)

    if csb:
        lisa_csb  = [ "ethane", "ethyne", "formamide", "formaldehyde", "urea", "ethylene" ]
        mydict = get_run_dict("/home/lschmidt/MELTING", lisa_csb, False)
    else:
        mydict = get_run_dict("/proj/nobackup/alexandria/lisa/melting", moldb.keys(), False)
    
    for mol in mydict:
        for temp in mydict[mol]:
            run_melt(mol, temp, mydict[mol][temp])
          #  sys.exit(0)

