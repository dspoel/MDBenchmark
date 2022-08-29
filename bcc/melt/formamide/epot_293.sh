#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2112 -f /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.edr -o epot_293.xvg
