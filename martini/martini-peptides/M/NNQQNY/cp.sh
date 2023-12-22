#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16




cp /home/nhosseini/venus/martini/martini-peptides/M/NNQQNY/BR/NPT_NNQQNY_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/M/NNQQNY/BR/NPT100_NNQQNY_Berendsen_Final.gro .

rm slurm*.out



