#!/usr/bin/env python3

import os, glob
from simtable import *

def check_trj(mol:str, temp:str, simdir:str, traj:str):
    for output in [ "rotacf_", "rotplane_", "msd_", "rdf_" ]:
        filename = ( "%s%g.xvg" % ( output, temp ))
        if not os.path.exists(filename):
            print("Cannot find %s/%s" % ( mol, filename ))
        else:
            foundTraj = False
            with open(filename, "r") as inf:
                for line in inf:
                    if line.find(simdir+"/"+trj) >= 0:
                        foundTraj = True
            if not foundTraj:
                print("Incorrect trajectory used in %s/%s should be %s/%s" % (mol, filename, simdir, trj))
    
if __name__ == '__main__':
    simtable_files = [ "csb_simtable.csv", "keb_simtable.csv" ]
    simtable      = get_simtable(simtable_files)
    os.chdir("bcc/melt")
    for molname in simtable.keys():
        os.chdir(molname)
        for temp in simtable[molname]:
            simdir    = simtable[molname][temp]["simdir"]
            trj       = simtable[molname][temp]["trrfile"]
            check_trj(molname, temp, simdir, trj)
            length    = simtable[molname][temp]["length"]
            minlength = 2000
            if length < minlength:
                print("Length for %s %s is %g, please extend to at least %g ps" % ( simdir, trj, length, minlength ))
        os.chdir("..")
