#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/ethyne/ethyne197.0/melting-npt-y_2.trr -s /home/lschmidt/MELTING/ethyne/ethyne197.0/melting-npt-y_2.tpr -o rdf_197.xvg -b 1800 -e 2000 
