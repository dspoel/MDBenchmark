#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/menh2_rotaxis.ndx -f /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.trr -s /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.tpr -o rotacf_129.xvg -b -190 -e 10 
gmx rotacf -n ../../../index/menh2_rotplane.ndx -f /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.trr -s /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.tpr -o rotplane_129.xvg -b -190 -e 10 
echo 0 | gmx msd -f /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.trr -s /home/lschmidt/MELTING/menh2/menh2129.0/melting-nvt.tpr -o msd_129.xvg -b -190 -e 10 
