#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16




cp /home/nhosseini/venus/martini/martini-peptides/M-primeprime/NNQQ2/BR/NPT_NNQQ2_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/M-primeprime/NNQQ2/BR/NPT100_NNQQ2_Berendsen_Final.gro .

rm slurm*.out


