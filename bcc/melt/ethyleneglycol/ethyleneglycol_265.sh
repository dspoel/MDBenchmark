#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethyleneglycol_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/265/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/265/melting-npt-y.tpr -o rotacf_265.xvg -b 3662 -e 5662 
gmx rotacf -n ../../../index/ethyleneglycol_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/265/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/265/melting-npt-y.tpr -o rotplane_265.xvg -b 3662 -e 5662 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/265/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/265/melting-npt-y.tpr -o msd_265.xvg -b 3662 -e 5662 
