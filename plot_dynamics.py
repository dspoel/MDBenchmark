#!/usr/bin/env python3

import os, glob
from molecule_db import *
from analyse import get_tail

molrename = { "menh2": "methylamine", "acooh": "acetic acid" }

#[T_m_exp, T_m_sim]
melting_points = { "12-benzenediol":[377, 389.5], 
                   "12-ethanediamine":[284, 229], 
                   "123-benzenetriol":[403, 370.5],
                   "14-benzoquinone":[388, 400.5],
                   "acetamide":[354.15, 311.5], 
                   "acooh":[289.81, 274],
                   "benzene":[278.68, 225.5], 
                   "cyclohexane":[279.69, 301.5],
                   "cyclopropane":[175.47, 117.5], 
                   "ethane":[100, 131.5], 
                   "ethanol":[159.05, 166.5],
                   "ethylene":[104.01, 106.5],
                   "ethyleneglycol":[260.15, 217.5],  
                   "ethyne":[192.4, 174.5],
                   "formaldehyde":[181.15, 163.5],
                   "formamide":[298.15, 293 ],
                   "formic_acid":[281.55, 248.5], 
                   "furan":[187.55, 140], 
                   "imidazole":[363.65, 290.5],
                   "menh2":[179.69, 241], 
                   "methanol":[176, 188.5],
                   "naphthalene":[353, 350.5], 
                   "octanoic_acid":[289, 286.5],
                   "pentane":[143.42, 170.5], 
                   "phenol":[314, 269],
                   "propane":[85.46, 90], 
                   "pyridine":[231.53, 243.5],
                   "succinic_acid":[459, 391.5], 
                   "urea":[406, 436 ], 
                   "uracil":[611.15, 756]}

def get_min_max(infile:str):
    xmin = 1e9
    xmax = -1e9
    with open(infile, "r") as inf:
        for line in inf:
            words = line.split()
            try:
                xmin = min(xmin, float(words[0]))
                xmax = max(xmax, float(words[0]))
            except ValueError:
                if False:
                    print("Ignoring %s" % line)
    return xmin, xmax
            
def plot_it(mol:str):
    title = mol
    if title in molrename:
        title = molrename[title]
    if mol in melting_points:
        tmexp = ("%s_tmexp.xvg" % mol)
        with open(tmexp, "w") as outf:
            outf.write("@ xaxis label \"T (K)\"\n")
            outf.write("%g 0.5\n" % melting_points[mol][0])
        tmsim = ("%s_tmsim.xvg" % mol)
        with open(tmsim, "w") as outf:
            outf.write("@ xaxis label \"T (K)\"\n")
            outf.write("%g 0.5\n" % melting_points[mol][1])
        xmin, xmax = get_min_max("temp_S0.xvg")
        xmin = min(xmin, min(melting_points[mol][0], melting_points[mol][1]))-5
        xmax = max(xmax, max(melting_points[mol][0], melting_points[mol][1]))+5
        os.system("viewxvg -f temp_diff.xvg temp_S0.xvg temp_filesize.xvg %s %s -alfs 18 -lfs 14 -tfs 18 -legend_out -ymin -0.05 -ymax 1.2 -xmin %g -xmax %g -mk  -label D S0 Zip 'Tm,exp' 'Tm,sim' -title '%s' -pdf %s_dynamics.pdf -noshow" % ( tmexp, tmsim, xmin, xmax, title, mol ))
    
moldb = get_moldb(False)
os.chdir("bcc/melt")
for mol in moldb:
    if os.path.isdir(mol):
        os.chdir(mol)
        plot_it(mol)
        os.chdir("..")
