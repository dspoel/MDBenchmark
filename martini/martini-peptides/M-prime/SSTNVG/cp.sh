#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16




cp /home/nhosseini/venus/martini/martini-peptides/M-prime/SSTNVG/BR/NPT_SSTNVG_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/M-prime/SSTNVG/BR/NPT100_SSTNVG_Berendsen_Final.gro .

rm slurm*.out


