#!/usr/bin/env python3
        
import os, shutil, glob, sys, math
from molecule_db import *

def run_rotacf(jobname: str, compound:str, tbegin: float, tend: float, traj: str, tpr: str,
               indexdir: str, rotacfout: str, rotplane: str, msdout: str):
    if os.path.exists(rotacfout) and os.path.exists(msdout) and os.path.exists(rotplane):
        return
    with open(jobname, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
#        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        outf.write("gmx rotacf -d -n %s/%s_rotaxis.ndx -f %s -s %s -o %s -b %d -e %d \n" % ( indexdir, compound, traj, tpr, rotacfout, tbegin, tend ))
        planendx = ( "%s/%s_rotplane.ndx" % ( indexdir, compound ))
        if os.path.exists(planendx):
            outf.write("gmx rotacf -n %s -f %s -s %s -o %s -b %d -e %d \n" % ( planendx, traj, tpr, rotplane, tbegin, tend ))
        outf.write("echo 0 | gmx msd -f %s -s %s -o %s -b %d -e %d \n" % ( traj, tpr, msdout, tbegin, tend ))
    os.system("sbatch %s" % jobname)

def get_last_time(logfile:str) -> float:
    with open(logfile) as inf:
        lines  = inf.readlines()
        nlines = len(lines)
        for line in range(nlines-1, 0, -1):
            if lines[line].find("    Step           Time") >= 0 and line < nlines-1:
                words = lines[line+1].strip().split()
                try:
                    return float(words[1])
                except:
                    print("Cannot find final MD time for %s" % logfile)
                    return 0.0
    return 0.0

def get_dict(topdir: str, moldb):
    if not os.path.exists(topdir):
        sys.exit("No such dir %s" % topdir)
    pwd = os.getcwd()
    os.chdir(topdir)
    lisa_name = { "acooh": "acoh", "12-ethanediamine": "ethylendiamine", "ethyleneglycol": "ethylenglycol", "ethylene": "ethene" }
    lisa_csb  = [ "ethane", "ethyne", "formamide", "formaldehyde", "urea", "ethylene" ]
    lisa_csb  = [ "ethylene" ]
    for molname in lisa_csb:
        mol = molname
        if mol in lisa_name:
            mol = lisa_name[mol]

        if os.path.exists(mol):
            os.chdir(mol)
            for simdir in glob.glob("*%s*" % mol):
                if os.path.isdir(simdir):
                    os.chdir(simdir)
                    newest_trr  = ""
                    newest_time = None
                    for trr in glob.glob("melting*trr"):
                        mytime = os.path.getmtime(trr)
                        if None == newest_time or mytime > newest_time:
                            newest_time = mytime
                            newest_trr  = trr
                    if None != newest_time:
                        # Extract the temperature from the dir name
                        ptr = simdir.find(mol)
                        try:
                            temp = float(simdir[ptr+len(mol):])
                        except ValueError:
                            print("Cannot extract temperature from %s" % simdir)
                            temp = 0.0
                        logfile = newest_trr[:-3] + "log"
                        tprfile = newest_trr[:-3] + "tpr"
                        if os.path.exists(logfile) and os.path.exists(tprfile):
                            endtime = get_last_time(logfile)
                            mydir   = os.getcwd()
                            workdir = ("%s/bcc/melt/%s" % ( pwd, molname ) )
                            if not os.path.isdir(workdir):
                                sys.exit("No such directory %s" % workdir)
                            os.chdir(workdir)
                            jobname = ("%s_%g.sh" % ( molname, temp ))
                            traj    = ("%s/%s" % ( mydir, newest_trr ))
                            tpr     = ("%s/%s" % ( mydir, tprfile ))
                            rotacfout = ("rotacf_%g.xvg" % temp )
                            rotplane  = ("rotplane_%g.xvg" % temp )
                            msdout    = ("msd_%g.xvg" % temp )
                            indexdir  = "../../../index"
                            run_rotacf(jobname, molname, endtime-1000, endtime, traj, tpr,
                                       indexdir, rotacfout, rotplane, msdout)
                            os.chdir(mydir)
                    os.chdir("..")
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
    #get_dict("/proj/nobackup/alexandria/lisa/melting", moldb)
    get_dict("/home/lschmidt/MELTING", moldb)

