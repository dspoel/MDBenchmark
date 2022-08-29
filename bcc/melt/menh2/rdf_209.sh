#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/menh2/209/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/209/melting-npt-y.tpr -o rdf_209.xvg -b 1800 -e 2000 
