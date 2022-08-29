#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/acetamide_rotaxis.ndx -f /home/lschmidt/MELTING/acetamide/acetamide154.0/melting-npt-y_4ns.trr -s /home/lschmidt/MELTING/acetamide/acetamide154.0/melting-npt-y_4ns.tpr -o rotacf_154.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/acetamide_rotplane.ndx -f /home/lschmidt/MELTING/acetamide/acetamide154.0/melting-npt-y_4ns.trr -s /home/lschmidt/MELTING/acetamide/acetamide154.0/melting-npt-y_4ns.tpr -o rotplane_154.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/acetamide/acetamide154.0/melting-npt-y_4ns.trr -s /home/lschmidt/MELTING/acetamide/acetamide154.0/melting-npt-y_4ns.tpr -o msd_154.xvg -b 2000 -e 4000 
