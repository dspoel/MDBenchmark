#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.trr -s /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.tpr -o rdf_181.xvg -b 1800 -e 2000 
