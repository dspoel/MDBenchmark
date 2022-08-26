#!/usr/bin/env python3

import argparse, os, glob, sys
import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from xvgutils import *
from simtable import *
from collect_dynamics import *

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def fit_two(files:list, mol:str, temp:float, vtype:list, outf):
    for fnr in range(len(files)):
        filename = files[fnr]
        if os.path.exists(filename):
            labels, legends, dataset = read_xvg(filename)

            npoints = len(dataset[0].x)
            xdata = np.zeros(npoints)
            ydata = np.zeros(npoints)
            for i in range(npoints):
                xdata[i] = dataset[0].x[i]
                ydata[i] = dataset[0].y[i]
    
            popt, pcov = curve_fit(func, xdata, ydata)
            a0, k, S0 = tuple(popt)
            tau = 0.0
            if (k > 0):
                tau = 1.0/k
            printstr = ("%s,%g,%s,%g,%g,%g" % (mol, temp, vtype[fnr], a0, tau, S0))
            if None != outf:
                outf.write("%s\n" % printstr)
            else:
                print(printstr)

def parseArguments():
    parser = argparse.ArgumentParser(
      prog='ana_dynamics.py',
      description=
"""
Script to analyse dynamics in solid or melting simulations.
""")
    parser.add_argument("-files", "--files", nargs="+", help="The file(s) to analyze, if none is given all will be analysed", type=str, default=None)
    return parser.parse_args()
    
if __name__ == '__main__':
    args = parseArguments()
    if None != args.files:
        fit_two(args.files, "mol", 0.0, args.files, None)
    else:
        simtable_files = [ "csb_simtable.csv", "keb_simtable.csv" ]
        simtable       = get_simtable(simtable_files)
        with open("fit_results.csv", "w") as outf:
            outf.write("#molecule,temp,vector,a0,tau,S0\n")
            os.chdir("bcc/melt")
            for mol in simtable.keys():
                if os.path.exists(mol):
                    os.chdir(mol)
                    for temp in sorted(simtable[mol]):
                        if mol in sim_status and temp in sim_status[mol]["success"]:
                            files = []
                            for vect in [ "acf", "plane" ]:
                                files.append("rot%s_%g.xvg" % ( vect, temp) )
                            fit_two(files, mol, temp, outf)
                    os.chdir("..")
