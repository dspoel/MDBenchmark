#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/benzene_rotaxis.ndx -f /home/lschmidt/MELTING/benzene/benzene298.0/melting-npt-y.trr -s /home/lschmidt/MELTING/benzene/benzene298.0/melting-npt-y.tpr -o rotacf_298.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/benzene_rotplane.ndx -f /home/lschmidt/MELTING/benzene/benzene298.0/melting-npt-y.trr -s /home/lschmidt/MELTING/benzene/benzene298.0/melting-npt-y.tpr -o rotplane_298.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/benzene/benzene298.0/melting-npt-y.trr -s /home/lschmidt/MELTING/benzene/benzene298.0/melting-npt-y.tpr -o msd_298.xvg -b 0 -e 2000 
