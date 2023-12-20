#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M-prime/VEALYL/NPT_VEALYL_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M-prime/VEALYL/NPT100_VEALYL_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M-prime/VEALYL/BR/NPT_VEALYL_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M-prime/VEALYL/BR/NPT100_VEALYL_Berendsen_Final.gro .

rm slurm*.out



