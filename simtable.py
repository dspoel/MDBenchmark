#!/usr/bin/env python3

import os, glob, argparse
from molecule_db import *
from get_csv_rows import *

def get_simtable(filename:str) -> dict:
    if not os.path.exists(filename):
        return None
    simtable = {}
    for row in get_csv_rows(filename, 12):
        if not row[0] in simtable:
            simtable[row[0]] = {}
        temp   = int(row[1])
        length = float(row[2])
        if not temp in simtable[row[0]] or length > simtable[row[0]][temp]["length"]:
            simtable[row[0]][temp] = { "host": row[3], "length": length, "nmol": int(row[4]),
                                       "simdir": row[5], "logfile": row[6], "cptfile": row[7],
                                       "tprfile": row[8], "trrfile": row[9], "edrfile": row[10],
                                       "trrtime": float(row[11]) }
    return simtable

def dump_simtable(simtable:dict, filename:str):
    with open(filename, "w") as outf:
        outf.write("\\begin{longtable}{lcp{12cm}}\n")
        outf.write("\\caption{Overview of melting simulations performed. Number of molecules in the system, temperature (K) and simulation length (ns).}\n")
        outf.write("\\label{meltsims}\\\\\n")
        outf.write("Compound & \# Mol & Temperature (Simulation length) \\\\\n")
        outf.write("\\hline\n")
        for mol in sorted(simtable.keys()):
            printStart = False
            for temp in sorted(simtable[mol].keys()):
                if not printStart:
                    outf.write("%s & %d &" % ( mol, simtable[mol][temp]["nmol"] ) )
                    printStart = True
                outf.write(" %d(%.0f)" % ( temp, simtable[mol][temp]["length"] ) )
            outf.write("\\\\\n")
        outf.write("\\hline\n")
        outf.write("\\end{longtable}\n")

def get_last_time(logfile:str) -> float:
    with open(logfile) as inf:
        lines  = inf.readlines()
        nlines = len(lines)
        for line in range(nlines-1, 0, -1):
            if lines[line].find("    Step           Time") >= 0 and line < nlines-1:
                words = lines[line+1].strip().split()
                try:
                    return float(words[1])
                except:
                    print("Cannot find final MD time for %s" % logfile)
                    return 0.0
    return 0.0

def get_dict_entry(mol:str):
    newest_trr  = ""
    newest_gro  = ""
    newest_time = None
    for trr in glob.glob("melting*trr"):
        mytime = os.path.getmtime(trr)
        if None == newest_time or mytime > newest_time:
            newest_time = mytime
            newest_trr  = trr
            mygro = trr[:-3] + "gro"
            if os.path.exists(mygro):
                newest_gro = mygro
            else:
                newset_gro = ""
    if None != newest_time:
        simdir = os.getcwd()
        # Extract the temperature from the dir name
        ptr = simdir.rfind(mol)
        try:
            if ptr >= 0:
                temp = float(simdir[ptr+len(mol):])
            else:
                temp = float(simdir)
        except ValueError:
            print("Cannot extract temperature from %s" % simdir)
            temp = 0.0
        
        logfile = newest_trr[:-3] + "log"
        tprfile = newest_trr[:-3] + "tpr"
        edrfile = newest_trr[:-3] + "edr"
        cptfile = newest_trr[:-3] + "cpt"
        if (os.path.exists(logfile) and os.path.exists(tprfile) and
            os.path.exists(edrfile) and os.path.exists(cptfile)):
            newdict = { "simdir":  simdir,
                        "logfile": logfile,
                        "cptfile": cptfile,
                        "tprfile": tprfile,
                        "trrfile": newest_trr,
                        "edrfile": edrfile,
                        "endtime": get_last_time(logfile),
                        "trrtime": newest_time }
            return newdict, temp
    return None, 0.0

def get_run_dict(topdir: str, molnames:list):
    if not os.path.exists(topdir):
        sys.exit("No such dir %s" % topdir)
    pwd = os.getcwd()
    os.chdir(topdir)
    lisa_name = { "acooh": "acoh", "12-ethanediamine": "ethylendiamine", "ethyleneglycol": "ethylenglycol", "ethylene": "ethene" }
    mydict = {}
    for molname in molnames:
        mol = molname
        if mol in lisa_name:
            mol = lisa_name[mol]
        if os.path.exists(mol):
            os.chdir(mol)
            mydict[mol] = {}
            simdirs = glob.glob("*%s*" % mol) + glob.glob("[1-9]*")
            print(simdirs)
            for simdir in simdirs:
                if os.path.isdir(simdir):
                    os.chdir(simdir)
                    newdict, temp = get_dict_entry(mol)
                    if None != newdict:
                        mydict[mol][temp] = newdict
                    os.chdir("..")
            os.chdir("..")
    os.chdir(pwd)
    return mydict

def get_natom(gro:str) -> int:
    try:
        with open(gro, "r") as inf:
            fff   = inf.readlines()
            return int(fff[1].strip())
    except:
        return 0

def get_nmol(mol:str, natom:int) -> int:
    finals = glob.glob("final*gro")
    ncryst = get_natom(finals[0])
    if (natom > 0):
        return ncryst/natom
    else:
        return 0

def parseArguments():
    parser = argparse.ArgumentParser(
      prog='simtable.py',
      description=
"""
Script to tabulate all melting simulations performed. Can take a long
time, so please run in the background.
""")
    mtname = "melt_table.csv" 
    parser.add_argument("-gen", "--generate", help="Generate the table", action="store_true")
    parser.add_argument("-out", "--output", help="Filename to write to, default "+mtname, type=str, default=mtname)
    parser.add_argument("-in", "--input", help="Filename to read a table from", type=str, default=None)
    parser.add_argument("-dump", "--dump", help="Dump the contents of the table to a latex file", type=str, default=None)
    return parser.parse_args()

if __name__ == '__main__':
    moldb = get_moldb(False)
    args  = parseArguments()
    
    if args.generate:
        with open(args.output, "w") as csv:
            os.chdir("bcc/melt")
            topdirs = { "keb2": "/proj/nobackup/alexandria/spoel/MDBenchmark/melting",
                        "keb": "/proj/nobackup/alexandria/lisa/melting",
                        "csb": "/home/lschmidt/MELTING"  }
            for host in topdirs.keys():
                if os.path.isdir(topdirs[host]):
                    mydict = get_run_dict(topdirs[host], moldb.keys())
                    print(mydict.keys())
                    for mol in mydict:
                        if os.path.isdir(mol):
                            os.chdir(mol)
                            nmol = get_nmol(mol, moldb[mol]["natom"])
                            for temp in sorted(mydict[mol].keys()):
                                mytime = mydict[mol][temp]["endtime"]/1000.0
                                if mytime >= 2:
                                    csv.write("%s|%g|%g|%s|%d|%s|%s|%s|%s|%s|%s|%s\n" % 
                                              ( mol, temp, mytime, host, nmol,
                                                mydict[mol][temp]["simdir"],
                                                mydict[mol][temp]["logfile"],
                                                mydict[mol][temp]["cptfile"],
                                                mydict[mol][temp]["tprfile"],
                                                mydict[mol][temp]["trrfile"],
                                                mydict[mol][temp]["edrfile"],
                                                str(mydict[mol][temp]["trrtime"]) ) ) 
                            os.chdir("..")
            os.chdir("../..")
    if None != args.dump and None != args.input:
        simtable = get_simtable(args.input)
        if None == simtable:
            sys.exit("No such file %s" % args.input)
        dump_simtable(simtable, args.dump)
