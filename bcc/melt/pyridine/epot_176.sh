#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2880 -f /home/lschmidt/MELTING/pyridine/pyridine176.0/melting-nvt.edr -o epot_176.xvg
