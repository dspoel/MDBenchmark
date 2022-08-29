#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/pyridine_rotaxis.ndx -f /home/lschmidt/MELTING/pyridine/pyridine231.0/melting-nvt.trr -s /home/lschmidt/MELTING/pyridine/pyridine231.0/melting-nvt.tpr -o rotacf_231.xvg -b -190 -e 10 
gmx rotacf -n ../../../index/pyridine_rotplane.ndx -f /home/lschmidt/MELTING/pyridine/pyridine231.0/melting-nvt.trr -s /home/lschmidt/MELTING/pyridine/pyridine231.0/melting-nvt.tpr -o rotplane_231.xvg -b -190 -e 10 
echo 0 | gmx msd -f /home/lschmidt/MELTING/pyridine/pyridine231.0/melting-nvt.trr -s /home/lschmidt/MELTING/pyridine/pyridine231.0/melting-nvt.tpr -o msd_231.xvg -b -190 -e 10 
