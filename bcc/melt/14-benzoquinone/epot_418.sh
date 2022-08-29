#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2304 -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.edr -o epot_418.xvg
