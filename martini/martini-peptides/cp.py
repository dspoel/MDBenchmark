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

            
        with open("cp.sh", "w") as script:
            script.write(f"""#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16


cp /home/nhosseini/marpep/martini-peptides/{maindir}/{subdir}/NPT_{subdir}_PR_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/{maindir}/{subdir}/NPT100_{subdir}_PR_Final.gro .

cp /home/nhosseini/venus/martini/martini-peptides/{maindir}/{subdir}/BR/NPT_{subdir}_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/{maindir}/{subdir}/BR/NPT100_{subdir}_Berendsen_Final.gro .

rm slurm*.out



""")

        os.system("chmod +x cp.sh")
        os.system("sbatch cp.sh")

        os.chdir("..")

    os.chdir("..")
