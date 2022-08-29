#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethylene_rotaxis.ndx -f /home/lschmidt/MELTING/ethene/ethene139.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene139.0/melting-npt-y2.tpr -o rotacf_139.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/ethylene_rotplane.ndx -f /home/lschmidt/MELTING/ethene/ethene139.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene139.0/melting-npt-y2.tpr -o rotplane_139.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/ethene/ethene139.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene139.0/melting-npt-y2.tpr -o msd_139.xvg -b 0 -e 2000 
