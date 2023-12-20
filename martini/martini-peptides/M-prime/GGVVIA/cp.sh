#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M-prime/GGVVIA/NPT_GGVVIA_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M-prime/GGVVIA/NPT100_GGVVIA_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M-prime/GGVVIA/BR/NPT_GGVVIA_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M-prime/GGVVIA/BR/NPT100_GGVVIA_Berendsen_Final.gro .

rm slurm*.out



