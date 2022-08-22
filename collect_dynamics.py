#!/usr/bin/env python3

import os, glob, sys
from molecule_db import *
from analyse import get_tail

csb = "HOST" in os.environ and os.environ["HOST"].find("csb") >= 0

sim_status = {
    # Fig. S4
    "ethane": { "failed": [  ], 
                "running": [  ], 
                "success": [ 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150 ] },
    "propane": { "failed": [ 35, 40, 45, 50, 60, 65, 75, 85, 95, 105, 55, 70, 80, 90, 100 ],
                 "running": [  ],
                 "success": [ 110, 115, 120, 125, 130, 135 ] },
    # 90 K is polycrystalline
    "cyclopropane": { "failed": [ 25 ],
                      "running": [ ],
                      "success": [ 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145,
                                   150, 155, 160, 165, 170, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225 ] },
    "pentane": { "failed": [ 93, 98, 103, 108, 113, 118, 123, 128, 133, 138, 153, 163, 168, 173,  183 ],
                 "running": [   ],
                 "success": [ 148, 158, 178, 188 ] },
    # 204 and 209 are polycrystalline
    "cyclohexane": { "failed": [29, 79, 129, 194, 199, 204, 209, 214, 219, 224, 229, 234  ],
                     "running": [  ],
                     "success": [ 179, 184, 189 ] },
    "ethylene": { "failed": [],
                  "running": [],
                  "success": [ 59, 64, 69, 74, 79, 84, 89, 94, 104, 109, 114, 119, 124, 129, 134, 139, 144, 149 ]},
    # Fig. S5
    "ethyne": { "failed": [ ],
                "running": [ ],
                "success": [ 142, 147, 152, 157, 162, 167, 172, 177, 182, 187, 192, 197, 202,
                             207, 212, 217, 222, 227, 232, 237, 242 ] },
    "14-benzoquinone": { "failed": [ 338, 343, 348, 353, 358, 363, 373 ],
                         "running": [  ],
                         "success": [ 368, 378, 383, 393, 398, 403, 408, 413, 418, 423, 428, 433, 438 ] },
    "benzene": { "failed": [ 128 ], 
                 "running": [  ],
                 "success": [ 178, 203, 208, 213, 218, 223, 228, 233, 238, 243, 248, 253, 258, 263, 268, 273,
                              283, 288, 293, 298, 303, 308, 313, 318, 323, 328 ] },
    "naphthalene": { "failed": [ 318, 323, 328 ], 
                     "running": [ ],
                     "success": [ 303, 308, 313, 333, 338, 343, 348, 353, 358, 363, 368, 373, 383, 388, 393, 398, 403 ] },
    "furan": { "failed": [ 7, 12, 37, 87, 112, 117 ],
               "running": [ ],
               "success": [ 122, 132, 127, 137, 142, 147, 152, 157, 162, 167, 172, 177, 182, 192, 
                            197, 202, 207, 212, 217, 222, 227,232, 237 ] },
    # 263 K is polycrystalline
    "imidazole": { "failed": [ 113, 163, 213, 268, 273, 278, 283, 288, 293, 313, 323, 333 ],
                   "running": [  ],
                   "success": [ 263, 298, 308, 318, 328, 338, 343, 348, 353, 358, 363, 368, 373, 378, 383, 388, 393, 398, 403, 408, 413 ] },
    # Fig. S6
    # 161 is polycrystalline. T = 191 an 201 K have extensive box deformation that can explain
    # the large file size.
    "methanol": { "failed": [ 126, 131, 136, 141, 146, 151, 156, 166, 176, 186, 196, 206 ], 
                  "running": [  ],
                  "success": [ 161, 171, 181, 191, 201, 211, 216 ] },
    # No ethanol crystal that converged to the crystal state. 
    # First one that is not omitted is liquid.
    # 184 may still be on its way to the liquid state
    "ethanol": { "failed": [ 109, 114, 119, 124, 129, 134, 139, 144, 149, 154, 159, 164, 169, 174, 179, 184  ],
                 "running": [   ],
                 "success": [ 189, 194, 199, 204, 209] },
    
    "ethyleneglycol": { "failed": [ 160, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260 ],
                        "running": [  ],
                        "success": [ 265, 270, 275, 280, 285, 290, 295, 300, 305, 310 ] },
    "phenol": { "failed": [ 239, 244, 254, 259, 264, 269, 274 ],
                "running": [  ],
                "success": [ 279, 284, 289, 294, 299, 304, 309, 319, 324, 329, 334, 339, 344, 349, 354, 359, 364 ] },
    "12-benzenediol": { "failed": [ 327, 332, 337, 342, 347, 352, 357, 382, 392, 417, 427],
                        "running": [  ],
                        "success": [ 372, 377, 387, 397, 402, 407, 412, 422] },
    "123-benzenetriol": { "failed": [ 353, 358, 363, 368, 378, 373, 383, 388, 393, 398  ],
                          "running": [   ],
                          "success": [ 408, 413, 418, 423, 428, 433, 438, 443, 448, 453 ] },
    # meh2 at 429K most likely gas phase
    "menh2": { "failed": [ 134, 139, 144, 149, 154, 159, 164, 169, 174, 184, 189, 194, 199, 204, 229, 239, 244],
               "running": [  ],
               "success": [ 209, 214, 219, 224, 234, 249, 254, 259, 264, 279, 329, 379, 429 ] },
    "12-ethanediamine": { "failed": [ 34, 84, 134, 154, 179, 184, 214, 219, 224, 229, 234, 239, 244, 249, 254, 274, 294, 299, 304, 309 ],
                          "running": [  ],
                          "success": [ 259, 264, 269, 279, 289, 314, 319, 324, 329, 334 ] },
    "formic_acid" : { "failed": [ 216, 221, 271,  226, 231, 236, 241, 246 ],
                      "running": [ ],
                      "success": [ 251, 256, 266, 276, 286, 291, 296, 301, 306, 311, 316, 321, 326, 331 ] },
    "acooh": { "failed": [ 139, 189, 214, 229, 249, 269, 289, 234, 239, 244, 254, 259, 264, 274, 279, 284, 304, 309, 319, 324, 329 ],
               "running": [  ],
               "success": [ 294, 299, 334, 339 ] },
    "octanoic_acid": { "failed": [ 229, 234, 239, 244, 249, 254, 259, 264, 269, 274, 279, 284, 294, 299, 304, 309, 314, 324 ],
                       "running": [  ],
                       "success": [ 319, 329, 334, 339 ] },
    "succinic_acid": { "failed": [ 309, 359, 384, 389, 394, 399, 404, 409, 414, 419, 429, 434, 439, 454, 469, 494, 499, 509, 514, 424, 464, 504 ],
                       "running": [  ],
                       "success": [  ] },
    # formaide at 253K might be considered as converged, at 263K polycrystalline
    "formamide": { "failed": [ 298  ],
                   "running": [  ],
                   "success": [ 248, 253, 258, 273, 288, 263, 268, 278, 283, 293, 303, 308, 313, 318, 323, 328, 333, 338, 343, 348 ] },
    "acetamide": { "failed": [ 104, 154, 204, 254, 279, 284 ],
                   "running": [  ],
                   "success": [ 289, 294, 299, 304, 309, 314, 319, 324, 329, 334, 339, 344, 349, 359, 364, 369, 374, 379, 384, 389, 394, 399, 404 ] },
    "urea": { "failed": [ 436 ],
              "running": [  ],
              "success": [ 356, 361, 366, 371, 376, 381, 386, 391, 396, 401, 406, 411, 416, 421, 426, 431, 441, 446, 451, 456 ] },
    "formaldehyde": { "failed": [  ],
                      "running": [  ],
                      "success": [ 131, 136, 141, 146, 151, 156, 161, 166, 171, 176, 181, 186, 191, 196, 201, 206, 211, 216, 221, 226, 231 ] },
    "uracil": { "failed": [  ],
                "running": [  ],
                "success": [ 561, 566, 571, 576, 581, 586, 591, 596, 601, 606, 616, 621, 626, 631, 636, 641, 646, 651, 656, 661, 666, 671, 676, 681, 686, 711, 731, 736, 741, 746, 751, 756, 761, 766, 771, 786, 811, 861 ] },
    "pyridine": { "failed": [ 181, 186, 191, 196, 201, 206, 211, 216, 221, 226, 236, 241, 251, 281 ],
                  "running": [  ],
                  "success": [ 246, 256, 261, 266, 271, 276 ] }}

def check_status() -> bool:
    allwell = True
    for mol in sim_status:
        for tfail in sim_status[mol]["failed"]:
            if tfail in sim_status[mol]["success"]:
                print("mol %s temp %d in both failed and success" % ( mol, tfail ))
                allwell = False
            elif tfail in sim_status[mol]["running"]:
                print("mol %s temp %d in both failed and running" % ( mol, tfail ))
                allwell = False
        for trun in sim_status[mol]["running"]:
            if trun in sim_status[mol]["success"]:
                print("mol %s temp %d in both running and success" % ( mol, trun ))
                allwell = False
    return allwell
        
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
        if m in ftemp and m in rtemp and not (int(m) in sim_status[compound]["failed"]):
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
            this_size = min_size
            if max_size > min_size:
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
    if not check_status():
        sys.exit("Fix table!")
    moldb = get_moldb(False)
    os.chdir("bcc/melt")
    for mol in moldb.keys():
        if os.path.isdir(mol):
            os.chdir(mol)
            alltemp = get_temps(mol)
            do_msd(alltemp)
            do_rotacf(alltemp)
            do_filesize(alltemp)
            os.chdir("..")
        else:
            sys.exit("No mol %s in %s" % ( mol, os.getcwd() ) )
