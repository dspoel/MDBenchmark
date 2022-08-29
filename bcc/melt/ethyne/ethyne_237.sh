#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethyne_rotaxis.ndx -f /home/lschmidt/MELTING/ethyne/ethyne237.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/ethyne/ethyne237.0/melting-npt-y_2.tpr -o rotacf_237.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/ethyne/ethyne237.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/ethyne/ethyne237.0/melting-npt-y_2.tpr -o msd_237.xvg -b 0 -e 2000 
