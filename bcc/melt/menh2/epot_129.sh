#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2352 -f /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.edr -o epot_129.xvg
