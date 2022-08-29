#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/menh2_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/menh2/224/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/224/melting-npt-y.tpr -o rotacf_224.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/menh2_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/menh2/224/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/224/melting-npt-y.tpr -o rotplane_224.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/menh2/224/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/224/melting-npt-y.tpr -o msd_224.xvg -b 0 -e 2000 
