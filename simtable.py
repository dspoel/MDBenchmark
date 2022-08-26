#!/usr/bin/env python3

import os, glob, argparse
from molecule_db import *
from get_csv_rows import *

lisa_name = { "acooh": "acoh", "12-ethanediamine": "ethylendiamine", "ethyleneglycol": "ethylenglycol", "ethylene": "ethene" }

Debug = False

def get_simtable(filenames:list) -> dict:
    simtable = {}
    for filename in filenames:
        if os.path.exists(filename):
            for row in get_csv_rows(filename, 13):
                if not row[0] in simtable:
                    simtable[row[0]] = {}
                temp   = int(row[1])
                length = float(row[2])
                if (not temp in simtable[row[0]] or length > simtable[row[0]][temp]["length"] or 
                    (length == simtable[row[0]][temp]["length"] and (row[3].find("keb") >= 0) or (row[3].find("csb2") >= 0))):
                    simtable[row[0]][temp] = { "host": row[3], "length": length, "nmol": int(row[4]),
                                               "simdir": row[5], "logfile": row[6], "cptfile": row[7],
                                               "tprfile": row[8], "trrfile": row[9], "edrfile": row[10],
                                               "grofile": row[11], "trrtime": float(row[12]) }
    return simtable

def dump_simtable(simtable:dict, filename:str):
    replace_names = { "acooh": "acetic acid", "menh2": "methylamine",
                      "12-benzenediol": "benzene-1,2-diol",
                      "12-ethanediamine": "ethanediamine",
                      "123-benzenetriol": "benzene-1,2,3-triol",
                      "14-benzoquinone": "1,4-benzoquinone" }
    with open(filename, "w") as outf:
        outf.write("\\begin{longtable}{lcp{12cm}}\n")
        outf.write("\\caption{Overview of melting simulations performed. Number of molecules in the system, simulation temperatures (K).}\n")
        outf.write("\\label{meltsims}\\\\\n")
        outf.write("Compound & \# Mol & Temperature\\\\\n")
        outf.write("\\hline\n")
        for mol in sorted(simtable.keys()):
            printStart = False
            printmol = mol.replace("_", " ")
            if printmol in replace_names:
                printmol = replace_names[printmol]
            for temp in sorted(simtable[mol].keys()):
                if not printStart:
                    outf.write("%s & %d &" % ( printmol, simtable[mol][temp]["nmol"] ) )
                    printStart = True
                outf.write(" %d" % ( temp ) )
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
    if Debug:
        print("Looking for %s in %s" % ( mol, os.getcwd() ) )
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
                mygro = "NPT2.gro"
                if os.path.exists(mygro):
                    newest_gro = mygro
                else:
                    newest_gro = ""
    if None != newest_time:
        simdir = os.getcwd()
        # Extract the temperature from the dir name
        findTemp = True
        try:
            stemp = simdir[simdir.rfind("/")+1:]
            if Debug:
                print("Looking for temperature in %s" % stemp)
            temp = float(stemp)
        except ValueError:
            ptr = simdir.rfind(mol)
            try:
                if ptr >= 0:
                    temp = float(simdir[ptr+len(mol):])
                else:
                    findTemp = False
            except ValueError:
                findTemp = False
        if not findTemp:
            print("Cannot extract temperature from %s" % simdir)
            temp = 0.0
        else:
            if Debug:
                print("Found temp %g for %s in %s" % ( temp, mol, simdir ) )
        logfile = newest_trr[:-3] + "log"
        tprfile = newest_trr[:-3] + "tpr"
        edrfile = newest_trr[:-3] + "edr"
        if (os.path.exists(logfile) and os.path.exists(tprfile) and
            os.path.exists(edrfile)):
            cptfile = newest_trr[:-3] + "cpt"
            if not os.path.exists(cptfile):
                cptfile = ""
            newdict = { "simdir":  simdir,
                        "logfile": logfile,
                        "cptfile": cptfile,
                        "tprfile": tprfile,
                        "trrfile": newest_trr,
                        "grofile": newest_gro,
                        "edrfile": edrfile,
                        "endtime": get_last_time(logfile),
                        "trrtime": newest_time }
            return newdict, temp
        else:
            if Debug:
                print("Could not find all files in %s" % simdir)
    else:
        if Debug:
            print("Could not find a simulation.")
    return None, 0.0

def get_run_dict(topdir: str, molnames:list, useLisaName:bool):
    if not os.path.exists(topdir):
        sys.exit("No such dir %s" % topdir)
    pwd = os.getcwd()
    os.chdir(topdir)
    mydict = {}
    for molname in molnames:
        moldir = molname
        if useLisaName and moldir in lisa_name:
            moldir = lisa_name[moldir]
        if os.path.exists(moldir):
            os.chdir(moldir)
            mydict[molname] = {}
            simdirs = glob.glob("*%s*" % moldir) + glob.glob("[1-9]*")
            if Debug:
                print(simdirs)
            for simdir in simdirs:
                if os.path.isdir(simdir):
                    os.chdir(simdir)
                    newdict, temp = get_dict_entry(moldir)
                    if None != newdict:
                        if Debug:
                            print(newdict)
                        if not temp in mydict[molname] or (newdict["trrtime"] > mydict[molname][temp]["trrtime"]):
                            mydict[molname][temp] = newdict
                    else:
                        if Debug:
                            print("Failed to find dictionary entry")
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
    parser.add_argument("-in", "--input", nargs="+", help="Filename(s) to read a table from", type=str, default=None)
    parser.add_argument("-dump", "--dump", help="Dump the contents of the table to a latex file", type=str, default=None)
    parser.add_argument("-v", "--verbose", help="Print debugging info", action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    moldb = get_moldb(False)
    args  = parseArguments()
    if args.verbose:
        Debug = True
        
    if args.generate:
        with open(args.output, "w") as csv:
            os.chdir("bcc/melt")
            topdirs = { "keb2": "/proj/nobackup/alexandria/spoel/MDBenchmark/melting",
                        "keb": "/proj/nobackup/alexandria/lisa/melting",
                        "csb": "/home/lschmidt/MELTING",
                        "csb2": "/home/spoel/wd/MDBenchmark/melting" }
            for host in topdirs.keys():
                if os.path.isdir(topdirs[host]):
                    mydict = get_run_dict(topdirs[host], moldb.keys(), host.find("2") < 0)
                    print(mydict.keys())
                    for molname in mydict:
                        moldir = molname
                        if os.path.isdir(moldir):
                            os.chdir(moldir)
                            nmol = get_nmol(molname, moldb[molname]["natom"])
                            for temp in sorted(mydict[molname].keys()):
                                mytime = mydict[molname][temp]["endtime"]
                                if mytime >= 100:
                                    csv.write("%s|%g|%g|%s|%d|%s|%s|%s|%s|%s|%s|%s|%s\n" % 
                                              ( molname, temp, mytime, host, nmol,
                                                mydict[molname][temp]["simdir"],
                                                mydict[molname][temp]["logfile"],
                                                mydict[molname][temp]["cptfile"],
                                                mydict[molname][temp]["tprfile"],
                                                mydict[molname][temp]["trrfile"],
                                                mydict[molname][temp]["edrfile"],
                                                mydict[molname][temp]["grofile"],
                                                str(mydict[molname][temp]["trrtime"]) ) ) 
                            os.chdir("..")
                        else:
                            if Debug:
                                print("Cannot find director %s, am here: %s" % ( moldir, os.getcwd() ) )
            os.chdir("../..")
    if None != args.dump and None != args.input:
        simtable = get_simtable(args.input)
        if None == simtable:
            sys.exit("No such file %s" % args.input)
        dump_simtable(simtable, args.dump)
