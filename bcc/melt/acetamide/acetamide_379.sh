#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/acetamide_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.tpr -o rotacf_379.xvg -b 1000 -e 3000 
gmx rotacf -n ../../../index/acetamide_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.tpr -o rotplane_379.xvg -b 1000 -e 3000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/acetamide/379/melting-npt-y_2.tpr -o msd_379.xvg -b 1000 -e 3000 
