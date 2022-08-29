#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3600 -f /home/lschmidt/MELTING/acetamide/acetamide299.0/melting-npt-y_4ns.edr -o epot_299.xvg
