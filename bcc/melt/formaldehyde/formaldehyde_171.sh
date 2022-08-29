#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formaldehyde_rotaxis.ndx -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.tpr -o rotacf_171.xvg -b 891 -e 2891 
gmx rotacf -n ../../../index/formaldehyde_rotplane.ndx -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.tpr -o rotplane_171.xvg -b 891 -e 2891 
echo 0 | gmx msd -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.tpr -o msd_171.xvg -b 891 -e 2891 
