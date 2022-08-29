#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formamide_rotaxis.ndx -f /home/lschmidt/MELTING/formamide/formamide253.0/melting-npt-y_10_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide253.0/melting-npt-y_10_NPTY.tpr -o rotacf_253.xvg -b 3000 -e 5000 
gmx rotacf -n ../../../index/formamide_rotplane.ndx -f /home/lschmidt/MELTING/formamide/formamide253.0/melting-npt-y_10_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide253.0/melting-npt-y_10_NPTY.tpr -o rotplane_253.xvg -b 3000 -e 5000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/formamide/formamide253.0/melting-npt-y_10_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide253.0/melting-npt-y_10_NPTY.tpr -o msd_253.xvg -b 3000 -e 5000 
