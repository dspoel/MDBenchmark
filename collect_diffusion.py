#!/usr/bin/env python3

import os, glob
from molecule_db import *

def do_one():
    td = {}
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
        for temp in sorted(td.keys()):
            outf.write("%10g  %10g  %10g\n" % ( temp, td[temp][0], td[temp][1] ) )

moldb = get_moldb(False)
os.chdir("bcc/melt")
for mol in moldb:
    if os.path.isdir(mol):
        os.chdir(mol)
        do_one()
        os.chdir("..")
