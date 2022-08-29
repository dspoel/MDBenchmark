#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/benzene_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/benzene/228/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/benzene/228/melting-npt-y.tpr -o rotacf_228.xvg -b 8000 -e 10000 
gmx rotacf -n ../../../index/benzene_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/benzene/228/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/benzene/228/melting-npt-y.tpr -o rotplane_228.xvg -b 8000 -e 10000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/benzene/228/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/benzene/228/melting-npt-y.tpr -o msd_228.xvg -b 8000 -e 10000 
