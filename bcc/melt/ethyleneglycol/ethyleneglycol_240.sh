#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/ethyleneglycol_rotaxis.ndx -f /home/lschmidt/MELTING/ethylenglycol/ethylenglycol240.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylenglycol/ethylenglycol240.0/melting-npt-y.tpr -o rotacf_240.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/ethyleneglycol_rotplane.ndx -f /home/lschmidt/MELTING/ethylenglycol/ethylenglycol240.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylenglycol/ethylenglycol240.0/melting-npt-y.tpr -o rotplane_240.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/ethylenglycol/ethylenglycol240.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylenglycol/ethylenglycol240.0/melting-npt-y.tpr -o msd_240.xvg -b 0 -e 2000 
