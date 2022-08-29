#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2816 -f /home/spoel/wd/MDBenchmark/melting/ethane/100/melting-npt-y.edr -o epot_100.xvg
