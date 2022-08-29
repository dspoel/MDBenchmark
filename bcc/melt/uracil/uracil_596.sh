#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/uracil_rotaxis.ndx -f /home/lschmidt/MELTING/uracil/uracil596.0/melting-npt-y.trr -s /home/lschmidt/MELTING/uracil/uracil596.0/melting-npt-y.tpr -o rotacf_596.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/uracil_rotplane.ndx -f /home/lschmidt/MELTING/uracil/uracil596.0/melting-npt-y.trr -s /home/lschmidt/MELTING/uracil/uracil596.0/melting-npt-y.tpr -o rotplane_596.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/uracil/uracil596.0/melting-npt-y.trr -s /home/lschmidt/MELTING/uracil/uracil596.0/melting-npt-y.tpr -o msd_596.xvg -b 0 -e 2000 
