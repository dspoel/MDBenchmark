#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3072 -f /home/lschmidt/MELTING/acoh/acoh339.0/melting-npt-y.edr -o epot_339.xvg
