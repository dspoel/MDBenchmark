#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/formamide/258/melting-npt-y_10_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/258/melting-npt-y_10_NPTY.tpr -o rdf_258.xvg -b 14827 -e 15027 
