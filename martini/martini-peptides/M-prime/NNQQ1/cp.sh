#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16




cp /home/nhosseini/venus/martini/martini-peptides/M-prime/NNQQ1/BR/NPT_NNQQ1_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/M-prime/NNQQ1/BR/NPT100_NNQQ1_Berendsen_Final.gro .

rm slurm*.out



