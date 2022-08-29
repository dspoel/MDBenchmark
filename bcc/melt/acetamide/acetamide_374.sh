#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/acetamide_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.tpr -o rotacf_374.xvg -b 300 -e 2300 
gmx rotacf -n ../../../index/acetamide_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.tpr -o rotplane_374.xvg -b 300 -e 2300 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/acetamide/374/melting-npt-y.tpr -o msd_374.xvg -b 300 -e 2300 
