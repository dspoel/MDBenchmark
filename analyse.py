#!/usr/bin/env python3

import os, shutil, glob, sys, math
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

def get_averages(infile:str, begin:int, end: int) -> list:
    ptxt = "koko.txt"
    os.system("gmx analyze -f %s -b %d -e %d > %s 2>&1" % ( infile, begin, end, ptxt ))
    myaver  = None
    myerror = None
    with open(ptxt, "r") as inf:
        for line in inf:
            if line.find("SS1") >= 0:
                words = line.split()
                if len(words) >= 2:
                    try:
                        myaver = float(words[1])
                        myerror = float(words[2])
                    except ValueError:
                        print("Invalid line '%s'" % line)
                else:
                    print("No words on line '%'" % line)
            elif False and line.find("err.est") >= 0:
                words = line.split()
                if len(words) >= 4:
                    try:
                        myerror = float(words[3])
                    except ValueError:
                        print("Invalid line '%s'" % line)
    return myaver, myerror

def grogzsize(grofile):
    gzfile = grofile+".gz"
    os.system("gzip %s" % grofile)
    gzsize = os.path.getsize(gzfile)
    os.system("gunzip %s" % gzfile)
    return gzsize

def analyse_solid(outf, moldb):
    solids = {}
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            soliddens = "solid_density"
            sdens = 0
            if soliddens in moldb[compound]:
                sdens = moldb[compound][soliddens]
            mysolid = {}
            outf.write("%s %s %s solid density %g\n" % ( compound, phase, top, sdens ))
            outf.write("%-10s  %10s  %10s  %10s\n" % ( "Temperature", "P(NVT)", "Rho(NPT)", "Epot(NPT)" ) )
            mytemps = []
            for temp in glob.glob("*"):
                if os.path.isdir(str(temp)):
                    try:
                        mytemps.append(int(temp))
                    except ValueError:
                        print("%s is not a directory with an integer name" % temp)
            print(mytemps)
            for mytemp in sorted(mytemps):
                temp = str(mytemp)
                if os.path.isdir(str(temp)):
                    os.chdir(str(temp))
                    mysolid[str(temp)] = {}
                    outf.write("%-10s" % temp)
                    if os.path.exists("NVT.gro"):
                        pnvt = "pressure-nvt.xvg"
                        if not os.path.exists(pnvt):
                            os.system("echo Pressure | gmx energy -f NVT.edr -o %s" % pnvt)
                        aver,error = get_averages(pnvt, 500, 1000)
                        if None != aver and None != error:
                            mysolid[str(temp)]["pnvt"] = [ aver, error ]
                            outf.write("  %10g (%g)" % ( aver, error))

                    final_gro = "NPT2.gro"                
                    if os.path.exists(final_gro):
                        tbegin = 10000
                        tend   = 15000
                        rhonpt = "density-npt.xvg"
                        if not os.path.exists(rhonpt):
                            os.system("echo Density | gmx energy -f NPT.edr -o %s" % rhonpt)
                        aver, error = get_averages(rhonpt, tbegin, tend)
                        if None != aver and None != error:
                            mysolid[str(temp)]["rhonpt"] = [ aver, error ]
                            outf.write("  %10g (%g)" % ( aver, error ))
                        epotnpt = "epot-npt.xvg"
                        if not os.path.exists(epotnpt):
                            os.system("echo Potential | gmx energy -f NPT.edr -o %s -nmol %d" % ( epotnpt, moldb[compound]["nsolid"]) )
                        aver, error = get_averages(epotnpt, tbegin, tend)
                        if None != aver and None != error:
                            mysolid[str(temp)]["epotnpt"] = [ aver, error ]
                            outf.write("  %10g (%10g)" % ( aver, error ))
                        gzsize = grogzsize(final_gro)
                        mysolid[str(temp)]["gzsize"] = [ gzsize ]
                        outf.write(" %10d" % gzsize)
                    outf.write("\n")
                    os.chdir("..")
            os.chdir("..")
            solids[compound] = mysolid
    return solids

def analyse_gas(outf, moldb):
    gas = {}
    for compound in moldb.keys():
        print("Looking for %s" % compound)
        if os.path.isdir(compound):
            os.chdir(compound)
            mygas = {}
            outf.write("%s %s %s\n" % ( compound, phase, top ))
            outf.write("%-10s  %10s\n" % ( "Temperature", "Epot(NVT)" ) )
            for temp in glob.glob("*"):
                if os.path.isdir(str(temp)):
                    os.chdir(str(temp))
                    mygas[str(temp)] = {}
                    outf.write("%-10s" % temp)
                    final_gro = "NVT.gro"
                    if os.path.exists(final_gro):
                        epotnvt = "epot-nvt.xvg"
                        if not os.path.exists(epotnvt):
                            os.system("echo Potential | gmx energy -f NVT.edr -o %s" % ( epotnvt ) )
                        aver, error = get_averages(epotnvt, 10000, 15000)
                        if None != aver and None != error:
                            mygas[str(temp)]["epotgas"] = [ aver, error ]
                            outf.write("  %10g (%g)" % (aver, error))
                                
                    outf.write("\n")
                    os.chdir("..")
            os.chdir("..")
            gas[compound] = mygas
    return gas

if shutil.which("gmx") == None:
    sys.exit("Please load the gromacs environment using\nml load GCC/10.2.0  OpenMPI/4.0.5 GROMACS/2021")
moldb  = get_moldb(False)
moldb  = input_dens(moldb)    

output = "results.txt"
outf   = open(output, "w")

allresults = {}

for top in [ "bcc", "resp" ]:
    print("Looking for %s" % top)
    if os.path.isdir(top):
        os.chdir(top)
        allresults[top] = {}
        for phase in [ "solid", "gas" ]:
            if os.path.isdir(phase):
                os.chdir(phase)
                if "solid" == phase:
                    allresults[top][phase] = analyse_solid(outf, moldb)
                else:
                    allresults[top][phase] = analyse_gas(outf, moldb)
                os.chdir("..")
        os.chdir("..")

outf.close()

def get_str(allresults, top:str, phase:str, compound:str, myT:str, prop:str, expectError:bool):
    if myT in allresults[top][phase][compound]:
        if prop in allresults[top][phase][compound][myT]:
            allres = allresults[top][phase][compound][myT][prop]
            if len(allres) == 2:
                return ("%g,%g" % ( allres[0], allres[1] ))
            elif len(allres) == 1:
                return ("%d" % ( allres[0] ))
    if expectError:
        return ","
    else:
        return ""

solid = "solid"
gas   = "gas"
with open("allresults.csv", "w") as csvf:
    csvf.write(",,bcc,,,,,,,,,,,resp,,,,,,,,,,\n")
    csvf.write("Compound,Temperature,P(NVT),sigmaP,Rho(NPT),sigmaRho,Epot(NPT),sigmaE,Epot(gas),sigmaE,DHsub,sigmaH,gzip_size,P(NVT),sigmaP,Rho(NPT),sigmaRho,Epot(NPT),sigmaE,Epot(gas),sigmaE,DHsub,sigmaH,gzip_size\n")
    for compound in moldb.keys():
        alltemps = []
        # Fetch all the temperatures from all compounds
        for top in [ "bcc", "resp" ]:
            for phase in [ solid, gas ]:
                for myt in allresults[top][phase][compound].keys():
                    if not int(myt) in alltemps and not myt == "0":
                        alltemps.append(int(myt))
        # Now loop over them and print what data we have
        Boltz = 0.00831415
        for myT in sorted(alltemps):
            csvf.write("%s,%d" % ( compound, myT ))
            for top in [ "bcc", "resp" ]:
                myTstr  = str(myT)
                epotnpt = get_str(allresults, top, solid, compound, myTstr, "epotnpt", True)
                epotgas = get_str(allresults, top, gas, compound, myTstr, "epotgas", True)
                dhsub   = ","
                try:
                    epn     = epotnpt.split(",")
                    epg     = epotgas.split(",")
                    epsolid = float(epn[0])
                    epgas   = float(epg[0])
                    errsub  = math.sqrt(float(epn[1])**2 + float(epg[1])**2)
                    dhsub   = ("%g,%g" % ( epgas-epsolid-2*myT*Boltz, errsub ))
                except ValueError:
                    # do nothing
                    print("Missing value")
                
                csvf.write(",%s,%s,%s,%s,%s,%s" % ( get_str(allresults, top, solid, compound, myTstr, "pnvt", True),
                                                    get_str(allresults, top, solid, compound, myTstr, "rhonpt", True),
                                                    epotnpt, epotgas, dhsub, 
                                                    get_str(allresults, top, solid, compound, myTstr, "gzsize", False)) )
            csvf.write("\n")

