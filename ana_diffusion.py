#!/usr/bin/env python3

import os, glob, sys
from molecule_db import *

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

def write_job(rootdir:str, mol:str, tempdict) -> str:
    pwd = os.getcwd()
    os.chdir(rootdir)
    target_dir = "melting_diff"
    os.makedirs(target_dir, exist_ok=True)
    os.chdir(target_dir)
    os.makedirs(mol, exist_ok=True)
    os.chdir(mol)
    job = "mol-diff.sh"
    with open(job, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        for temp in tempdict:
            msdxvg = ( "msd_%f.xvg" % temp )
            trr = tempdict[temp]["dir"]+"/"+tempdict[temp]["trr"]
            tpr = tempdict[temp]["dir"]+"/"+tempdict[temp]["tpr"]
            outf.write("echo 0 | gmx msd -trestart 10000 -f %s -s %s -o %s -b %f\n" % ( trr, tpr, msdxvg, tempdict[temp]["end"]-1000) )
    os.system("sbatch %s" % job)
    os.chdir(pwd)

def get_dict(topdir: str, moldb):
    if not os.path.exists(topdir):
        sys.exit("No such dir %s" % topdir)
    pwd = os.getcwd()
    os.chdir(topdir)
    mydict = {}
    for mol in [ "acoh", "ethylendiamine", "ethylenglycol" ]:
        if os.path.exists(mol):
            os.chdir(mol)
            mydict[mol] = {}
            for simdir in glob.glob("OUT-%s*" % mol):
                if os.path.exists(simdir):
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
                            mydict[mol][temp] = { "dir": mydir, "trr": newest_trr, "tpr": tprfile, "end": endtime }
                    os.chdir("..")
            write_job(pwd, mol, mydict[mol])
            os.chdir("..")
    os.chdir(pwd)

moldb = get_moldb(False)
get_dict("/proj/nobackup/alexandria/lisa/melting", moldb)

