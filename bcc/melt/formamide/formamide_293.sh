#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formamide_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.tpr -o rotacf_293.xvg -b 13027 -e 15027 
gmx rotacf -n ../../../index/formamide_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.tpr -o rotplane_293.xvg -b 13027 -e 15027 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/293/melting-npt-y_15_NPTY.tpr -o msd_293.xvg -b 13027 -e 15027 
