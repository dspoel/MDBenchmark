#!/usr/bin/env python3

import os, glob

for mydir in glob.glob("*"):
    if os.path.isdir(mydir):
        os.chdir(mydir)
        os.system("gmx editconf -f ../../../box/solid/%s.pdb -n index -o ../../box/solid/%s.pdb" % ( mydir, mydir ))
        os.chdir("..")
