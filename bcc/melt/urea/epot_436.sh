#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2304 -f /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.edr -o epot_436.xvg
