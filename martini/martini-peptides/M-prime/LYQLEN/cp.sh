#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M-prime/LYQLEN/NPT_LYQLEN_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M-prime/LYQLEN/NPT100_LYQLEN_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M-prime/LYQLEN/BR/NPT_LYQLEN_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M-prime/LYQLEN/BR/NPT100_LYQLEN_Berendsen_Final.gro .

rm slurm*.out



