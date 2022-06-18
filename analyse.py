#!/usr/bin/env python3

import os, shutil, glob, sys
from molecule_db import *

def input_dens(moldb):
    for compound in moldb.keys():
        dip    = "editconf.txt"
        newpdb = "new.pdb"
        os.system("gmx editconf -f box/solid/%s.pdb -density 100 -o %s > %s 2>&1" % ( compound, newpdb, dip))
        if os.path.exists(newpdb):
            with open(dip, "r") as inf:
                for line in inf:
                    if line.find("Density of input") >= 0:
                        moldb[compound]["solid_density"] = float(line.split()[3])
            os.unlink(newpdb)
        if os.path.exists(dip):
            os.unlink(dip)
    return moldb

def get_averages(infile:str, begin:int) -> list:
    ptxt = "koko.txt"
    os.system("gmx analyze -f %s -b %d > %s 2>&1" % ( infile, begin, ptxt ))
    aver = []
    with open(ptxt, "r") as inf:
        for line in inf:
            if line.find("SS") >= 0:
                words = line.split()
                if len(words) >= 2:
                    try:
                        aver.append(float(words[1]))
                    except ValueError:
                        print("Invalid line '%s'" % line)
                else:
                    print("No words on line '%'" % line)
    return aver

def analyse_solid(outf, moldb):
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            soliddens = "solid_density"
            sdens = 0
            if soliddens in moldb[compound]:
                sdens = moldb[compound][soliddens]
            outf.write("%s %s %s solid density %g\n" % ( compound, phase, top, sdens ))
            outf.write("%-10s  %10s  %10s  %10s\n" % ( "Temperature", "P(NVT)", "Rho(NPT)", "Epot(NPT)" ) )
            for temp in glob.glob("*"):
                if os.path.isdir(str(temp)):
                    os.chdir(str(temp))
                    outf.write("%-10s" % temp)
                    if os.path.exists("NVT.gro"):
                        pnvt = "pressure-nvt.xvg"
                        if not os.path.exists(pnvt):
                            os.system("echo Pressure | gmx energy -f NVT -o %s" % pnvt)
                        aver = get_averages(pnvt, 500)
                        if len(aver) > 0:
                            outf.write("  %10g" % aver[0])
                                
                    if os.path.exists("NPT.gro"):
                        rhonpt = "density-npt.xvg"
                        if not os.path.exists(rhonpt):
                            os.system("echo Density | gmx energy -f NPT -o %s" % rhonpt)
                        aver = get_averages(rhonpt, 3000)
                        if len(aver) > 0:
                            outf.write("  %10g" % aver[0])
                        epotnpt = "epot-npt.xvg"
                        if not os.path.exists(epotnpt):
                            os.system("echo Potential | gmx energy -f NPT -o %s -nmol %d" % ( epotnpt, moldb[compound]["nsolid"]) )
                        aver = get_averages(epotnpt, 3000)
                        if len(aver) > 0:
                            outf.write("  %10g" % aver[0])
                    outf.write("\n")
                    os.chdir("..")
            os.chdir("..")

def analyse_gas(outf, moldb):
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            outf.write("%s %s %s\n" % ( compound, phase, top ))
            outf.write("%-10s  %10s\n" % ( "Temperature", "Epot(NVT)" ) )
            for temp in glob.glob("*"):
                if os.path.isdir(str(temp)):
                    os.chdir(str(temp))
                    outf.write("%-10s" % temp)
                    if os.path.exists("NVT.gro"):
                        epotnvt = "epot-nvt.xvg"
                        if not os.path.exists(epotnvt):
                            os.system("echo Potential | gmx energy -f NVT -o %s" % ( epotnvt ) )
                        aver = get_averages(epotnvt, 10000)
                        if len(aver) > 0:
                            outf.write("  %10g" % aver[0])
                                
                    outf.write("\n")
                    os.chdir("..")
            os.chdir("..")

if shutil.which("gmx") == None:
    sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")
moldb  = get_moldb(False)
moldb  = input_dens(moldb)    

output = "results.txt"
outf   = open(output, "w")

for top in [ "bcc", "resp" ]:
    print("Looking for %s" % top)
    if os.path.isdir(top):
        os.chdir(top)
        for phase in [ "solid", "gas" ]:
            if os.path.isdir(phase):
                os.chdir(phase)
                if "solid" == phase:
                    analyse_solid(outf, moldb)
                else:
                    analyse_gas(outf, moldb)
                os.chdir("..")
        os.chdir("..")

outf.close()
