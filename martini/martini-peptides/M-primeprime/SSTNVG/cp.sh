#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M-primeprime/SSTNVG/NPT_SSTNVG_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M-primeprime/SSTNVG/NPT100_SSTNVG_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M-primeprime/SSTNVG/BR/NPT_SSTNVG_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M-primeprime/SSTNVG/BR/NPT100_SSTNVG_Berendsen_Final.gro .

rm slurm*.out



