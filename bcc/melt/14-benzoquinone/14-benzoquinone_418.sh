#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/14-benzoquinone_rotaxis.ndx -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.tpr -o rotacf_418.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/14-benzoquinone_rotplane.ndx -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.tpr -o rotplane_418.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone418.0/melting-npt.tpr -o msd_418.xvg -b 0 -e 2000 
