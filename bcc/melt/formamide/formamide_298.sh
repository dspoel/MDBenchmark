#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formamide_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.tpr -o rotacf_298.xvg -b 38025 -e 40025 
gmx rotacf -n ../../../index/formamide_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.tpr -o rotplane_298.xvg -b 38025 -e 40025 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.tpr -o msd_298.xvg -b 38025 -e 40025 
