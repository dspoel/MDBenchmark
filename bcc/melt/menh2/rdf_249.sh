#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.trr -s /home/spoel/wd/MDBenchmark/melting/menh2/249/melting-npt-y_2.tpr -o rdf_249.xvg -b 3800 -e 4000 
