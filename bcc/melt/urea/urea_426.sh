#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/urea_rotaxis.ndx -f /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.trr -s /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.tpr -o rotacf_426.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/urea_rotplane.ndx -f /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.trr -s /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.tpr -o rotplane_426.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.trr -s /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.tpr -o msd_426.xvg -b 2000 -e 4000 
