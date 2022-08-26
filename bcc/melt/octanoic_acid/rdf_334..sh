#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid334.0/melting-npt-y_22_NPTY.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid334.0/melting-npt-y_22_NPTY.tpr -o rdf_334.xvg -b 19800 -e 20000 
