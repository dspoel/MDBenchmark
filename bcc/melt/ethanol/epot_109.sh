#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3200 -f /home/lschmidt/MELTING/ethanol/ethanol109.0/melting-npt-y.edr -o epot_109.xvg
