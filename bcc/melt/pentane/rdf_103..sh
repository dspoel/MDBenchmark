#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/pentane/pentane103.0/melting-npt-y.trr -s /home/lschmidt/MELTING/pentane/pentane103.0/melting-npt-y.tpr -o rdf_103.xvg -b 1800 -e 2000 
