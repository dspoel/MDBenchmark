#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rdf -sel 0 -ref 0 -dt 1 -f /home/lschmidt/MELTING/furan/furan127.0/melting-npt-y_ori.trr -s /home/lschmidt/MELTING/furan/furan127.0/melting-npt-y_ori.tpr -o rdf_127.xvg -b 1800 -e 2000 
