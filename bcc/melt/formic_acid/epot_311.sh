#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3072 -f /home/lschmidt/MELTING/formic_acid/formic_acid311.0/melting-npt-y_2.edr -o epot_311.xvg
