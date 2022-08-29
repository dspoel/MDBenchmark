#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/cyclohexane_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/cyclohexane/289/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/cyclohexane/289/melting-npt-y.tpr -o rotacf_289.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/cyclohexane_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/cyclohexane/289/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/cyclohexane/289/melting-npt-y.tpr -o rotplane_289.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/cyclohexane/289/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/cyclohexane/289/melting-npt-y.tpr -o msd_289.xvg -b 2000 -e 4000 
