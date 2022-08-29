#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/formic_acid/formic_acid246.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid246.0/melting-npt-y_2.tpr -o rotacf_246.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/formic_acid_rotplane.ndx -f /home/lschmidt/MELTING/formic_acid/formic_acid246.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid246.0/melting-npt-y_2.tpr -o rotplane_246.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/formic_acid/formic_acid246.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid246.0/melting-npt-y_2.tpr -o msd_246.xvg -b 0 -e 2000 
