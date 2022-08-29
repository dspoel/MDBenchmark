#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethyleneglycol_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.tpr -o rotacf_260.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/ethyleneglycol_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.tpr -o rotplane_260.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/260/melting-npt.tpr -o msd_260.xvg -b 2000 -e 4000 
