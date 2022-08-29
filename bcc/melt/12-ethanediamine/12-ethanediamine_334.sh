#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/12-ethanediamine_rotaxis.ndx -f /home/lschmidt/MELTING/ethylendiamine/ethylendiamine334.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylendiamine/ethylendiamine334.0/melting-npt-y.tpr -o rotacf_334.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/12-ethanediamine_rotplane.ndx -f /home/lschmidt/MELTING/ethylendiamine/ethylendiamine334.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylendiamine/ethylendiamine334.0/melting-npt-y.tpr -o rotplane_334.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/ethylendiamine/ethylendiamine334.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylendiamine/ethylendiamine334.0/melting-npt-y.tpr -o msd_334.xvg -b 0 -e 2000 
