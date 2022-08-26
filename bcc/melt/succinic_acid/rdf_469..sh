#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/succinic_acid/succinic_acid469.0/melting-nvt.trr -s /home/lschmidt/MELTING/succinic_acid/succinic_acid469.0/melting-nvt.tpr -o rdf_469.xvg -b -190 -e 10 
