#!/usr/bin/env python3

import os, glob
from molecule_db import *
from analyse import get_tail

def do_msd():
    td  = {}
    for msd in glob.glob("msd*xvg"):
        temp = float(msd[4:-4])
        with open(msd, "r") as inf:
            for line in inf:
                if line.find("System") >= 0 and line.find("D") >= 0:
                    words = line.strip().split()
                    try:
                        ddd   = float(words[4])
                        err   = float(words[6][:-1])
                        td[temp] = [ ddd, err ]
                    except ValueError:
                        print("Incomprehensible line '%s'" % line)
    with open("temp_diff.xvg", "w") as outf:
        outf.write("@ xaxis legend \"T (K)\"\n")
        for temp in sorted(td.keys()):
            outf.write("%10g  %10g\n" % ( temp, td[temp][0] ) )

def do_rotacf():
    temps = []
    for rot in glob.glob("rotacf_*.xvg"):
        temps.append(rot[7:-4])

    S0 = {}
    for temp in temps:
        my_files = [ ("rotacf_%s.xvg" % temp ), ("rotplane_%s.xvg" % temp ) ]
        myS0 = get_tail(my_files, 250)
        if None != myS0:
            S0[float(temp)] = myS0 
    
    with open("temp_S0.xvg", "w") as outf:
        outf.write("@ xaxis legend \"T (K)\"\n")
        for temp in sorted(S0.keys()):
            outf.write("%10g  %10g\n" % ( temp, S0[temp] ) )

moldb = get_moldb(False)
os.chdir("bcc/melt")
lisa_csb  = [ "ethane", "ethyne", "formamide", "formaldehyde", "urea", "ethylene" ]
if False:
    for mol in moldb:
        if os.path.isdir(mol) and mol not in lisa_csb:
            os.chdir(mol)
            do_msd()
            do_rotacf()
            os.chdir("..")
else:
    for mol in lisa_csb:
        if os.path.isdir(mol):
            os.chdir(mol)
            do_msd()
            do_rotacf()
            os.chdir("..")
