#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.trr -s /home/spoel/wd/MDBenchmark/melting/formamide/298/melting-npt-y_20_NPTY.tpr -o rdf_298.xvg -b 39825 -e 40025 
