#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.trr -s /home/lschmidt/MELTING/urea/urea426.0/melting-npt-y_8.tpr -o rdf_426.xvg -b 3800 -e 4000 
