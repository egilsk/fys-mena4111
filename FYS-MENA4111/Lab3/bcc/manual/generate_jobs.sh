#!/bin/sh-f
for a in 2.9 3.0 3.1 3.2 3.3
do
mkdir a$a
sed s/3.1/$a/ POSCAR > a$a/POSCAR
cp INCAR KPOINTS POTCAR jobfile a$a/
cd a$a
sbatch jobfile
cd ..
done
