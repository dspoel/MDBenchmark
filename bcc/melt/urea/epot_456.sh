#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2304 -f /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.edr -o epot_456.xvg
