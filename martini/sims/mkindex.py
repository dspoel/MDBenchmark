#!/usr/bin/env python3

import argparse, os

def make_index(nmol:int, natom:int, indices:list):
    with open("index.ndx", "w") as outf:
        outf.write("[ index ]\n")
        for i in range(nmol):
            for j in range(len(indices)):
                outf.write("  %d" % ( i*natom+indices[j]) )
            outf.write("\n")

                
def parseArguments():
    parser = argparse.ArgumentParser(
      prog='mkindex.py',
      description=
"""
Script to generate index file to convert from all-atom to Martini
""")
    parser.add_argument("-natom", "--natom", help="Number of atoms per molecule", type=int, default=1)
    parser.add_argument("-nmol", "--nmol", help="Number of molecules", type=int, default=1)
    parser.add_argument("-index", "--index", nargs='+', help="Atom indices in AA compound", type=int, default=0)
    return parser.parse_args()
    
if __name__ == '__main__':
    args = parseArguments()
    make_index(args.nmol, args.natom, args.index)

