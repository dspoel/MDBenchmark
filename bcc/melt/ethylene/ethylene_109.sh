#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethylene_rotaxis.ndx -f /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.tpr -o rotacf_109.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/ethylene_rotplane.ndx -f /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.tpr -o rotplane_109.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.tpr -o msd_109.xvg -b 0 -e 2000 
