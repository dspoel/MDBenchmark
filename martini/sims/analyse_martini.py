#!/usr/bin/env python3

import os, glob

for comp in glob.glob("*"):
    if not os.path.isdir(comp):
        continue
    os.chdir(comp)
    diffs = {}
    for temp in glob.glob("*"):
        if not os.path.isdir(temp):
            continue
        os.chdir(temp)
        msd = "msd_NPT.xvg"
        if os.path.exists(msd):
            with open(msd, "r") as inf:
                for line in inf:
                    if line.find("D[    System]") >= 0:
                        words = line.strip().split()
                        diffs[int(temp)] = { "value": float(words[4]), "error": float(words[6][:-1]) }
        os.chdir("..")
    adxvg = "alldiff.xvg"
    with open(adxvg, "w") as outf:
        outf.write("@    title \"%s\"\n" % comp)
        outf.write("@    xaxis  label \"T (K)\"\n")
        outf.write("@    yaxis  label \"D (1e-5 cm2/s)\"\n")
        for temp in sorted(diffs.keys()):
            outf.write("%3d  %10g\n" % ( temp, diffs[temp]["value"] ))
    os.system("viewxvg -f %s -noshow -pdf %s" % ( adxvg, "diff-" + comp + ".pdf") )
    os.chdir("..")
