#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16




cp /home/nhosseini/venus/martini/martini-peptides/M-primeprime/NNFGAIL/BR/NPT_NNFGAIL_Berendsen_Final.gro .
cp /home/nhosseini/venus/martini/martini-peptides/M-primeprime/NNFGAIL/BR/NPT100_NNFGAIL_Berendsen_Final.gro .

rm slurm*.out



