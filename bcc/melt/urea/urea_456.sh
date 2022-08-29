#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/urea_rotaxis.ndx -f /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.trr -s /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.tpr -o rotacf_456.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/urea_rotplane.ndx -f /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.trr -s /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.tpr -o rotplane_456.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.trr -s /home/lschmidt/MELTING/urea/urea456.0/melting-npt-y.tpr -o msd_456.xvg -b 0 -e 2000 
