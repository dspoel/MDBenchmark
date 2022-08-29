#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/12-ethanediamine/309/melting-npt-y.tpr -o rdf_309.xvg -b 1517 -e 1717 
