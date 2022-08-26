#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/ethylene/84/melting-npt-y2.trr -s /home/spoel/wd/MDBenchmark/melting/ethylene/84/melting-npt-y2.tpr -o rdf_84.xvg -b 3800 -e 4000 
