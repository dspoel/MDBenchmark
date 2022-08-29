#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 2520 -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.edr -o epot_260.xvg
