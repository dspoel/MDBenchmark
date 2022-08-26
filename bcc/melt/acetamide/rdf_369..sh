#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.trr -s /home/lschmidt/MELTING/acetamide/acetamide369.0/melting-npt-y.tpr -o rdf_369.xvg -b -198 -e 2 
