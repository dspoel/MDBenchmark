#!/usr/bin/env python3

#SBATCH -t "2:00:00"
#SBATCH -n 1
#SBATCH -p CLUSTER-AMD

import os
import glob


for maindir in glob.glob("M*"):
    if not os.path.isdir(maindir):
       continue
    os.chdir(maindir)

    for subdir in glob.glob("[A-Z]*" ):
        os.chdir(subdir)
        if subdir in ["NNQQNY", "GNNQQNY", "NNFGAIL"]:
            temperature = 293
        elif subdir in ["VQIVYK", "GGVVIA"]:
            temperature = 291
        elif subdir in ["LYQLEN", "VEALYL"]:
            temperature = 310
        else:
            temperature = 298


            

        with open("../../../MDP/peptides/NPTP.mdp", "r") as original:
             original_c = original.read()
        
            
        with open("martini.sh", "w") as script:
            script.write(f"""#!/bin/bash
#SBATCH -p CLUSTER-AMD
#SBATCH -t 10:00:10
#SBATCH -c 16

cp ../../../MDP/peptides/NPTP.mdp .
echo -e "{original_c}\nref_t= {temperature}" > NPTP.mdp

cp ../../../MDP/peptides/EM.mdp .
cp ../../../MDP/peptides/EM100.mdp .
cp ../../../MDP/peptides/NPT100P.mdp .

gmx grompp  -c boxxx.pdb -f EM100.mdp -o EM100.tpr -r boxxx.pdb -p topol.top
gmx mdrun -nt 16 -s EM100.tpr -deffnm EM100 -c EM100.gro
echo -e "a  bb\nq" | gmx make_ndx -f EM.gro -o index.ndx
echo -e "bb"|gmx genrestr -f EM.gro -n index.ndx -o posre.itp -fc 1000 1000 1000
awk '/\[ system \]/{print "#ifdef POSRES\n#include \"posre.itp\"\n#endif"}1' topol.top > topol_new.top

gmx grompp  -c EM100.gro -f NPT100p.mdp -o NPT100_new.tpr -r EM100.gro -p topol_new.top -maxwarn 1
gmx mdrun -nt 16 -s NPT100_new.tpr -deffnm NPT100_new -c NPT100_new.gro

gmx grompp  -c NPT100_new.gro -f NPT100p.mdp -o NPT100.tpr -r NPT100_new.gro -p topol.top -maxwarn 1
gmx mdrun -nt 16 -s NPT100.tpr -deffnm NPT100 -c NPT100.gro



gmx grompp  -c boxxx.pdb -f EM.mdp -o EM.tpr -r boxxx.pdb -p topol.top
gmx mdrun -nt 16 -s EM.tpr -deffnm EM -c EM.gro
echo -e "a  bb\nq" | gmx make_ndx -f EM.gro -o index.ndx
echo -e "bb"|gmx genrestr -f EM.gro -n index.ndx -o posre.itp -fc 1000 1000 1000
awk '/\[ system \]/{print "#ifdef POSRES\n#include \"posre.itp\"\n#endif"}1' topol.top > topol_new.top

gmx grompp  -c EM.gro -f NPTP.mdp -o NPT_new.tpr -r EM.gro -p topol_new.top -maxwarn 1
gmx mdrun -nt 16 -s NPT_new.tpr -deffnm NPT_new -c NPT_new.gro

gmx grompp  -c NPT_new.gro -f NPTP.mdp -o NPT.tpr -r NPT_new.gro -p topol.top -maxwarn 1
gmx mdrun -nt 16 -s NPT.tpr -deffnm NPT -c NPT.gro

mkdir BR
cd BR
cp ../../../../MDP/peptides/NPTB.mdp .
echo -e "{original_c}\nref_t= {temperature}" > NPTB.mdp
cp ../../../../MDP/peptides/EM.mdp .
cp ../../../../MDP/peptides/EM100.mdp .
cp ../../../../MDP/peptides/NPTB100.mdp .

gmx grompp  -c ../boxxx.pdb -f EM100.mdp -o EM100.tpr -r ../boxxx.pdb -p ../topol.top
gmx mdrun -nt 16 -s EM100.tpr -deffnm EM100 -c EM100.gro
echo -e "a  bb\nq" | gmx make_ndx -f EM.gro -o index.ndx
echo -e "bb"|gmx genrestr -f EM.gro -n index.ndx -o posre.itp -fc 1000 1000 1000
awk '/\[ system \]/{print "#ifdef POSRES\n#include \"posre.itp\"\n#endif"}1' ../topol.top > topol_new.top

gmx grompp  -c EM100.gro -f NPTB100.mdp -o NPT100_new.tpr -r EM100.gro -p ../topol_new.top -maxwarn 1
gmx mdrun -nt 16 -s NPT100_new.tpr -deffnm NPT100_new -c NPT100_new.gro

gmx grompp  -c NPT100_new.gro -f NPTB100.mdp -o NPT100.tpr -r NPT100_new.gro -p ../topol.top -maxwarn 1
gmx mdrun -nt 16 -s NPT100.tpr -deffnm NPT100 -c NPT100.gro

gmx grompp  -c ../boxxx.pdb -f EM.mdp -o EM.tpr -r ../boxxx.pdb -p ../topol.top
gmx mdrun -nt 16 -s EM.tpr -deffnm EM -c EM.gro
echo -e "a  bb\nq" | gmx make_ndx -f EM.gro -o index.ndx
echo -e "bb"|gmx genrestr -f EM.gro -n index.ndx -o posre.itp -fc 1000 1000 1000
awk '/\[ system \]/{print "#ifdef POSRES\n#include \"posre.itp\"\n#endif"}1' ../topol.top > topol_new.top

gmx grompp  -c EM.gro -f NPTB.mdp -o NPT_new.tpr -r EM.gro -p ../topol_new.top -maxwarn 1
gmx mdrun -nt 16 -s NPT_new.tpr -deffnm NPT_new -c NPT_new.gro

gmx grompp  -c NPT_new.gro -f NPTB.mdp -o NPT.tpr -r NPT_new.gro -p ../topol.top -maxwarn 1
gmx mdrun -nt 16 -s NPT.tpr -deffnm NPT -c NPT.gro

""")

        os.system("chmod +x martini.sh")
        os.system("sbatch martini.sh")

        os.chdir("..")

    os.chdir("..")
