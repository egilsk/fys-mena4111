#!/bin/sh-f
for layer in 1 2 3 4 5 6 7
do
mkdir layer$layer
sed s/4/$layer/ make_slab.py > layer$layer/make_slab.py
cp INCAR KPOINTS POTCAR POSCAR_bulk jobfile layer$layer/
cd layer$layer
python make_slab.py
sbatch jobfile
cd ..
done
