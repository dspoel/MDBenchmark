#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/ethane/95/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethane/95/melting-npt-y.tpr -o rdf_95.xvg -b 5800 -e 6000 
