#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 71:00:10
#SBATCH -c 16



cp /home/nhosseini/marpep/martini-peptides/M/GNNQQNY/NPT_GNNQQNY_PR_Final.gro . 
cp /home/nhosseini/marpep/martini-peptides/M/GNNQQNY/NPT100_GNNQQNY_PR_Final.gro . 

cp /home/nhosseini/marpep/martini-peptides/M/GNNQQNY/BR/NPT_GNNQQNY_Berendsen_Final.gro .
cp /home/nhosseini/marpep/martini-peptides/M/GNNQQNY/BR/NPT100_GNNQQNY_Berendsen_Final.gro .

rm slurm*.out



