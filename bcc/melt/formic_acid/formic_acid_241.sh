#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/formic_acid/formic_acid241.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid241.0/melting-npt-y_2.tpr -o rotacf_241.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/formic_acid_rotplane.ndx -f /home/lschmidt/MELTING/formic_acid/formic_acid241.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid241.0/melting-npt-y_2.tpr -o rotplane_241.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/formic_acid/formic_acid241.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid241.0/melting-npt-y_2.tpr -o msd_241.xvg -b 0 -e 2000 
