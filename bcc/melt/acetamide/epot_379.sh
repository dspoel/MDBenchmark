#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3600 -f /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.edr -o epot_379.xvg
