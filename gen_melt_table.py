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

    with open("melt_table.csv", "w") as csv:
        os.chdir("bcc/melt")
        for mol in mydict:
            if os.path.isdir(mol):
                os.chdir(mol)
                nmol = get_nmol(mol, moldb[mol]["natom"])
                for temp in sorted(mydict[mol].keys()):
                    mytime = mydict[mol][temp]["endtime"]/1000
                    if mytime >= 1:
                        csv.write("%s|%g|%g|%s|%d\n" % ( mol, temp, mytime, host, nmol ) ) 
                os.chdir("..")
