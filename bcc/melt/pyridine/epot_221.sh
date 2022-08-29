#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2880 -f /home/lschmidt/MELTING/pyridine/pyridine221.0/melting-npt-y.edr -o epot_221.xvg
