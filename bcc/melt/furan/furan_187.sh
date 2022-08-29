#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/furan_rotaxis.ndx -f /home/lschmidt/MELTING/furan/furan187.0/melting-nvt.trr -s /home/lschmidt/MELTING/furan/furan187.0/melting-nvt.tpr -o rotacf_187.xvg -b -200 -e 0 
gmx rotacf -n ../../../index/furan_rotplane.ndx -f /home/lschmidt/MELTING/furan/furan187.0/melting-nvt.trr -s /home/lschmidt/MELTING/furan/furan187.0/melting-nvt.tpr -o rotplane_187.xvg -b -200 -e 0 
echo 0 | gmx msd -f /home/lschmidt/MELTING/furan/furan187.0/melting-nvt.trr -s /home/lschmidt/MELTING/furan/furan187.0/melting-nvt.tpr -o msd_187.xvg -b -200 -e 0 
