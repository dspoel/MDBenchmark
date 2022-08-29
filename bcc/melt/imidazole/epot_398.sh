#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3360 -f /home/lschmidt/MELTING/imidazole/imidazole398.0/melting-npt-y.edr -o epot_398.xvg
