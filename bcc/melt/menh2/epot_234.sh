#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2352 -f /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.edr -o epot_234.xvg
