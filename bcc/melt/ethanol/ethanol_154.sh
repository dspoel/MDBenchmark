#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethanol_rotaxis.ndx -f /home/lschmidt/MELTING/ethanol/ethanol154.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethanol/ethanol154.0/melting-npt-y.tpr -o rotacf_154.xvg -b -733 -e 1267 
gmx rotacf -n ../../../index/ethanol_rotplane.ndx -f /home/lschmidt/MELTING/ethanol/ethanol154.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethanol/ethanol154.0/melting-npt-y.tpr -o rotplane_154.xvg -b -733 -e 1267 
echo 0 | gmx msd -f /home/lschmidt/MELTING/ethanol/ethanol154.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethanol/ethanol154.0/melting-npt-y.tpr -o msd_154.xvg -b -733 -e 1267 
