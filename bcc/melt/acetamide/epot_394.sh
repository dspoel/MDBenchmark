#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3600 -f /home/lschmidt/MELTING/acetamide/acetamide394.0/melting-npt-y_2.edr -o epot_394.xvg
