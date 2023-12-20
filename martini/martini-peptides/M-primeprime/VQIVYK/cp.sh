#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M-primeprime/VQIVYK/NPT_VQIVYK_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M-primeprime/VQIVYK/NPT100_VQIVYK_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M-primeprime/VQIVYK/BR/NPT_VQIVYK_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M-primeprime/VQIVYK/BR/NPT100_VQIVYK_Berendsen_Final.gro .

rm slurm*.out



