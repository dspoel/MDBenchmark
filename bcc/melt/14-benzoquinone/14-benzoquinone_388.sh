#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/14-benzoquinone_rotaxis.ndx -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone388.0/melting-nvt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone388.0/melting-nvt.tpr -o rotacf_388.xvg -b -200 -e 0 
gmx rotacf -n ../../../index/14-benzoquinone_rotplane.ndx -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone388.0/melting-nvt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone388.0/melting-nvt.tpr -o rotplane_388.xvg -b -200 -e 0 
echo 0 | gmx msd -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone388.0/melting-nvt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone388.0/melting-nvt.tpr -o msd_388.xvg -b -200 -e 0 
