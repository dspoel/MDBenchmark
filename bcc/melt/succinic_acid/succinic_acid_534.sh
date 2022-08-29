#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rotacf -d -n ../../../index/succinic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/succinic_acid/succinic_acid534.0/melting-nvt.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid534.0/melting-nvt.tpr -o rotacf_534.xvg -b -199 -e 1 
gmx rotacf -n ../../../index/succinic_acid_rotplane.ndx -f /home/lschmidt/MELTING/succinic_acid/succinic_acid534.0/melting-nvt.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid534.0/melting-nvt.tpr -o rotplane_534.xvg -b -199 -e 1 
echo 0 | gmx msd -f /home/lschmidt/MELTING/succinic_acid/succinic_acid534.0/melting-nvt.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid534.0/melting-nvt.tpr -o msd_534.xvg -b -199 -e 1 
