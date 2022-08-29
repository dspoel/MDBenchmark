#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/succinic_acid_rotaxis.ndx -f /home/lschmidt/MELTING/succinic_acid/succinic_acid424.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid424.0/melting-npt-y_NPTY.tpr -o rotacf_424.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/succinic_acid_rotplane.ndx -f /home/lschmidt/MELTING/succinic_acid/succinic_acid424.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid424.0/melting-npt-y_NPTY.tpr -o rotplane_424.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/succinic_acid/succinic_acid424.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid424.0/melting-npt-y_NPTY.tpr -o msd_424.xvg -b 0 -e 2000 
