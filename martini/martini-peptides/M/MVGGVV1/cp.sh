#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M/MVGGVV1/NPT_MVGGVV1_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M/MVGGVV1/NPT100_MVGGVV1_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M/MVGGVV1/BR/NPT_MVGGVV1_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M/MVGGVV1/BR/NPT100_MVGGVV1_Berendsen_Final.gro .

rm slurm*.out



