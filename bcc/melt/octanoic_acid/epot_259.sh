#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2912 -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid259.0/melting-npt-y.edr -o epot_259.xvg
