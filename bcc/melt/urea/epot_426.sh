#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2304 -f /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.edr -o epot_426.xvg
