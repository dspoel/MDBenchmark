#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/12-benzenediol_rotaxis.ndx -f /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.trr -s /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.tpr -o rotacf_427.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/12-benzenediol_rotplane.ndx -f /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.trr -s /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.tpr -o rotplane_427.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.trr -s /home/lschmidt/MELTING/12-benzenediol/12-benzenediol427.0/melting-npt-y.tpr -o msd_427.xvg -b 0 -e 2000 
