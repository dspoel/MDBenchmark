#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethyleneglycol_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/275/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/275/melting-npt-y.tpr -o rotacf_275.xvg -b 781 -e 2781 
gmx rotacf -n ../../../index/ethyleneglycol_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/275/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/275/melting-npt-y.tpr -o rotplane_275.xvg -b 781 -e 2781 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/275/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/275/melting-npt-y.tpr -o msd_275.xvg -b 781 -e 2781 
