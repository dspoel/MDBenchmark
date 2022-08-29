#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2800 -f /home/lschmidt/MELTING/uracil/uracil646.0/melting-npt-y.edr -o epot_646.xvg
