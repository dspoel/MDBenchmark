#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -p CLUSTER-AMD
#SBATCH -n 1
echo Potential | gmx energy -nmol 3400 -f /home/lschmidt/MELTING/123-benzenetriol/123-benzenetriol413.0/melting-npt-y.edr -o epot_413.xvg
