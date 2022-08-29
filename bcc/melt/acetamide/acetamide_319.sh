#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/acetamide_rotaxis.ndx -f /home/lschmidt/MELTING/acetamide/acetamide319.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/acetamide/acetamide319.0/melting-npt-y_2.tpr -o rotacf_319.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/acetamide_rotplane.ndx -f /home/lschmidt/MELTING/acetamide/acetamide319.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/acetamide/acetamide319.0/melting-npt-y_2.tpr -o rotplane_319.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/acetamide/acetamide319.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/acetamide/acetamide319.0/melting-npt-y_2.tpr -o msd_319.xvg -b 0 -e 2000 
