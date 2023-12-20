#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M/NNFGAIL/NPT_NNFGAIL_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M/NNFGAIL/NPT100_NNFGAIL_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M/NNFGAIL/BR/NPT_NNFGAIL_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M/NNFGAIL/BR/NPT100_NNFGAIL_Berendsen_Final.gro .

rm slurm*.out



