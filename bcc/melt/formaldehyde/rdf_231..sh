#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/formaldehyde/formaldehyde231.0/melting-npt-y_L.trr -s /home/lschmidt/MELTING/formaldehyde/formaldehyde231.0/melting-npt-y_L.tpr -o rdf_231.xvg -b 800 -e 1000 
