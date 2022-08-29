#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethylene_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/ethylene/104/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/104/melting-npt-y.tpr -o rotacf_104.xvg -b 1587 -e 3587 
gmx rotacf -n ../../../index/ethylene_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/ethylene/104/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/104/melting-npt-y.tpr -o rotplane_104.xvg -b 1587 -e 3587 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/ethylene/104/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/104/melting-npt-y.tpr -o msd_104.xvg -b 1587 -e 3587 
