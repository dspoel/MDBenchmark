#!/usr/bin/env python3

import os, glob
from molecule_db import *
from analyse import get_tail

molrename = { "menh2": "methylamine", "acooh": "acetic acid" }

def plot_it(mol:str):
    title = mol
    if title in molrename:
        title = molrename[title]
    os.system("viewxvg -f temp_diff.xvg temp_S0.xvg -alfs 14 -lfs 16 -tfs 16 -ymin -0.05 -ymax 1.2 -mk  -label D S0 -title %s -pdf %s_dynamics.pdf -noshow" % ( title, mol ))
    
moldb = get_moldb(False)
os.chdir("bcc/melt")
for mol in moldb:
    if os.path.isdir(mol):
        os.chdir(mol)
        plot_it(mol)
        os.chdir("..")
