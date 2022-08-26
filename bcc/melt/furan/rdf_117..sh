#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.trr -s /home/spoel/wd/MDBenchmark/melting/furan/117/melting-npt-y_ori.tpr -o rdf_117.xvg -b 31807 -e 32007 
