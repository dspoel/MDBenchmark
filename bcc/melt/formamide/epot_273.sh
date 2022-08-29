#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2112 -f /home/spoel/wd/MDBenchmark/melting/formamide/273/melting-npt-y_10_NPTY.edr -o epot_273.xvg
