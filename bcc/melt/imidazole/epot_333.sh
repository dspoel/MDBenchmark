#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3360 -f /home/spoel/wd/MDBenchmark/melting/imidazole/333/melting-npt-y.edr -o epot_333.xvg
