#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/imidazole_rotaxis.ndx -f /home/lschmidt/MELTING/imidazole/imidazole318.0/melting-npt-y.trr -s /home/lschmidt/MELTING/imidazole/imidazole318.0/melting-npt-y.tpr -o rotacf_318.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/imidazole_rotplane.ndx -f /home/lschmidt/MELTING/imidazole/imidazole318.0/melting-npt-y.trr -s /home/lschmidt/MELTING/imidazole/imidazole318.0/melting-npt-y.tpr -o rotplane_318.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/imidazole/imidazole318.0/melting-npt-y.trr -s /home/lschmidt/MELTING/imidazole/imidazole318.0/melting-npt-y.tpr -o msd_318.xvg -b 0 -e 2000 
