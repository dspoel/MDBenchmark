#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2816 -f /home/lschmidt/MELTING/ethane/ethane145.0/melting-npt-y.edr -o epot_145.xvg
