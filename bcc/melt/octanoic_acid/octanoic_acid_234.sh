#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/octanoic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.tpr -o rotacf_234.xvg -b 20000 -e 22000 
gmx rotacf -n ../../../index/octanoic_acid_rotplane.ndx -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.tpr -o rotplane_234.xvg -b 20000 -e 22000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.tpr -o msd_234.xvg -b 20000 -e 22000 
