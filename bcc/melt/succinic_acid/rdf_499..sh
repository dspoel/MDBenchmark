#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/succinic_acid/succinic_acid499.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid499.0/melting-npt-y_NPTY.tpr -o rdf_499.xvg -b 1074 -e 1274 
