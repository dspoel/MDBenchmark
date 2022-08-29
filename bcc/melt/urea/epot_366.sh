#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2304 -f /home/lschmidt/MELTING/urea/urea366.0/melting-npt-y_2.edr -o epot_366.xvg
