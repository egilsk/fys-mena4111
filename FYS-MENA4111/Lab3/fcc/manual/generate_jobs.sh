#!/bin/sh-f
for a in 3.8 3.9 4.0 4.1 4.2
do
mkdir a$a
sed s/4.0/$a/ POSCAR > a$a/POSCAR
cp INCAR KPOINTS POTCAR jobfile a$a/
cd a$a
sbatch jobfile
cd ..
done
