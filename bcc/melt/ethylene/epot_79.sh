#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2268 -f /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.edr -o epot_79.xvg
