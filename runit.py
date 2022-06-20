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

def fetch_mdp(src:str, dest:str, temp:int):
    if os.path.exists(dest):
        os.unlink(dest)
    shutil.copy(src, dest)
    with open(dest, "a") as mdpf:
        mdpf.write("ref_t = %d\n" % temp)
    
def write_input(compound, phase, top, temp, moldb):
    if (("solid" == phase and os.path.exists("NPT.gro")) or
        ("gas" == phase and os.path.exists("NVT.gro")) or
        (temp == 0)):
        return None
        
    job = ("%s-%s-%s-%s.sh" % ( compound, top, phase, temp ))
    with open(job, "w") as outf:
        outf.write("#!/bin/sh\n")
        outf.write("#SBATCH -t 71:00:00\n#SBATCH -A SNIC2021-3-8\n")
        confin = ( "../../../../box/%s/%s.pdb" % ( phase, compound ))
        
        if "solid" == phase:
            nmol = moldb[compound]["nsolid"]
            outf.write("#SBATCH -n 14\n")
            for sim in [ "NVT", "NPT" ]:
                mdp = sim + ".mdp"
                tpr = sim + ".tpr"
                fetch_mdp(("../../../../MDP/%s%s.mdp" % ( sim, phase )), mdp, temp)
                outgro = sim + ".gro"
                if not os.path.exists(outgro):
                    outf.write("gmx grompp -maxwarn 2 -c %s -f %s -o %s\n" % ( confin, mdp, tpr ) )
                    outf.write("mpirun -np 12 gmx_mpi mdrun -dd 3 2 2 -s %s -deffnm %s -c %s\n" % ( tpr, sim, outgro))
                confin = outgro
        else:
            nmol   = 1
            outf.write("#SBATCH -n 1\n")
            sim = "NVT"
            mdp = sim + ".mdp"
            tpr = sim + ".tpr"
            fetch_mdp(("../../../../MDP/%s%s.mdp" % ( sim, phase )), mdp, temp)
            outf.write("gmx grompp -maxwarn 2 -c %s -f %s -o %s\n" % ( confin, mdp, tpr ) )
            outf.write("gmx mdrun -s %s -deffnm %s  \n" % (tpr, sim))
        write_top(compound, nmol)
        
    return job

moldb = get_moldb(True)
for top in [ "bcc", "resp" ]:
    os.chdir(top)
    for phase in [ "gas", "solid" ]:
        os.chdir(phase)
        for compound in moldb.keys():
            os.makedirs(compound, exist_ok=True)
            os.chdir(compound)
            mytemps = list(range(moldb[compound]["Tmin"], moldb[compound]["Tmax"]+1, moldb[compound]["DeltaT"]))
            for et in moldb[compound]["ExtraT"]:
                if not et in mytemps:
                    mytemps.append(et)
            for temp in mytemps:
                os.makedirs(str(temp), exist_ok=True)
                os.chdir(str(temp))
                job = write_input(compound, phase, top, temp, moldb)
                if None != job:
                    print("Generated script %s" % job)
                    for slurmfile in glob.glob("slurm*"):
                        os.unlink(slurmfile)
                    os.system("sbatch %s" % job)
#                    sys.exit(0)
                os.chdir("..")
            os.chdir("..")
        os.chdir("..")
    os.chdir("..")
