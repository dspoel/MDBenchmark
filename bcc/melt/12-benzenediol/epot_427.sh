#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3168 -f /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.edr -o epot_427.xvg
