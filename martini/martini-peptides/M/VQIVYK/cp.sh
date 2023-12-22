#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16




cp /home/nhosseini/venus/martini/martini-peptides/M/VQIVYK/BR/NPT_VQIVYK_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/M/VQIVYK/BR/NPT100_VQIVYK_Berendsen_Final.gro .

rm slurm*.out



