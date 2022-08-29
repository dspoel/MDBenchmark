#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/14-benzoquinone_rotaxis.ndx -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone413.0/melting-npt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone413.0/melting-npt.tpr -o rotacf_413.xvg -b -243 -e 1757 
gmx rotacf -n ../../../index/14-benzoquinone_rotplane.ndx -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone413.0/melting-npt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone413.0/melting-npt.tpr -o rotplane_413.xvg -b -243 -e 1757 
echo 0 | gmx msd -f /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone413.0/melting-npt.trr -s /home/lschmidt/MELTING/14-benzoquinone/14-benzoquinone413.0/melting-npt.tpr -o msd_413.xvg -b -243 -e 1757 
