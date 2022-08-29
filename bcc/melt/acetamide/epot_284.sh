#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3600 -f /home/lschmidt/MELTING/acetamide/acetamide284.0/melting-npt-y_4ns.edr -o epot_284.xvg
