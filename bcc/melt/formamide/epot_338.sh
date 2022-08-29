#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2112 -f /home/lschmidt/MELTING/formamide/formamide338.0/melting-npt-y.edr -o epot_338.xvg
