#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethylene_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.tpr -o rotacf_79.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/ethylene_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.tpr -o rotplane_79.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/79/melting-npt-y2.tpr -o msd_79.xvg -b 2000 -e 4000 
