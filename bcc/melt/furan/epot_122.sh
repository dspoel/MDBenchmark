#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2048 -f /home/lschmidt/MELTING/furan/furan122.0/melting-npt-y_ori.edr -o epot_122.xvg
