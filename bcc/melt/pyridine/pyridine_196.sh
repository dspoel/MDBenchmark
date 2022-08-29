#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/pyridine_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/pyridine/196/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/pyridine/196/melting-npt-y.tpr -o rotacf_196.xvg -b 400 -e 2400 
gmx rotacf -n ../../../index/pyridine_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/pyridine/196/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/pyridine/196/melting-npt-y.tpr -o rotplane_196.xvg -b 400 -e 2400 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/pyridine/196/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/pyridine/196/melting-npt-y.tpr -o msd_196.xvg -b 400 -e 2400 
