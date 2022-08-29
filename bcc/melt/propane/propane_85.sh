#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/propane_rotaxis.ndx -f /home/lschmidt/MELTING/propane/propane85.0/melting-npt.trr -s /home/lschmidt/MELTING/propane/propane85.0/melting-npt.tpr -o rotacf_85.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/propane_rotplane.ndx -f /home/lschmidt/MELTING/propane/propane85.0/melting-npt.trr -s /home/lschmidt/MELTING/propane/propane85.0/melting-npt.tpr -o rotplane_85.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/propane/propane85.0/melting-npt.trr -s /home/lschmidt/MELTING/propane/propane85.0/melting-npt.tpr -o msd_85.xvg -b 0 -e 2000 
