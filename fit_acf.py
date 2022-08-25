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

def fit_two(mol:str, temp:float, outf):
    for vect in [ "acf", "plane" ]:
        filename = ("rot%s_%g.xvg" % ( vect, temp) )
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
            outf.write("%s,%g,%s,%g,%g,%g\n" % (mol, temp, vect, a0, tau, S0))

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
                    fit_two(mol, temp, outf)
            os.chdir("..")
