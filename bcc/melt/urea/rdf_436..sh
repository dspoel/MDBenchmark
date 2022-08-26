#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.trr -s /home/spoel/wd/MDBenchmark/melting/urea/436/melting-npt-y_28.tpr -o rdf_436.xvg -b 11845 -e 12045 
