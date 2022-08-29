#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/benzene_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/benzene/233/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/benzene/233/melting-npt-y.tpr -o rotacf_233.xvg -b 4000 -e 6000 
gmx rotacf -n ../../../index/benzene_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/benzene/233/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/benzene/233/melting-npt-y.tpr -o rotplane_233.xvg -b 4000 -e 6000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/benzene/233/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/benzene/233/melting-npt-y.tpr -o msd_233.xvg -b 4000 -e 6000 
