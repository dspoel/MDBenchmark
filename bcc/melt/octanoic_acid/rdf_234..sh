#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.trr -s /home/lschmidt/MELTING/octanoic_acid/octanoic_acid234.0/melting-npt-y_22_NPTY.tpr -o rdf_234.xvg -b 21800 -e 22000 
