#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/imidazole_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/imidazole/343/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/imidazole/343/melting-npt-y.tpr -o rotacf_343.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/imidazole_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/imidazole/343/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/imidazole/343/melting-npt-y.tpr -o rotplane_343.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/imidazole/343/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/imidazole/343/melting-npt-y.tpr -o msd_343.xvg -b 2000 -e 4000 
