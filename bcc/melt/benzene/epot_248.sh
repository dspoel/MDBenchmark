#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3072 -f /home/spoel/wd/MDBenchmark/melting/benzene/248/melting-npt-y.edr -o epot_248.xvg
