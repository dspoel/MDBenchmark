#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2688 -f /home/lschmidt/MELTING/propane/propane65.0/melting-npt-y.edr -o epot_65.xvg
