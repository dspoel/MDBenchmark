#!/usr/bin/env python3

import os
from molecule_db import *

rotaxis = { "12-benzenediol": [ 1, 8, 3, 6 ], 
    "acooh": [ 1, 2, 1, 3 ], 
    "ethanol": [ 1, 8, 2, 6 ], 
    "formamide": [ 1, 4, 3, 6 ], 
    "methanol": [ 1, 6, 2, 5 ], 
    "propane": [ 1, 5, 5, 8 ], 
    "12-ethanediamine": [ 2, 5, 6, 9 ], 
    "benzene": [ 1, 7, 5, 11 ], 
    "ethylene": [ 2, 5, 3, 6 ], 
    "formic_acid": [ 1, 3, 1, 4 ], 
    "naphthalene": [ 1, 2, 7, 10 ], 
    "pyridine": [ 1, 8, 1, 4 ], 
    "123-benzenetriol": [ 1, 3, 1, 5 ], 
    "cyclohexane": [ 1, 7, 1, 13 ], 
    "ethyleneglycol": [ 1, 3, 6, 9 ], 
    "furan": [ 6, 8, 6, 4 ], 
    "octanoic_acid": [ 6, 21, 7, 8 ], 
    "succinic_acid": [ 2, 8, 6, 8 ], 
    "14-benzoquinone": [ 3, 7, 3, 8 ], 
    "cyclopropane": [ 1, 2, 1, 3 ], 
    "ethyne": [ 1, 3 ], 
    "imidazole": [ 5, 8, 2, 8 ], 
    "pentane": [ 5, 8, 8, 11 ], 
    "uracil": [ 4, 9, 10, 12 ], 
    "acetamide": [ 3, 6, 2, 5 ], 
    "ethane": [ 2, 6, 3, 7 ], 
    "formaldehyde": [ 1, 3, 1, 4 ], 
    "menh2": [ 1, 2, 1, 3 ], 
    "phenol": [ 1, 5, 5, 9 ], 
    "urea": [ 3, 4, 1, 2 ]
}

rotplane = { "12-benzenediol": [ 1, 3, 5 ],
             "acooh": [ 1, 2, 3 ],
             "ethanol": [ 1, 5, 8 ],
             "formamide": [ 1, 2, 4 ],
             "methanol": [ 3, 1, 2 ],
             "propane": [ 1, 5, 8 ],
             "12-ethanediamine": [ 1, 4, 7 ],
             "benzene": [ 1, 5, 9 ],
             "ethylene": [ 2, 3, 4 ],
             "formic_acid": [ 1, 3, 4 ],
             "naphthalene": [ 8, 1, 10 ],
             "pyridine": [ 1, 4, 8 ],
             "123-benzenetriol": [ 1, 3, 5 ],
             "cyclohexane": [ 1, 7, 13 ],
             "ethyleneglycol": [ 1, 3, 6 ],
             "furan": [ 2, 6, 8 ],
             "octanoic_acid": [ 5, 7, 8 ],
             "succinic_acid": [ 2, 4, 6 ],
             "14-benzoquinone": [ 3, 7, 8 ],
             "cyclopropane": [ 1, 2, 3 ],
             "imidazole": [ 5, 7, 9 ],
             "pentane": [ 5, 8, 11 ],
             "uracil": [ 1, 9, 11 ],
             "acetamide": [ 2, 3, 6 ],
             "ethane": [ 2, 5, 8 ],
             "formaldehyde": [ 1, 3, 4],
             "menh2": [ 2, 3, 4 ],
             "phenol": [ 1, 5, 9 ],
             "urea": [ 2, 3, 4 ]
             }
             
moldb = get_moldb(True)
for mol in moldb.keys():
    nsolid = moldb[mol]["nsolid"]
    if mol in rotaxis:
        gasbox  = ( "box/gas/%s.pdb" % mol )
        natom   = 0
        with open(gasbox, "r") as inf:
            for line in inf:
                if line.find("ATOM ") >= 0:
                    natom += 1
        outfile = ( "index/%s_rotaxis.ndx" % mol )
        with open(outfile, "w") as outf:
            outf.write("[ rotaxis ]\n")
            for i in range(nsolid):
                if mol in rotaxis:
                    for j in range(len(rotaxis[mol])):
                        outf.write("  %d" % ( i*natom+rotaxis[mol][j] ) )
                    outf.write("\n")
        outfile = ( "index/%s_rotplane.ndx" % mol )
        with open(outfile, "w") as outf:
            outf.write("[ rotplane ]\n")
            for i in range(nsolid):
                if mol in rotplane:
                    for j in range(len(rotplane[mol])):
                        outf.write("  %d" % ( i*natom+rotplane[mol][j] ) )
                    outf.write("\n")
