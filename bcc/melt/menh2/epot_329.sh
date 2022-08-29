#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2352 -f /home/lschmidt/MELTING/menh2/menh2329.0/melting-npt-y.edr -o epot_329.xvg
