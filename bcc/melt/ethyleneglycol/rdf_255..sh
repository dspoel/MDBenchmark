#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/255/melting-npt-y.trr -s /home/spoel/wd/MDBenchmark/melting/ethyleneglycol/255/melting-npt-y.tpr -o rdf_255.xvg -b 2700 -e 2900 
