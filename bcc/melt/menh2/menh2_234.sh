#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/menh2_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.tpr -o rotacf_234.xvg -b 4000 -e 6000 
gmx rotacf -n ../../../index/menh2_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.tpr -o rotplane_234.xvg -b 4000 -e 6000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/234/melting-npt-y_2.tpr -o msd_234.xvg -b 4000 -e 6000 
