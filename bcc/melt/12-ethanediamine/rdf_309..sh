#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/ethylendiamine/ethylendiamine309.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylendiamine/ethylendiamine309.0/melting-npt-y.tpr -o rdf_309.xvg -b 1517 -e 1717 
