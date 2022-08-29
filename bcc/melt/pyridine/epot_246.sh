#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2880 -f /home/lschmidt/MELTING/pyridine/pyridine246.0/melting-npt-y.edr -o epot_246.xvg
