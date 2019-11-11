#!/bin/sh-f
for E in 400 450 500 550 600 650 700 750 800 850
do
mkdir E$E
sed s/400/$E/ INCAR > E$E/INCAR
cp POSCAR KPOINTS POTCAR jobfile E$E/
cd E$E
sbatch jobfile
cd ..
done
