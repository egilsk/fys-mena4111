#!/usr/bin/env python

from ase.io import read, vasp
from ase.build import sort, surface

unitcell = sort(read('POSCAR_bulk'))

slab = surface(unitcell, indices=(0,0,1), layers=4, vacuum=7)

vasp.write_vasp('POSCAR',sort(slab),vasp5=True,direct=True)