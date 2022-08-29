#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3600 -f /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.edr -o epot_374.xvg
