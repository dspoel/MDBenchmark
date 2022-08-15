#!/usr/bin/env python3

from get_csv_rows import *

def get_moldb(verbose:bool):
    moldb = {}
    for row in get_csv_rows("molecule_db.csv", 13):
        extrat = []
        for r in range(6, 12):
            if len(row[r]) > 0:
                extrat.append(int(row[r]))
        try:
            moldb[row[0]] = { "natom": int(row[1]), "nsolid": int(row[2]), "Tmin": int(row[3]), "Tmax": int(row[4]), "DeltaT": int(row[5]), "ExtraT": extrat, "Pcryst": int(row[12]) }
        except ValueError:
            print(row)
    if verbose:
        for m in moldb.keys():
            print("%s|%d|%g|%g|%g|%s" % ( m, moldb[m]["nsolid"], moldb[m]["Tmin"], moldb[m]["Tmax"], moldb[m]["DeltaT"], moldb[m]["ExtraT"] ) )
    return moldb

