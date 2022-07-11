#!/usr/bin/env python3

import os, shutil, glob
from molecule_db import *

def write_top(compound:str, nmol: int):
    with open("topol.top", "w") as outf:
        outf.write("#include \"../../../itp/%s.itp\"\n" % compound)
        outf.write("[ system ]\n")
        outf.write("%s\n" % compound)
        outf.write("[ molecules ]\n")
        outf.write("MOL %d\n" % ( nmol ))

def fetch_mdp(src:str, dest:str, temp:int, pres = None):
    if os.path.exists(dest):
        os.unlink(dest)
    shutil.copy(src, dest)
    with open(dest, "a") as mdpf:
        mdpf.write("ref_t = %d\n" % temp)
        if None != pres:
            mdpf.write("ref_p = %f %f %f 0 0 0\n" % ( pres, pres, pres ) )

def get_nsteps(logfile:str):
    step = None
    with open(logfile, "r") as inf:
        lines = inf.readlines()
        nlines = len(lines)
        for i in range(nlines):
            if lines[i].find("           Step           Time") >= 0 and i < nlines-1:
                oldstep = step
                try:
                    words = lines[i+1].split()
                    step  = int(words[0])
                except ValueError:
                    step = oldstep
    return step

def write_input(compound, phase, top, temp, moldb):
    if (("solid" == phase and os.path.exists("NPT2.gro")) or
        ("gas" == phase and os.path.exists("NVT.gro")) or
        (temp == 0)):
        return None
        
    job = ("%s-%s-%s-%s.sh" % ( compound, top, phase, temp ))
    with open(job, "w") as outf:
        outf.write("#!/bin/sh\n")
        outf.write("#SBATCH -t 36:00:00\n")
        outf.write("#SBATCH -A SNIC2021-3-8\n")
        confin = ( "../../../../box/%s/%s.pdb" % ( phase, compound ))
        pres   = 1
        if "solid" == phase:
            ncores = 12
            nmol = moldb[compound]["nsolid"]
            outf.write("#SBATCH -n %d\n" % ncores)
            for sim in [ "EM", "NVT", "NPT", "NPT2" ]:
                tpr    = sim + ".tpr"
                outgro = sim + ".gro"
                mdp    = sim + ".mdp"
                if not os.path.exists(outgro):
                    hname = "HOSTNAME"
                    if hname in os.environ and os.environ[hname].find("csb.bmc.uu.se") >= 0:
                        mdrun = "gmx mdrun -ntmpi 8  -ntomp 1 -dd 2 2 2"
                    else:
                        mdrun = "mpirun gmx_mpi mdrun -ntomp 1 -dd 3 2 2 "
                    if sim == "NPT2":
                        oldsim = "NPT"
                        cpt    = oldsim + ".cpt"
                        nsteps_done = get_nsteps(oldsim + ".log")
                        nsteps_left = max(10000, 15000000-nsteps_done)
                        outf.write("%s -cpi %s -deffnm %s -nsteps %d -c %s\n" % ( mdrun, cpt, oldsim, nsteps_left, outgro))
                    else:
                        pres   = None
                        if sim.find("NPT") >= 0:
                            pres = moldb[compound]["Pcryst"]
                        fetch_mdp(("../../../../MDP/%s%s.mdp" % ( sim, phase )), mdp, temp, pres)
                        outf.write("gmx grompp -maxwarn 2 -c %s -f %s -o %s\n" % ( confin, mdp, tpr ) )
                        outf.write("%s -s %s -deffnm %s -c %s\n" % ( mdrun, tpr, sim, outgro))
                confin = outgro
        else:
            nmol   = 1
            outf.write("#SBATCH -n 1\n")
            sim = "NVT"
            mdp = sim + ".mdp"
            tpr = sim + ".tpr"
            fetch_mdp(("../../../../MDP/%s%s.mdp" % ( sim, phase )), mdp, temp, None)
            outf.write("gmx grompp -maxwarn 2 -c %s -f %s -o %s\n" % ( confin, mdp, tpr ) )
            outf.write("gmx mdrun -s %s -deffnm %s  \n" % (tpr, sim))
        write_top(compound, nmol)
        
    return job

moldb = get_moldb(True)
for top in [ "bcc", "resp" ]:
    os.chdir(top)
    for phase in [ "gas" ]:
        os.chdir(phase)
        for compound in moldb.keys():
            os.makedirs(compound, exist_ok=True)
            os.chdir(compound)
            mytemps = list(range(moldb[compound]["Tmin"], moldb[compound]["Tmax"]+1, moldb[compound]["DeltaT"]))
            for et in moldb[compound]["ExtraT"]:
                if not et in mytemps:
                    mytemps.append(et)
            for temp in mytemps:
                if temp == 0:
                    continue
                os.makedirs(str(temp), exist_ok=True)
                os.chdir(str(temp))
                job = write_input(compound, phase, top, temp, moldb)
                if None != job:
                    print("Generated script %s" % job)
                    for slurmfile in glob.glob("slurm*"):
                        os.unlink(slurmfile)
                    print("Submitting %s" % job)
                    os.system("sbatch %s" % job)
#                    sys.exit(0)
                os.chdir("..")
            os.chdir("..")
        os.chdir("..")
    os.chdir("..")
