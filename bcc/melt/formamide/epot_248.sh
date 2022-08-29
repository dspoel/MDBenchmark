#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2112 -f /home/spoel/wd/MDBenchmark/melting/formamide/248/melting-npt-y_10_NPTY.edr -o epot_248.xvg
