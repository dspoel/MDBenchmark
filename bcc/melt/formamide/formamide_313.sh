#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formamide_rotaxis.ndx -f /home/lschmidt/MELTING/formamide/formamide313.0/melting-npt-y_5_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide313.0/melting-npt-y_5_NPTY.tpr -o rotacf_313.xvg -b 3000 -e 5000 
gmx rotacf -n ../../../index/formamide_rotplane.ndx -f /home/lschmidt/MELTING/formamide/formamide313.0/melting-npt-y_5_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide313.0/melting-npt-y_5_NPTY.tpr -o rotplane_313.xvg -b 3000 -e 5000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/formamide/formamide313.0/melting-npt-y_5_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide313.0/melting-npt-y_5_NPTY.tpr -o msd_313.xvg -b 3000 -e 5000 
