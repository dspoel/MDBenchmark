#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/urea_rotaxis.ndx -f /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.trr -s /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.tpr -o rotacf_431.xvg -b 8000 -e 10000 
gmx rotacf -n ../../../index/urea_rotplane.ndx -f /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.trr -s /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.tpr -o rotplane_431.xvg -b 8000 -e 10000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.trr -s /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.tpr -o msd_431.xvg -b 8000 -e 10000 
