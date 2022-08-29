#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3072 -f /home/lschmidt/MELTING/benzene/benzene273.0/melting-npt-y.edr -o epot_273.xvg
