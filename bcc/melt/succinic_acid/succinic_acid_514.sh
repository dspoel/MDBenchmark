#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/succinic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.tpr -o rotacf_514.xvg -b -894 -e 1106 
gmx rotacf -n ../../../index/succinic_acid_rotplane.ndx -f /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.tpr -o rotplane_514.xvg -b -894 -e 1106 
echo 0 | gmx msd -f /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.tpr -o msd_514.xvg -b -894 -e 1106 
