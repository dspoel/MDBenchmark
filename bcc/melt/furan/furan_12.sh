#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/furan_rotaxis.ndx -f /home/lschmidt/MELTING/furan/furan12.0/melting-npt-y_4ns.trr -s /home/lschmidt/MELTING/furan/furan12.0/melting-npt-y_4ns.tpr -o rotacf_12.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/furan_rotplane.ndx -f /home/lschmidt/MELTING/furan/furan12.0/melting-npt-y_4ns.trr -s /home/lschmidt/MELTING/furan/furan12.0/melting-npt-y_4ns.tpr -o rotplane_12.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/furan/furan12.0/melting-npt-y_4ns.trr -s /home/lschmidt/MELTING/furan/furan12.0/melting-npt-y_4ns.tpr -o msd_12.xvg -b 2000 -e 4000 
