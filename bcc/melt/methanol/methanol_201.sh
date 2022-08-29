#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/methanol_rotaxis.ndx -f /home/lschmidt/MELTING/methanol/methanol201.0/melting-npt-y_L.trr -s /home/lschmidt/MELTING/methanol/methanol201.0/melting-npt-y_L.tpr -o rotacf_201.xvg -b -1000 -e 1000 
gmx rotacf -n ../../../index/methanol_rotplane.ndx -f /home/lschmidt/MELTING/methanol/methanol201.0/melting-npt-y_L.trr -s /home/lschmidt/MELTING/methanol/methanol201.0/melting-npt-y_L.tpr -o rotplane_201.xvg -b -1000 -e 1000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/methanol/methanol201.0/melting-npt-y_L.trr -s /home/lschmidt/MELTING/methanol/methanol201.0/melting-npt-y_L.tpr -o msd_201.xvg -b -1000 -e 1000 
