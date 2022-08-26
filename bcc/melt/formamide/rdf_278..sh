#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/formamide/formamide278.0/melting-npt-y_10_NPTY.trr -s /home/lschmidt/MELTING/formamide/formamide278.0/melting-npt-y_10_NPTY.tpr -o rdf_278.xvg -b 4800 -e 5000 
