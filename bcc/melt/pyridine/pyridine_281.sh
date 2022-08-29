#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/pyridine_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/pyridine/281/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/pyridine/281/melting-npt-y.tpr -o rotacf_281.xvg -b 1600 -e 3600 
gmx rotacf -n ../../../index/pyridine_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/pyridine/281/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/pyridine/281/melting-npt-y.tpr -o rotplane_281.xvg -b 1600 -e 3600 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/pyridine/281/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/pyridine/281/melting-npt-y.tpr -o msd_281.xvg -b 1600 -e 3600 
