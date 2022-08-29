#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2520 -f /home/spoel/wd/MDBenchmark/melting/cyclohexane/234/melting-npt-y.edr -o epot_234.xvg
