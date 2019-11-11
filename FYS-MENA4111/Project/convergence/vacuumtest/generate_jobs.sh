#!/bin/sh-f
for v in 1 2 3 4 5 6 7 8 9 10 11 12 13
do
mkdir v$v
sed s/6/$v/ make_slab.py > v$v/make_slab.py
cp INCAR KPOINTS POTCAR POSCAR_bulk jobfile v$v/
cd v$v
python make_slab.py
sbatch jobfile
cd ..
done
