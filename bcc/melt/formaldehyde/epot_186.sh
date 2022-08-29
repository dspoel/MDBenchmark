#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2048 -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/186/melting-npt-y_L.edr -o epot_186.xvg
