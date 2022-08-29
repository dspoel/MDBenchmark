#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/furan_rotaxis.ndx -f /home/lschmidt/MELTING/furan/furan202.0/melting-npt-y_ori.trr -s /home/lschmidt/MELTING/furan/furan202.0/melting-npt-y_ori.tpr -o rotacf_202.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/furan_rotplane.ndx -f /home/lschmidt/MELTING/furan/furan202.0/melting-npt-y_ori.trr -s /home/lschmidt/MELTING/furan/furan202.0/melting-npt-y_ori.tpr -o rotplane_202.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/furan/furan202.0/melting-npt-y_ori.trr -s /home/lschmidt/MELTING/furan/furan202.0/melting-npt-y_ori.tpr -o msd_202.xvg -b 0 -e 2000 
