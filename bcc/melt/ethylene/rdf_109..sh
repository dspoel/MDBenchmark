#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.trr -s /home/lschmidt/MELTING/ethene/ethene109.0/melting-npt-y2.tpr -o rdf_109.xvg -b 1800 -e 2000 
