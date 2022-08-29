#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2400 -f /home/lschmidt/MELTING/succinic_acid/succinic_acid489.0/melting-nvt.edr -o epot_489.xvg
