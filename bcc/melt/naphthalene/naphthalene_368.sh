#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/naphthalene_rotaxis.ndx -f /home/lschmidt/MELTING/naphthalene/naphthalene368.0/melting-npt-y.trr -s /home/lschmidt/MELTING/naphthalene/naphthalene368.0/melting-npt-y.tpr -o rotacf_368.xvg -b -490 -e 1510 
gmx rotacf -n ../../../index/naphthalene_rotplane.ndx -f /home/lschmidt/MELTING/naphthalene/naphthalene368.0/melting-npt-y.trr -s /home/lschmidt/MELTING/naphthalene/naphthalene368.0/melting-npt-y.tpr -o rotplane_368.xvg -b -490 -e 1510 
echo 0 | gmx msd -f /home/lschmidt/MELTING/naphthalene/naphthalene368.0/melting-npt-y.trr -s /home/lschmidt/MELTING/naphthalene/naphthalene368.0/melting-npt-y.tpr -o msd_368.xvg -b -490 -e 1510 
