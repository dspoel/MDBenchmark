#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2912 -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid254.0/melting-npt-y_22_NPTY.edr -o epot_254.xvg
