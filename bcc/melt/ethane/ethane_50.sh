#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethane_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethane/50/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/50/melting-npt-y.tpr -o rotacf_50.xvg -b 12000 -e 14000 
gmx rotacf -n ../../../index/ethane_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethane/50/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/50/melting-npt-y.tpr -o rotplane_50.xvg -b 12000 -e 14000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethane/50/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/50/melting-npt-y.tpr -o msd_50.xvg -b 12000 -e 14000 
