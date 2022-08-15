#!/usr/bin/env python3

import os, glob
from molecule_db import *
from analyse import get_tail

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0

ignore = {
    "ethane": [ 55, 60, 65, 70, 75, 80 ],
    "pentane": [ 98, 113, 118, 123, 128, 133, 138 ],
    # 204 and 209 are polycrystalline
    "cyclohexane": [ 129, 184, 204, 209 ],
    "benzene": [ 128, 178 ],
    "imidazole": [ 263, 268 ],
    # 161 i spolycrystalline
    "methanol": [ 151, 156, 161 ],
    # No ethanol crystal that converged to the crystal state. 
    # First one that is not omitted is liquid.
    # 184 may still be on its way to the liquid state
    "ethanol": [ 109, 114, 119, 124, 129, 134, 139, 144, 149, 154, 159, 164, 169, 174,  179, 184 ],
    # No real crystal for this compound either.  First one that is not omitted is liquid.
    "ethyleneglycol": [ 160, 190, 195, 200, 205, 210, 215, 220, 225, 230 ],
    # No real crystal here either. First one that is not omitted is liquid.
    "phenol": [ 244, 254, 259, 264, 269, 274 ],
    "12-benzenediol": [ 327, 332, 
                        337, 342, 347, 352, 357, 377, 382, 387, 392
                        , 397
    ]
}

def get_temps(compound:str):
    mtemp = {}
    for msd in glob.glob("msd_*xvg"):
        mtemp[msd[4:-4]] = 1
    ftemp = {}
    for fs in glob.glob("final_*.gro"):
        ftemp[fs[6:-4]] = 1
    rtemp = {}
    for rot in glob.glob("rotacf_*.xvg"):
        rtemp[rot[7:-4]] = 1
    alltemp = []
    for m in mtemp:
        if m in ftemp and m in rtemp: # and (not compound in ignore or not int(m) in ignore[compound]): 
            alltemp.append(m)
    return alltemp

def do_msd(alltemp:list):
    td  = {}
    for temp in alltemp:
        msd = ("msd_%s.xvg" % temp )
        with open(msd, "r") as inf:
            for line in inf:
                if line.find("System") >= 0 and line.find("D") >= 0:
                    words = line.strip().split()
                    try:
                        ddd   = float(words[4])
                        err   = float(words[6][:-1])
                        td[float(temp)] = [ ddd, err ]
                    except ValueError:
                        print("Incomprehensible line '%s'" % line)
    with open("temp_diff.xvg", "w") as outf:
        outf.write("@ xaxis label \"T (K)\"\n")
        for temp in sorted(td.keys()):
            outf.write("%10g  %10g\n" % ( temp, td[temp][0] ) )

def do_filesize(alltemp:list):
    fsize    = {}
    min_size = 10000000
    max_size = 0
    for temp in alltemp:
        my_gro = ("final_%s.gro" % temp )
        koko = "koko.gz"
        os.system("gzip -c %s > %s" % ( my_gro, koko ))
        my_size = os.path.getsize(koko)
        fsize[float(temp)] = my_size
        os.unlink(koko)
        max_size = max(max_size, my_size)
        min_size = min(min_size, my_size)
    
    with open("temp_filesize.xvg", "w") as outf:
        outf.write("@ xaxis label \"T (K)\"\n")
        for temp in sorted(fsize.keys()):
            this_size = 0.5+(0.5*(fsize[temp]-min_size))/(max_size-min_size)
            outf.write("%10g  %10g\n" % ( temp, this_size ) )

def do_rotacf(alltemp:list):
    S0 = {}
    for temp in alltemp:
        my_files = [ ("rotacf_%s.xvg" % temp ), ("rotplane_%s.xvg" % temp ) ]
        myS0 = get_tail(my_files, 50)
        if None != myS0:
            S0[float(temp)] = myS0 
    
    with open("temp_S0.xvg", "w") as outf:
        outf.write("@ xaxis label \"T (K)\"\n")
        for temp in sorted(S0.keys()):
            outf.write("%10g  %10g\n" % ( temp, S0[temp] ) )

if __name__ == '__main__':
    moldb = get_moldb(False)
    os.chdir("bcc/melt")
    lisa_csb  = [ "ethane", "ethyne", "formamide", "formaldehyde", "urea", "ethylene" ]
    if not csb:
        for mol in moldb:
            if os.path.isdir(mol) and mol not in lisa_csb:
                os.chdir(mol)
                alltemp = get_temps(mol)
                do_msd(alltemp)
                do_rotacf(alltemp)
                do_filesize(alltemp)
                os.chdir("..")
    else:
        for mol in lisa_csb:
            if os.path.isdir(mol):
                os.chdir(mol)
                alltemp = get_temps(mol)
                do_msd(alltemp)
                do_rotacf(alltemp)
                do_filesize(alltemp)
                os.chdir("..")
