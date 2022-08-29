#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/urea_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.trr -s /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.tpr -o rotacf_436.xvg -b 10045 -e 12045 
gmx rotacf -n ../../../index/urea_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.trr -s /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.tpr -o rotplane_436.xvg -b 10045 -e 12045 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.trr -s /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.tpr -o msd_436.xvg -b 10045 -e 12045 
