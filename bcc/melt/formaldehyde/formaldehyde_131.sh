#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formaldehyde_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/131/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/131/melting-npt-y_L.tpr -o rotacf_131.xvg -b 2000 -e 4000 
gmx rotacf -n ../../../index/formaldehyde_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/131/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/131/melting-npt-y_L.tpr -o rotplane_131.xvg -b 2000 -e 4000 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/131/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/131/melting-npt-y_L.tpr -o msd_131.xvg -b 2000 -e 4000 
