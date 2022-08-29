#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2744 -f /home/lschmidt/MELTING/ethyne/ethyne147.0/melting-npt-y_2.edr -o epot_147.xvg
