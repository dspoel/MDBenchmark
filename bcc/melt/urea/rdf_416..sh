#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/urea/urea416.0/melting-npt-y_4.trr -s /home/lschmidt/MELTING/urea/urea416.0/melting-npt-y_4.tpr -o rdf_416.xvg -b 1800 -e 2000 
