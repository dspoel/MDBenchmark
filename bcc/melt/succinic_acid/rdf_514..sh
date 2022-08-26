#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid514.0/melting-npt-y_NPTY.tpr -o rdf_514.xvg -b 906 -e 1106 
