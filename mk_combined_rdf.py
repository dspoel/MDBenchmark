#!/usr/bin/env python3

import os, glob
from molecule_db import *

def mklist():
    mydirs = glob.glob("[0-9]*")
    mytemp = []
    for md in mydirs:
        mytemp.append(int(md))
    return sorted(mytemp)

def run_comp(compound:str):    
    mylist = mklist()

    mycmd = ( "viewxvg -xmin 0. -ymin 0.25 -xmax 1 -ymax 4 -title 'RDF %s' -legend_right -noshow -pdf rdf_%s.pdf" % ( compound, compound ))

    mycmd +=  " -f xray/rdf.xvg"
    for ml in mylist:
        mycmd += (" %s/rdf.xvg" % str(ml) )
    
    mycmd += " -label xray"
    for ml in mylist:
        mycmd += " " + str(ml)

    print(mycmd)
    os.system(mycmd)

def do_rdf(moldb):
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            run_comp(compound)
            os.chdir("..")

moldb  = get_moldb(False)

for top in [ "bcc", "resp" ]:
    print("Looking for %s" % top)
    if os.path.isdir(top):
        os.chdir(top)
        phase = "solid"
        if os.path.isdir(phase):
            os.chdir(phase)
            do_rdf(moldb)
            os.chdir("..")
        os.chdir("..")
