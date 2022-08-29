#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/octanoic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid264.0/melting-npt-y.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid264.0/melting-npt-y.tpr -o rotacf_264.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/octanoic_acid_rotplane.ndx -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid264.0/melting-npt-y.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid264.0/melting-npt-y.tpr -o rotplane_264.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid264.0/melting-npt-y.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid264.0/melting-npt-y.tpr -o msd_264.xvg -b 0 -e 2000 
