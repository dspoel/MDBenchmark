#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/acetamide_rotaxis.ndx -f /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.trr -s /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.tpr -o rotacf_369.xvg -b -198 -e 2 
gmx rotacf -n ../../../index/acetamide_rotplane.ndx -f /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.trr -s /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.tpr -o rotplane_369.xvg -b -198 -e 2 
echo 0 | gmx msd -f /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.trr -s /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.tpr -o msd_369.xvg -b -198 -e 2 
