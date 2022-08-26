#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/ethane/ethane110.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethane/ethane110.0/melting-npt-y.tpr -o rdf_110.xvg -b 1800 -e 2000 
