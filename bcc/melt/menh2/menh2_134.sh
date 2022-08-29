#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/menh2_rotaxis.ndx -f /home/lschmidt/MELTING/menh2/menh2134.0/melting-npt-y.trr -s /home/lschmidt/MELTING/menh2/menh2134.0/melting-npt-y.tpr -o rotacf_134.xvg -b -466 -e 1534 
gmx rotacf -n ../../../index/menh2_rotplane.ndx -f /home/lschmidt/MELTING/menh2/menh2134.0/melting-npt-y.trr -s /home/lschmidt/MELTING/menh2/menh2134.0/melting-npt-y.tpr -o rotplane_134.xvg -b -466 -e 1534 
echo 0 | gmx msd -f /home/lschmidt/MELTING/menh2/menh2134.0/melting-npt-y.trr -s /home/lschmidt/MELTING/menh2/menh2134.0/melting-npt-y.tpr -o msd_134.xvg -b -466 -e 1534 
