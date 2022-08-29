#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2400 -f /home/lschmidt/MELTING/succinic_acid/succinic_acid419.0/melting-npt-y_NPTY.edr -o epot_419.xvg
