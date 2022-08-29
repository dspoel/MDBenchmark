#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/formic_acid/formic_acid281.0/melting-nvt.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid281.0/melting-nvt.tpr -o rotacf_281.xvg -b -200 -e 0 
gmx rotacf -n ../../../index/formic_acid_rotplane.ndx -f /home/lschmidt/MELTING/formic_acid/formic_acid281.0/melting-nvt.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid281.0/melting-nvt.tpr -o rotplane_281.xvg -b -200 -e 0 
echo 0 | gmx msd -f /home/lschmidt/MELTING/formic_acid/formic_acid281.0/melting-nvt.trr -s /home/lschmidt/MELTING/formic_acid/formic_acid281.0/melting-nvt.tpr -o msd_281.xvg -b -200 -e 0 
