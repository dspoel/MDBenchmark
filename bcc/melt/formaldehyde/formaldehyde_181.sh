#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
gmx rotacf -d -n ../../../index/formaldehyde_rotaxis.ndx -f /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.trr -s /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.tpr -o rotacf_181.xvg -b 0 -e 2000 
gmx rotacf -n ../../../index/formaldehyde_rotplane.ndx -f /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.trr -s /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.tpr -o rotplane_181.xvg -b 0 -e 2000 
echo 0 | gmx msd -f /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.trr -s /home/lschmidt/MELTING/formaldehyde/formaldehyde181.0/melting-npt.tpr -o msd_181.xvg -b 0 -e 2000 
