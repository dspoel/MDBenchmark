#!/usr/bin/env python3
        
import os, shutil, glob, sys, math
from molecule_db import *
from simtable    import *

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0

def use_sim(simtable:dict, mol:str, temp: int) -> bool:
    if not mol in simtable or not temp in simtable[mol]:
        print("Cannot find mol %s, temp %g in simtable. Sorry." % ( mol, temp ))
        return False
    if csb and simtable[mol][temp]["host"] == "csb":
        return True
    if not csb and simtable[mol][temp]["host"] == "keb":
        return True
    return False
        
def run_rotacf(jobname: str, compound:str, tbegin: float, tend: float, traj: str, tpr: str,
               indexdir: str, rotacfout: str, rotplane: str, msdout: str):
#    if os.path.exists(rotacfout) and os.path.exists(msdout) and os.path.exists(rotplane):
#        return
    with open(jobname, "w") as outf:
        outf.write("#!/bin/bash\n")
        outf.write("#SBATCH -t 24:00:00\n")
        if not csb:
            outf.write("#SBATCH -A SNIC2021-3-8\n")
        outf.write("#SBATCH -n 1\n")
        outf.write("gmx rotacf -d -n %s/%s_rotaxis.ndx -f %s -s %s -o %s -b %d -e %d \n" % ( indexdir, compound, traj, tpr, rotacfout, tbegin, tend ))
        planendx = ( "%s/%s_rotplane.ndx" % ( indexdir, compound ))
        if os.path.exists(planendx):
            outf.write("gmx rotacf -n %s -f %s -s %s -o %s -b %d -e %d \n" % ( planendx, traj, tpr, rotplane, tbegin, tend ))
        outf.write("echo 0 | gmx msd -f %s -s %s -o %s -b %d -e %d \n" % ( traj, tpr, msdout, tbegin, tend ))
    os.system("sbatch %s" % jobname)

def ana_dynamics(topdirs: list, molnames:list):
    simtable = get_simtable()
    dump_simtable(simtable)
    pwd = os.getcwd()
    print("pwd %s" % pwd)
    lisa_name = { "acooh": "acoh", "12-ethanediamine": "ethylendiamine", "ethyleneglycol": "ethylenglycol", "ethylene": "ethene" }
    for molname in molnames:
        mol = molname
        if mol in lisa_name:
            mol = lisa_name[mol]

        for topdir in topdirs:
            if not os.path.exists(topdir):
                continue
            os.chdir(topdir)
            if os.path.exists(mol):
                os.chdir(mol)
                for simdir in glob.glob("*%s*" % mol):
                    if os.path.isdir(simdir):
                        os.chdir(simdir)
                        newest_trr  = ""
                        newest_gro  = ""
                        newest_time = None
                        for trr in glob.glob("melting*trr"):
                            if trr.find("nvt") >= 0 or trr.find("NVT") >= 0:
                                continue
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
                            logfile = newest_trr[:-3] + "log"
                            tprfile = newest_trr[:-3] + "tpr"
                            if os.path.exists(logfile) and os.path.exists(tprfile) and use_sim(simtable, molname, temp):
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
                                run_rotacf(jobname, molname, endtime-200, endtime, traj, tpr,
                                           indexdir, rotacfout, rotplane, msdout)
                                if len(newest_gro) > 4:
                                    shutil.copyfile(("%s/%s" % ( mydir, newest_gro)), ("final_%g.gro" % temp ))
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
        topdirs = [ "/proj/nobackup/alexandria/spoel/MDBenchmark/melting",
                    "/proj/nobackup/alexandria/lisa/melting",
                    "/home/lschmidt/MELTING" ]
        ana_dynamics(topdirs, moldb.keys())

