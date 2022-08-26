#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.trr -s /home/lschmidt/MELTING/urea/urea431.0/melting-npt-y_18.tpr -o rdf_431.xvg -b 9800 -e 10000 
