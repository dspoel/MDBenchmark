#!/usr/bin/env python3

import os, glob
from molecule_db import *
from collect_dynamics import sim_status
from get_csv_rows import *

molrename = { "menh2": "methylamine", "acooh": "acetic acid" }

def get_ref(mol:str):
    with open("../../../allresults.csv", "r") as inf:
        for line in inf:
            if line.find("#") < 0:
                row = line.split(",")
                if len(row) > 21:
                    if row[0] == mol and row[20] != "liquid":
                        return row[1], row[20], ("../../solid/%s/%s/rdf.xvg" % ( mol, row[1] ))
    return 0, "", ""

def plot_it(mol:str):
    temps = sim_status[mol]["success"]
    if len(temps) == 0:
        return
    title = mol
    if title in molrename:
        title = molrename[title]
    filelist = ""
    templist = ""
    reftemp, refphase, reffile = get_ref(mol)
    if len(reffile) > 0:
        filelist = reffile
        templist = ( "%s@%s" % ( refphase, reftemp ) )
    found_data = False
    sorted_temps = sorted(temps)
    ndelta = 1
    if len(sorted_temps) > 12:
        ndelta = 2
        if len(sorted_temps) > 24:
            ndelta = 3
    for t in range(0, len(sorted_temps), ndelta):
        rdf = ( "rdf_%g.xvg" % sorted_temps[t])
        if os.path.exists(rdf):
            filelist += (" %s" % rdf)
            templist += (" %g" % sorted_temps[t])
            found_data = True
    if found_data:
        os.system("viewxvg -f %s -alfs 18 -lfs 14 -tfs 18 -legend_out -ymin -0.02 -ymax 4 -xmin 0 -xmax 1.2  -label %s -title '%s' -pdf ../RDF/%s_rdf.pdf -noshow" % ( filelist, templist, title, mol ))
    
moldb = get_moldb(False)
os.chdir("bcc/melt")
for mol in moldb.keys():
    if os.path.isdir(mol):
        os.chdir(mol)
        plot_it(mol)
        os.chdir("..")
