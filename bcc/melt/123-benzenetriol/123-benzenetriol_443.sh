#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/123-benzenetriol_rotaxis.ndx -f /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol443.0/melting-npt-y.trr -s /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol443.0/melting-npt-y.tpr -o rotacf_443.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/123-benzenetriol_rotplane.ndx -f /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol443.0/melting-npt-y.trr -s /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol443.0/melting-npt-y.tpr -o rotplane_443.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol443.0/melting-npt-y.trr -s /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol443.0/melting-npt-y.tpr -o msd_443.xvg -b 0 -e 2000 
