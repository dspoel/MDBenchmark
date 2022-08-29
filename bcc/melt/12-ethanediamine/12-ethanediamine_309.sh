#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/12-ethanediamine_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.tpr -o rotacf_309.xvg -b -283 -e 1717 
gmx rotacf -n ../../../index/12-ethanediamine_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.tpr -o rotplane_309.xvg -b -283 -e 1717 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.tpr -o msd_309.xvg -b -283 -e 1717 
