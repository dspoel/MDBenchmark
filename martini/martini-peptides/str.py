#!/usr/bin/env python3

#SBATCH -t "2:00:00"
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD

import os
import glob


for maindir in glob.glob("M*"):
    if not os.path.isdir(maindir):
       continue
    os.chdir(maindir)

    for subdir in glob.glob("[A-Z]*" ):
        os.chdir(subdir)

            
        with open("str.sh", "w") as script:
            script.write(f"""#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16


mv NPT.gro NPT_{subdir}_PR_Final.gro
mv NPT100.gro NPT100_{subdir}_PR_Final.gro

cd BR

mv NPT.gro NPT_{subdir}_Berendsen_Final.gro
mv NPT100.gro NPT100_{subdir}_Berendsen_Final.gro



""")

        os.system("chmod +x str.sh")
        os.system("sbatch str.sh")

        os.chdir("..")

    os.chdir("..")
