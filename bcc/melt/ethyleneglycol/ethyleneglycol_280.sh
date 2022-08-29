#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethyleneglycol_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/280/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/280/melting-npt-y.tpr -o rotacf_280.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/ethyleneglycol_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/280/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/280/melting-npt-y.tpr -o rotplane_280.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/280/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/280/melting-npt-y.tpr -o msd_280.xvg -b 0 -e 2000 
