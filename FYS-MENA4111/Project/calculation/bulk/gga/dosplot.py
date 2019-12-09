#!/usr/bin/env python
#
# Plot the DOS from a VASP calculation.
# Written by Ole Martin Lovvik, 2018-09-20
# $LastChangedDate$
# $Rev$
#
# Please send bugs to ole.martin.lovvik@sintef.no
'''
Usage: dosplot.py [options] 

Plot the DOS or local DOS. The DOSCAR file has to be 
present.

Options:
  -h, --help          Show this help message and exit
  -l, --ldos atom     Prints the LDOS of the specified 
                      atom, the number corresponding to
                      its order in POSCAR.
'''

from __future__ import division
from __future__ import print_function

from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import os, glob, getopt
from subprocess import call

shopts = 'hl:s:'
longopts = ['help', 'ldos=', 'spin']

ldos = False
spin = False

try:
    opts, args = getopt.getopt(sys.argv[1:], shopts, longopts)
except getopt.GetoptError as err:
    # print help information and exit:
    print('{0}: {1}'.format(sys.argv[0], str(err)))
    print(__doc__)
    sys.exit(2)


for o, a in opts:
    if o in ('-h', '--help'):
        # print help information and exit:
        print(__doc__)
        sys.exit()
    elif o in ('-l', '--ldos'):
        if not a:
            print("Missing argument to --ldos")
            print(__doc__)
        atom = a
        ldos = True
    elif o in ('-s', '--spin'):
        spin = True
    else:
        print(__doc__)
        exit(1)

# Check if DOSCAR exists
try:
    os.path.isfile('DOSCAR')
except:
    print("DOSCAR file is not found")
    exit(1)

if not os.path.isfile('DOS0'):
    call('split_dos')

# Total DOS:
if not ldos:
    DOSdata = loadtxt('DOS0')#,usecols=(0,1))

    plot(DOSdata[:,0],DOSdata[:,1])

    xlim((-10,10))
    xlabel('$E - E_{Fermi}$ [eV]')
    ylabel('DOS [states/eV]')

    savefig('TDOS.png')

    show()

# Local DOS:
else:
    print("Atom number: "+atom)
    dosfile='DOS'+atom
    try:
        os.path.isfile(dosfile)
    except:
        print(dosfile+" is not found. Did you use LORBIT=11 in INCAR?")
        exit(1)
    try:
        DOSdata = loadtxt(dosfile)
    except:
        print("Trouble reading "+dosfile)
    if len(DOSdata[0])==10:
        plot(DOSdata[:,0],DOSdata[:,1],label='s')
        plot(DOSdata[:,0],DOSdata[:,2],label='p')
        plot(DOSdata[:,0],DOSdata[:,5],label='d')
    elif len(DOSdata[0])==4:
        plot(DOSdata[:,0],DOSdata[:,1],label='s')
        plot(DOSdata[:,0],DOSdata[:,2],label='p')
        plot(DOSdata[:,0],DOSdata[:,3],label='d')
    xlim((-10,10))
    ylim((-1,5))
    xlabel('$E - E_{Fermi}$ [eV]')
    ylabel('DOS [states/eV]')
    legend()
    suptitle('LDOS atom no '+atom)
    savefig('LDOS'+atom+'.png')

    show()


# Remove DOS[0-9]* files generated by split_dos
try:
    for a in glob.glob('DOS[0-9]*'): os.remove(a)
except:
    print("No DOS0 removed")
try:
    for a in glob.glob('tmp.dat*'): os.remove(a)
except:
    pass

exit()
