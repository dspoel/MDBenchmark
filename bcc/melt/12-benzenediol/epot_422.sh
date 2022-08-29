#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3168 -f /home/lschmidt/MELTING/12-benzenediol/12-benzenediol422.0/melting-nvt.edr -o epot_422.xvg
