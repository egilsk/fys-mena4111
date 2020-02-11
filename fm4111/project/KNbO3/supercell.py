#!/usr/bin/env python

from ase.io import read,vasp
from ase.utils.geometry import sort,cut
from numpy import sqrt

at0 = sort(read('POSCAR'))
sat0 = cut(at0,a=(1,0,-1),b=(0,2,0),c=(1,0,1))
vasp.write_vasp('POSCAR_super',sort(sat0),vasp5=True,direct=True)
