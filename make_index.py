#!/usr/bin/env python3

import os
from molecule_db import *

rotaxis = { "12-benzenediol": [ 1, 8 ], 
    "acooh": [ 1, 2 ], 
    "ethanol": [ 1, 8 ], 
    "formamide": [ 1, 4 ], 
    "methanol": [ 1, 3 ], 
    "propane": [ 1, 6 ], 
    "12-ethanediamine": [ 1, 10 ], 
    "benzene": [ 1, 7 ], 
    "ethylene": [ 1, 4 ], 
    "formic_acid": [ 3, 4 ], 
    "naphthalene": [ 7, 10 ], 
    "pyridine": [ 1, 6 ], 
    "123-benzenetriol": [ 1, 8 ], 
    "cyclohexane": [ 1, 10 ], 
    "ethyleneglycol": [ 1, 9 ], 
    "furan": [ 3, 9 ], 
    "octanoic_acid": [ 6, 21 ], 
    "succinic_acid": [ 1, 2 ], 
    "14-benzoquinone": [ 1, 2 ], 
    "cyclopropane": [ 1, 6 ], 
    "ethyne": [ 1, 3 ], 
    "imidazole": [ 5, 8 ], 
    "pentane": [ 1, 14 ], 
    "uracil": [ 4, 9 ], 
    "acetamide": [ 3, 6 ], 
    "ethane": [ 1, 5 ], 
    "formaldehyde": [ 1, 2 ], 
    "menh2": [ 1, 4 ], 
    "phenol": [ 5, 12 ], 
    "urea": [ 3, 4 ]
}

moldb = get_moldb(True)
for mol in moldb.keys():
    nsolid = moldb[mol]["nsolid"]
    gasbox  = ( "box/gas/%s.pdb" % mol )
    natom   = 0
    with open(gasbox, "r") as inf:
        for line in inf:
            if line.find("ATOM ") >= 0:
                natom += 1
    if mol in rotaxis:
        outfile = ( "index/%s_rotaxis.ndx" % mol )
        with open(outfile, "w") as outf:
            outf.write("[ rotaxis ]\n")
            for i in range(nsolid):
                outf.write("%d  %d\n" % ( i*natom+rotaxis[mol][0],
                                          i*natom+rotaxis[mol][1] ) )
    outfile = ( "index/%s_rmsd.ndx" % mol)
    with open(outfile, "w") as outf:
        for i in range(nsolid):
            outf.write("[ mol%d ]\n" % (i+1))
            for j in range(1, natom+1):
                outf.write(" %d" % ( i*natom+j ))
            outf.write("\n")
        
