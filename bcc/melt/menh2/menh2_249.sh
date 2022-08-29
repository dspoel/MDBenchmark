#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/menh2_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.tpr -o rotacf_249.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/menh2_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.tpr -o rotplane_249.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.tpr -o msd_249.xvg -b 2000 -e 4000 
