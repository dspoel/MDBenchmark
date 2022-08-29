#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/furan_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.trr -s /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.tpr -o rotacf_117.xvg -b 30007 -e 32007 
gmx rotacf -n ../../../index/furan_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.trr -s /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.tpr -o rotplane_117.xvg -b 30007 -e 32007 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.trr -s /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.tpr -o msd_117.xvg -b 30007 -e 32007 
