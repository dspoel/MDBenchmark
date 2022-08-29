#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethane_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethane/85/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/85/melting-npt-y.tpr -o rotacf_85.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/ethane_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethane/85/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/85/melting-npt-y.tpr -o rotplane_85.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethane/85/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/85/melting-npt-y.tpr -o msd_85.xvg -b 0 -e 2000 
