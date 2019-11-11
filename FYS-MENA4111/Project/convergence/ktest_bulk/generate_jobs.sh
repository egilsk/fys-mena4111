#!/bin/sh-f
for k in 1 2 3 4 5 6
do
mkdir k$k
cp INCAR POSCAR POTCAR jobfile k$k/
cd k$k
makekpoints -d $k
sbatch jobfile
cd ..
done
