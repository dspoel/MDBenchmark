#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2352 -f /home/lschmidt/MELTING/menh2/menh2244.0/melting-npt-y_2.edr -o epot_244.xvg
