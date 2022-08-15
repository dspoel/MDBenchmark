#!/usr/bin/env python3

import os, glob
from molecule_db import *
from melt_continue import *

def get_natom(gro:str) -> int:
    try:
        with open(gro, "r") as inf:
            fff   = inf.readlines()
            return int(fff[1].strip())
    except:
        return 0

def get_nmol(mol:str, natom:int) -> int:
    finals = glob.glob("final*gro")
    ncryst = get_natom(finals[0])
    if (natom > 0):
        return ncryst/natom
    else:
        return 0

if __name__ == '__main__':
    moldb = get_moldb(False)
    host  = "keb"
    if csb:
        mydict = get_run_dict("/home/lschmidt/MELTING", moldb.keys(), True)
        host   = "csb"
    else:
        mydict = get_run_dict("/proj/nobackup/alexandria/lisa/melting", moldb.keys(), True)

    csv = open("mm.csv", "w")
    textab = "melt_mols.tex"
    with open(textab, "w") as outf:
        outf.write("\\begin{table}[ht!]\n")
        outf.write("\\caption{Overview of melting simulations performed. Number of molecules in the system, temperature (K) and simulation length (ns).}\n")
        outf.write("\\label{meltsims}\n")
        outf.write("\\begin{tabular}{lcc}\n")
        outf.write("Compound & \# Mol & Temperature (Simulation length) \\\\\n")
        outf.write("\\hline\n")
        os.chdir("bcc/melt")
        for mol in mydict:
            if os.path.isdir(mol):
                os.chdir(mol)
                nmol = get_nmol(mol, moldb[mol]["natom"])
                outf.write("%s & %d &" % ( mol, nmol ) )
                for temp in sorted(mydict[mol].keys()):
                    mytime = mydict[mol][temp]["endtime"]/1000
                    if mytime >= 1:
                        outf.write(" %g(%.0f)" % ( temp, mytime  ) )
                        csv.write("%s|%s|%g|%g\n" % ( host, mol, temp, mytime ) ) 
                outf.write("\\\\\n")
                os.chdir("..")
        outf.write("\\hline\n")
        outf.write("\\end{tabular}\n")
        outf.write("\\end{table}\n")
    csv.close()
