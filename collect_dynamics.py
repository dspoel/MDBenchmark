#!/usr/bin/env python3

import os, glob
from molecule_db import *
from analyse import get_tail

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0

not_converged = {
    "ethane": [ 55, 60, 65, 70, 75, 80 ],
    "pentane": [ 98, 113, 118, 123, 128, 133,  148, 153, 158, 163, 168, 173, 178, 183, 188 ],
    "propane": [ 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105 ],
    # 204 and 209 are polycrystalline
    "cyclohexane": [ 129, 204, 209 ],
    "benzene": [ 128 ],
    "imidazole": [ 213, 283, 293, 303, 313, 323, 333 ],
    # 161 i spolycrystalline
    "methanol": [ 126, 131, 136, 141, 146, 151, 156, 166, 176, 186, 196, 206 ],
    # No ethanol crystal that converged to the crystal state. 
    # First one that is not omitted is liquid.
    # 184 may still be on its way to the liquid state
    "ethanol": [ 109, 114, 119, 124, 129, 134, 139, 144, 149, 154, 159, 164, 169, 174, 179 ],
    # No real crystal for this compound either.  First one that is not omitted is liquid.
    "ethyleneglycol": [ 160, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, ],
    "formic_acid" : [ 216, 221, 226, 231, 236, 241, 246, 256, 266, 276 ],
    # No real crystal here either. First one that is not omitted is liquid.
    "phenol": [ 239, 244, 254, 259, 264, 269, 274, 279, 284, 289, 299, 314, 324 ],
    "12-benzenediol": [ 327, 332, 337, 342, 347, 352, 357, 417, 427 ],
    "123-benzenetriol": [ 353, 358, 363, 368, 373, 378, 383, 393, 403 ],
    "12-ethanediamine": [ 269, 279, 289, 299, 309 ],
    "pyridine": [ 181, 186, 191, 196, 201, 206, 211, 216, 221, 226, 236, 241 ],
    "menh2": [ 139, 144, 149, 154, 159, 164, 169, 174 ],
    "acooh": [ 189, 229, 249, 269 ],
    "octanoic_acid": [ 284, 294, 304, 314 ],
    "succinic_acid": [ 424, 464, 504 ],
    "acetamide": [ 104, 154, 204, 284, 294  ],
    "formamide": [],
    "urea": [ 436  ]
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
        if m in ftemp and m in rtemp and (not compound in not_converged or not int(m) in not_converged[compound]): 
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
    for mol in moldb:
        if os.path.isdir(mol):
            os.chdir(mol)
            alltemp = get_temps(mol)
            do_msd(alltemp)
            do_rotacf(alltemp)
            do_filesize(alltemp)
            os.chdir("..")
        else:
            sys.exit("No mol %s in %s" % ( mol, os.getcwd() ) )
