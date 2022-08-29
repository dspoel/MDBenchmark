#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.trr -s /home/spoel/wd/MDBenchmark/melting/formaldehyde/171/melting-npt-y_L.tpr -o rdf_171.xvg -b 2691 -e 2891 
