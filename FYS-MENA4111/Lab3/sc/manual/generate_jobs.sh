#!/bin/sh-f
for a in 2.4 2.5 2.6 2.7 2.8
do
mkdir a$a
sed s/2.6/$a/ POSCAR > a$a/POSCAR
cp INCAR KPOINTS POTCAR jobfile a$a/
cd a$a
sbatch jobfile
cd ..
done
