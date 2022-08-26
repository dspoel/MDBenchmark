#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/ethylenglycol/ethylenglycol255.0/melting-npt-y.trr -s /home/lschmidt/MELTING/ethylenglycol/ethylenglycol255.0/melting-npt-y.tpr -o rdf_255.xvg -b 761 -e 961 
