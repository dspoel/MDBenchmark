#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2048 -f /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.edr -o epot_117.xvg
