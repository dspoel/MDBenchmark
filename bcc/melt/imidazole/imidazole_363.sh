#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/imidazole_rotaxis.ndx -f /home/lschmidt/MELTING/imidazole/imidazole363.0/melting-nvt.trr -s /home/lschmidt/MELTING/imidazole/imidazole363.0/melting-nvt.tpr -o rotacf_363.xvg -b -200 -e 0 
gmx rotacf -n ../../../index/imidazole_rotplane.ndx -f /home/lschmidt/MELTING/imidazole/imidazole363.0/melting-nvt.trr -s /home/lschmidt/MELTING/imidazole/imidazole363.0/melting-nvt.tpr -o rotplane_363.xvg -b -200 -e 0 
echo 0 | gmx msd -f /home/lschmidt/MELTING/imidazole/imidazole363.0/melting-nvt.trr -s /home/lschmidt/MELTING/imidazole/imidazole363.0/melting-nvt.tpr -o msd_363.xvg -b -200 -e 0 
