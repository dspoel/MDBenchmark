#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/acooh_rotaxis.ndx -f /home/lschmidt/MELTING/acoh/acoh314.0/melting-nvt.trr -s /home/lschmidt/MELTING/acoh/acoh314.0/melting-nvt.tpr -o rotacf_314.xvg -b -198 -e 2 
gmx rotacf -n ../../../index/acooh_rotplane.ndx -f /home/lschmidt/MELTING/acoh/acoh314.0/melting-nvt.trr -s /home/lschmidt/MELTING/acoh/acoh314.0/melting-nvt.tpr -o rotplane_314.xvg -b -198 -e 2 
echo 0 | gmx msd -f /home/lschmidt/MELTING/acoh/acoh314.0/melting-nvt.trr -s /home/lschmidt/MELTING/acoh/acoh314.0/melting-nvt.tpr -o msd_314.xvg -b -198 -e 2 
