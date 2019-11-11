from __future__ import print_function
from collections import OrderedDict
import numpy as np
"""This module defines an ASE interface to SIESTA.

Written by Mads Engelund
http://www.mads-engelund.net

Home of the SIESTA package:
http://www.uam.es/departamentos/ciencias/fismateriac/siesta
"""
from ase.calculators.siesta.base_siesta import BaseSiesta
import ase.units as un


# Version 3.2 of Siesta
class Siesta3_2(BaseSiesta):
    allowed_xc = {
        'LDA': ['PZ', 'CA', 'PW92'],
        'GGA': ['PBE', 'revPBE', 'RPBE',
                'WC', 'PBEsol', 'LYP']}

    unit_fdf_keywords = {
        'PAO.EnergyShift': "eV",
        'BasisPressure': 'eV/Ang**3',
        'LatticeConstant': 'Ang',
        'ZM.UnitsLength': 'Ang',
        'WarningMiniumAtomicDistance': 'Ang',
        'MaxBondDistance': 'Ang',
        'kgrid_cutoff': 'Ang',
        'DM.EnergyTolerance': 'eV',
        'DM.HarrisTolerance': 'eV',
        'EggboxScale': 'eV',
        'ElectronicTemperature': 'eV',
        'OMM.TPreconScale': 'eV',
        'ON.eta': 'eV',
        'ON.eta_alpha': 'eV',
        'ON.eta_beta': 'eV',
        'ON.RcLWF': 'Ang',
        'ON.ChemicalPotentialRc': 'Ang',
        'ON.ChemicalPotentialTemperature': 'eV',
        'Optical.EnergyMinimum': 'eV',
        'Optical.EnergyMaximum': 'eV',
        'Optical.Broaden': 'eV',
        'Optical.Scissor': 'eV',
        'MD.MaxForceTol': 'eV/Ang',
        'MD.MaxStressTol': 'eV/Ang**3',
        'MD.MaxCGDispl': 'Ang',
        'MD.PreconditioningVariableCell': 'Ang',
        'ZM.ForceTolLength': 'eV/Ang',
        'ZM.ForceTolAngle': 'eV/rad',
        'ZM.MaxDiplLength': 'Ang',
        'MD.FIRE.TimeStep': 's',
        'MD.TargetPressure': 'eV/Ang**3',
        'MD.LengthTimeStep': 's',
        'MD.InitialTemperature': 'eV',
        'MD.TargetTemperature': 'eV',
        'MD.NoseMass': 'Kg*m**2',               # Not in ASE unit
        'MD.ParrinelloRahmanMass': 'Kg*m**2',   # Not in ASE unit
        'MD.TauRelax': 's',
        'MD.BulkModulus': 'eV/Ang**3',
        'MD.FCDispl': 'Ang'}

    allowed_fdf_keywords = OrderedDict([
        ('SystemName', "siesta"),
        ('SystemLabel', "siesta"),
        ('NumberOfSpecies', 0),
        ('NumberOfAtoms', 0),
        ('AtomicMass', 0),
        ('ChemicalSpeciesLabel', None),
        ('PAO.BasisSize', "DZP"),
        ('PAO.BasisSizes', None),
        ("PAO.EnergyShift", 0.02 / un.Ry),  # 0.02Ry
        ('PAO.BasisType', "split"),
        ('PAO.SplitNorm', 0.15),
        ('PAO.SplitNormH', 0.15),
        ('PAO.NewSplitCode', False),
        ('PAO.FixSplitTable', False),
        ('PAO.FixSplitTailNorm', False),
        ('PAO.SoftDefault', False),
        ('PAO.SoftInnerRadius', 0.9),
        ('PAO.SoftPotential', 40.0),  # Ry
        ('PS.lmax', None),
        ('PS.KBprojectors', None),
        ('FilterCutoff', None),
        ('FilterTol', None),
        ('User.Basis', False),
        ('User.Basis.NetCDF', False),
        ('BasisPressure', 0.2),  # GPa
        ('ReparametrizePseudos', False),
        ('New.A.Parameter', 0.001),
        ('New.B.Parameter', 0.01),
        ('Rmax.Radial.Grid', 50.0),
        ('Restricted.Radial.Grid', True),
        ('LatticeConstant', 1.0),  # Ang
        ('LatticeParameters', np.array([1.0, 1.0, 1.0,
                                       90.0, 90.0, 90.0])),
        ('LatticeVectors', np.array([[1.0, 0.0, 0.0],
                                     [0.0, 1.0, 0.0],
                                     [0.0, 0.0, 1.0]])),
        ('SuperCell', None),
        ('AtomicCoordinatesFormat', "Ang"),
        ('AtomicCoorFormatOut', "Ang"),
        ('AtomicCoordinatesOrigin', np.array([0.0, 0.0, 0.0])),
        ('AtomicCoordinatesAndAtomicSpecies', None),
        ('Zmatrix', None),
        ('ZM.UnitsLength', "Ang"),
        ('ZM.UnitsAngle', "rad"),
        ('WriteCoorXmol', False),
        ('WriteCoorCerius', False),
        ('WriteMDXmol', False),
        ('WarningMiniumAtomicDistance', 1.0),  # Bohr
        ('MaxBondDistance', 6.0),  # Bohr
        ('kgrid_cutoff', 0.0),  # Bohr
        ('kgrid_Monkhorst_Pack', None),
        ('ChangeKgridInMD', False),
        ('TimeReversalSymmetryForKpoints', True),
        ('WriteKpoints', False),
        ('XC.functional', "LDA"),
        ('XC.authors', "PZ"),
        ('XC.hydrid', None),
        ('SpinPolarized', False),
        ('NonCollinearSpin', False),
        ('FixSpin', False),
        ('TotalSpin', 0.0),
        ('SingleExcitation', False),
        ('Harris_functional', False),
        ('MaxSCFIterations', 50),
        ('SCFMustConverge', False),
        ('DM.MixingWeight', 0.25),
        ('DM.NumberPulay', 0),
        ('DM.Pulay.Avoid.First.After.Kick', False),
        ('DM.NumberBroyden', 0),
        ('DM.Broyden.Cycle.On.Maxit', True),
        ('DM.NumberKick', 0),
        ('DM.KickMixingWeight', 0.50),
        ('DM.MixSCF1', False),
        ('DM.UseSaveDM', False),
        ('DM.FormattedFiles', False),
        ('DM.FormattedInput', False),
        ('DM.FormattedOutput', False),
        ('DM.InitSpinAF', False),
        ('DM.InitSpin', None),
        ('DM.AllowReuse', True),
        ('DM.AllowExtrapolation', True),
        ('SCF.Read.Charge.NetCDF', False),
        ('SCF.ReadDeformation.Charge.NetCDF', False),
        ('WriteDM', True),
        ('WriteDM.NetCDF', False),
        ('WrireDMHS.NetCDF', False),
        ('WriteDM.History.NetCDF', False),
        ('WrireDMHS.History.NetCDF', False),
        ('DM.Tolerance', 1E-4),
        ('DM.Require.Energy.Convergence', False),
        ('DM.EnergyTolerance', 1E-4),  # eV
        ('DM.Require.Harris.Convergence', False),
        ('DM.Harris.Tolerance', 1E-4),  # eV
        ('MeshCutoff', 100),  # Ry
        ('MeshSubDivisions', 2),
        ('GridCellSampling', None),
        ('EggboxRemove', None),
        ('EggboxScale', 1.0),  # eV
        ('NeglNonOverlapInt', False),
        ('SaveHS', False),
        ('FixAuxiliaryCell', False),
        ('NaiveAuxiliaryCell', False),
        ('SolutionMethod', "diagon"),
        ('NumberOfEigenStates', 0),
        ('Use.New.Diagk', False),
        ('Diag.DivideAndConquer', True),
        ('Diag.AllInOne', False),
        ('Diag.NoExpert', False),
        ('Diag.PreRotate', False),
        ('Diag.Use2D', True),
        ('WriteEigenvalues', False),
        ('OccupationFunction', "FD"),
        ('OccupationMPOrder', 1),
        ('ElectronicTemperature', 300.0),  # K pp
        ('ON.functional', "Kim"),
        ('ON.MaxNumIter', 1000),
        ('ON.etol', 1E-8),
        ('ON.eta', 0.0),  # eV
        ('ON.eta_alpha', 0.0),  # eV
        ('ON.eta_beta', 0.0),  # eV
        ('ON.RcLWF', 9.5),  # Bohr
        ('ON.ChemicalPotential', False),
        ('ON.ChemicalPotentialUse', False),
        ('ON.ChemicalPotentialRc', 9.5),  # Bohr
        ('ON.ChemicalPotentialTemperature', 0.05),  # Ry
        ('ON.ChemicalPotentialOrder', 100),
        ('ON.LowerMemory', False),
        ('ON.UseSaveLWF', False),
        ('BandLinesScale', None),  # by default pi/a (a: lattice constant)
        ('BandLines', None),
        ('BandPoints', None),
        ('WriteKbands', False),
        ('WriteBands', False),
        ('WFS.Write.For.Bands', False),
        ('WFS.Band.Min', 1),
        ('WFS.Band.Max', 0),  # default number of orbital
        ('WaveFuncPointScale', None),  # by default pi/a (a: lattice constant)
        ('WaveFuncKPoints', None),
        ('WriteWaveFunctions', False),
        ('ProjectedDensityOfStates', None),
        ('LocalDensityOfStates', None),
        ('WriteMullikenPop', 0),
        ('MullikenInSCF', False),
        ('WriteHirshfeldPop', False),
        ('WriteVoronoiPop', False),
        ('PartialChargesAtEveryGeometry', False),
        ('PartialChargesAtEveryScfStep', False),
        ('COOP.Write', False),
        ('WFS.Energy.Min', None),  # default -\infty
        ('WFS.Energy.Max', None),  # default +\infty
        ('WFS.Band.Min', 1),
        ('WFS.Band.Max', 0),  # default the number of orbitals
        ('OpticalCalculation', False),
        ('Optical.EnergyMinimum', 0.0),  # Ry
        ('Optical.EnergyMaximum', 10.0),  # Ry
        ('Optical.Broaden', 0.0),  # Ry
        ('Optical.Scissor', 0.0),  # Ry
        ('Optical.NumberOfBands', 0),  # default all bands
        ('Optical.Mesh', None),
        ('Optical.OffsetMesh', False),
        ('Optical.PolarizationType', "polycrystal"),
        ('Optical.Vector', None),
        ('PolarizationGrids', None),
        ('BornCharge', False),
        ('NetCharge', 0.0),
        ('SimulateDoping', False),
        ('ExternalElectricField', None),
        ('SlabDipoleCorrection', False),
        ('LongOutput', False),
        ('MD.UseSaveXV', False),
        ('MD.UseSaveCG', False),
        ('SaveRho', False),
        ('SaveDeltaRho', False),
        ('SaveElectrostaticPotential', False),
        ('SaveNeutralAtomPotential', False),
        ('SaveTotalPotential', False),
        ('SaveIonicCharge', False),
        ('SaveTotalCharge', False),
        ('SaveBaderCharge', False),
        ('SaveInitialChargeDensity', False),
        ('MM.Potentials', None),
        ('MM.Cutoff', 30.0),  # Bohr
        ('MM.UnitsEnergy', "eV"),
        ('MM.UnitsDistance', "Ang"),
        ('MM.Grimme.D', 20.0),
        ('MM.Grimme.S6', 1.66),
        ('BlockSize', 8),
        ('ProcessorY', 0),  # default depend the number of cpus
        ('Diag.Memory', 1.0),
        ('Diag.ParallelOverK', False),
        ('UseDomainDecomposition', False),
        ('UseSpatialDecomposition', False),
        ('RcSpatial', 0.0),  # max of the matrix element range
        ('DirectPhi', False),
        ('AllocReportLevel', 0),
        ('UseSaveData', False),
        ('WriteDenchar', False),
        ('MD.TypeOfRun', "Verlet"),
        ('MD.VariableCell', False),
        ('MD.ConstantVolume', False),
        ('MD.RelaxCellOnly', False),
        ('MD.MaxForceTol', 0.04),  # eV/Ang
        ('MD.MaxStressTol', 1.0),  # GPa
        ('MD.NumCGsteps', 0),
        ('MD.MaxCGDispl', 0.2),  # Bohr
        ('MD.PreconditioningVariableCell', 5.0),  # Ang
        ('ZM.ForceTolLength', 0.00155),  # Ry/Bohr
        ('ZM.ForceTolAngle', 0.0035),  # Ry/Rad
        ('ZM.MaxDiplLength', 0.2),  # Bohr
        ('ZM.MaxDiplAngle', 0.003),  # rad
        ('MD.UseSaveCG', False),
        ('MD.Broyden.History.Steps', 5),
        ('MD.Broyden.Cycle.On.Maxit', True),
        ('MD.Broyden.Initial.Inverse.Jacobian', 1.0),
        ('MD.FIRE.TimeStep', 0.0),  # ??
        ('MD.Quench', False),
        ('MD.FireQuench', False),
        ('MD.TargetPressure', 0.0),  # GPa
        ('MD.TargetStress', None),
        ('MD.RemoveIntramolecularPressure', False),
        ('MD.InitialTimeStep', 1),
        ('MD.FinalTimestep', 1),
        ('MD.LengthTimeStep', 1.0),  # fs
        ('MD.InitialTemperature', 0.0),  # K
        ('MD.TargetTemperature', 0.0),  # K
        ('MD.NoseMass', 100.0),  # Ry.fs^2
        ('MD.ParrinelloRahmanMass', 100.0),  # Ry.fs^{2}
        ('MD.AnnealOption', 0.0),
        ('MD.TauRelax', 100.0),  # fs
        ('MD.BulkModulus', 100.0),  # Ry/Bohr^{3}
        ('Master.code', 'fsiesta'),
        ('Master.interface', 'pipes'),
        ('Master.address', 'localhost'),  # or IP address
        ('Master.port', 10001),
        ('Master.socketType', 'inet'),
        ('WriteCoorInitial', True),
        ('WriteCoorStep', False),
        ('WriteForces', False),
        ('WriteMDhistory', False),
        ('XML.Write', False),
        ('GeometryConstraints', None),
        ('MD.FCDispl', 0.04),  # Bohr
        ('MD.FCfirst', 1),
        ('MD.FClast', 0),
        ('PhononLabels', None),
        ('MD.ATforPhonon', None)])


# Trunk version, snapshot 462
class SiestaTrunk462(BaseSiesta):
    allowed_xc = {
        'LDA': ['PZ', 'CA', 'PW92'],
        'GGA': ['PW91', 'PBE', 'revPBE', 'RPBE',
                'WC', 'AM05', 'PBEsol', 'PBEJsJrLO',
                'PBEGcGxLO', 'PBEGcGxHEG', 'BLYP'],
        'VDW': ['DRSLL', 'LMKLL', 'KBM', 'C09', 'BH', 'VV']}
    unit_fdf_keywords = {
        'BasisPressure': 'eV/Ang**3',
        'LatticeConstant': 'Ang',
        'ZM.UnitsLength': 'Ang',
        'WarningMiniumAtomicDistance': 'Ang',
        'MaxBondDistance': 'Ang',
        'kgrid_cutoff': 'Ang',
        'DM.EnergyTolerance': 'eV',
        'DM.HarrisTolerance': 'eV',
        'EggboxScale': 'eV',
        'ElectronicTemperature': 'eV',
        'ON.eta': 'eV',
        'ON.eta_alpha': 'eV',
        'ON.eta_beta': 'eV',
        'ON.RcLWF': 'Ang',
        'ON.ChemicalPotentialRc': 'Ang',
        'ON.ChemicalPotentialTemperature': 'eV',
        'Optical.EnergyMinimum': 'eV',
        'Optical.EnergyMaximum': 'eV',
        'Optical.Broaden': 'eV',
        'Opticalcissor': 'eV',
        'MD.MaxForceTol': 'eV/Ang',
        'MD.MaxStressTol': 'eV/Ang**3',
        'MD.MaxCGDispl': 'Ang',
        'MD.PreconditioningVariableCell': 'Ang',
        'ZM.ForceTolLength': 'eV/Ang',
        'ZM.ForceTolAngle': 'eV/rad',
        'ZM.MaxDiplLength': 'Ang',
        'MD.FIRE.TimeStep': 's',
        'MD.TargetPressure': 'eV/Ang**3',
        'MD.LengthTimeStep': 's',
        'MD.InitialTemperature': 'eV',
        'MD.TargetTemperature': 'eV',
        'MD.NoseMass': 'Kg*m**2',               # Not in ASE unit
        'MD.ParrinelloRahmanMass': 'Kg*m**2',   # Not in ASE unit
        'MD.TauRelax': 's',
        'MD.BulkModulus': 'eV/Ang**3',
        'MD.FCDispl': 'Ang'}

    allowed_fdf_keywords = OrderedDict([
        ('SystemName', "siesta"),
        ('SystemLabel', "siesta"),
        ('NumberOfSpecies', 0),
        ('NumberOfAtoms', 0),
        ('AtomicMass', 0),
        ('ChemicalSpeciesLabel', None),
        ('PAO.BasisSize', "DZP"),
        ('PAO.BasisSizes', None),
        ('PAO.BasisType', "split"),
        ('PAO.SplitNorm', 0.15),
        ('PAO.SplitNormH', 0.15),
        ('PAO.NewSplitCode', False),
        ('PAO.FixSplitTable', False),
        ('PAO.FixSplitTailNorm', False),
        ('PAO.SoftDefault', False),
        ('PAO.SoftInnerRadius', 0.9),
        ('PAO.SoftPotential', 40.0),  # Ry
        ('PS.lmax', None),
        ('PS.KBprojectors', None),
        ('FilterCutoff', None),
        ('FilterTol', None),
        ('User.Basis', False),
        ('User.Basis.NetCDF', False),
        ('BasisPressure', 0.2),  # GPa
        ('ReparametrizePseudos', False),
        ('New.A.Parameter', 0.001),
        ('New.B.Parameter', 0.01),
        ('Rmax.Radial.Grid', 50.0),
        ('Restricted.Radial.Grid', True),
        ('LatticeConstant', 1.0),  # Ang
        ('LatticeParameters', np.array([1.0, 1.0, 1.0,
                                       90.0, 90.0, 90.0])),
        ('LatticeVectors', np.array([[1.0, 0.0, 0.0],
                                     [0.0, 1.0, 0.0],
                                     [0.0, 0.0, 1.0]])),
        ('SuperCell', None),
        ('AtomicCoordinatesFormat', "Ang"),
        ('AtomicCoorFormatOut', "Ang"),
        ('AtomicCoordinatesOrigin', np.array([0.0, 0.0, 0.0])),
        ('AtomicCoordinatesAndAtomicSpecies', None),
        ('Zmatrix', None),
        ('ZM.UnitsLength', "Ang"),
        ('ZM.UnitsAngle', "rad"),
        ('WriteCoorXmol', False),
        ('WriteCoorCerius', False),
        ('WriteMDXmol', False),
        ('WarningMiniumAtomicDistance', 1.0),  # Bohr
        ('MaxBondDistance', 6.0),  # Bohr
        ('kgrid_cutoff', 0.0),  # Bohr
        ('kgrid_Monkhorst_Pack', None),
        ('ChangeKgridInMD', False),
        ('TimeReversalSymmetryForKpoints', True),
        ('WriteKpoints', False),
        ('XC.functional', "LDA"),
        ('XC.authors', "PZ"),
        ('XC.hydrid', None),
        ('SpinPolarised', False),
        ('NonCollinearSpin', False),
        ('FixSpin', False),
        ('TotalSpin', 0.0),
        ('SingleExcitation', False),
        ('Harris_functional', False),
        ('MaxSCFIterations', 50),
        ('SCFMustConverge', False),
        ('DM.MixingWeight', 0.25),
        ('DM.NumberPulay', 0),
        ('DM.Pulay.Avoid.First.After.Kick', False),
        ('DM.NumberBroyden', 0),
        ('DM.Broyden.Cycle.On.Maxit', True),
        ('DM.NumberKick', 0),
        ('DM.KickMixingWeight', 0.50),
        ('DM.MixSCF1', False),
        ('DM.UseSaveDM', False),
        ('DM.FormattedFiles', False),
        ('DM.FormattedInput', False),
        ('DM.FormattedOutput', False),
        ('DM.InitSpinAF', False),
        ('DM.InitSpin', None),
        ('DM.AllowReuse', True),
        ('DM.AllowExtrapolation', True),
        ('SCF.Read.Charge.NetCDF', False),
        ('SCF.ReadDeformation.Charge.NetCDF', False),
        ('WriteDM', True),
        ('WriteDM.NetCDF', False),
        ('WrireDMHS.NetCDF', False),
        ('WriteDM.History.NetCDF', False),
        ('WrireDMHS.History.NetCDF', False),
        ('DM.Tolerance', 1E-4),
        ('DM.Require.Energy.Convergence', False),
        ('DM.EnergyTolerance', 1E-4),  # eV
        ('DM.Require.Harris.Convergence', False),
        ('DM.Harris.Tolerance', 1E-4),  # eV
        ('MeshCutoff', 100),  # Ry
        ('MeshSubDivisions', 2),
        ('GridCellSampling', None),
        ('EggboxRemove', None),
        ('EggboxScale', 1.0),  # eV
        ('NeglNonOverlapInt', False),
        ('SaveHS', False),
        ('FixAuxiliaryCell', False),
        ('NaiveAuxiliaryCell', False),
        ('SolutionMethod', "diagon"),
        ('NumberOfEigenStates', 0),
        ('Use.New.Diagk', False),
        ('Diag.DivideAndConquer', True),
        ('Diag.AllInOne', False),
        ('Diag.NoExpert', False),
        ('Diag.PreRotate', False),
        ('Diag.Use2D', True),
        ('WriteEigenvalues', False),
        ('OccupationFunction', "FD"),
        ('OccupationMPOrder', 1),
        ('ElectronicTemperature', 300.0),  # K pp
        ('ON.functional', "Kim"),
        ('ON.MaxNumIter', 1000),
        ('ON.etol', 1E-8),
        ('ON.eta', 0.0),  # eV
        ('ON.eta_alpha', 0.0),  # eV
        ('ON.eta_beta', 0.0),  # eV
        ('ON.RcLWF', 9.5),  # Bohr
        ('ON.ChemicalPotential', False),
        ('ON.ChemicalPotentialUse', False),
        ('ON.ChemicalPotentialRc', 9.5),  # Bohr
        ('ON.ChemicalPotentialTemperature', 0.05),  # Ry
        ('ON.ChemicalPotentialOrder', 100),
        ('ON.LowerMemory', False),
        ('ON.UseSaveLWF', False),
        ('BandLinesScale', None),  # by default pi/a (a: lattice constant)
        ('BandLines', None),
        ('BandPoints', None),
        ('WriteKbands', False),
        ('WriteBands', False),
        ('WFS.Write.For.Bands', False),
        ('WFS.Band.Min', 1),
        ('WFS.Band.Max', 0),  # default number of orbital
        ('WaveFuncPointScale', None),  # by default pi/a (a: lattice constant)
        ('WaveFuncKPoints', None),
        ('WriteWaveFunctions', False),
        ('ProjectedDensityOfStates', None),
        ('LocalDensityOfStates', None),
        ('WriteMullikenPop', 0),
        ('MullikenInSCF', False),
        ('WriteHirshfeldPop', False),
        ('WriteVoronoiPop', False),
        ('PartialChargesAtEveryGeometry', False),
        ('PartialChargesAtEveryScfStep', False),
        ('COOP.Write', False),
        ('WFS.Energy.Min', None),  # default -\infty
        ('WFS.Energy.Max', None),  # default +\infty
        ('WFS.Band.Min', 1),
        ('WFS.Band.Max', 0),  # default the number of orbitals
        ('OpticalCalculation', False),
        ('Optical.EnergyMinimum', 0.0),  # Ry
        ('Optical.EnergyMaximum', 10.0),  # Ry
        ('Optical.Broaden', 0.0),  # Ry
        ('Optical.Scissor', 0.0),  # Ry
        ('Optical.NumberOfBands', 0),  # default all bands
        ('Optical.Mesh', None),
        ('Optical.OffsetMesh', False),
        ('Optical.PolarizationType', "polycrystal"),
        ('Optical.Vector', None),
        ('PolarizationGrids', None),
        ('BornCharge', False),
        ('NetCharge', 0.0),
        ('SimulateDoping', False),
        ('ExternalElectricField', None),
        ('SlabDipoleCorrection', False),
        ('LongOutput', False),
        ('MD.UseSaveXV', False),
        ('MD.UseSaveCG', False),
        ('SaveRho', False),
        ('SaveDeltaRho', False),
        ('SaveElectrostaticPotential', False),
        ('SaveNeutralAtomPotential', False),
        ('SaveTotalPotential', False),
        ('SaveIonicCharge', False),
        ('SaveTotalCharge', False),
        ('SaveBaderCharge', False),
        ('SaveInitialChargeDensity', False),
        ('MM.Potentials', None),
        ('MM.Cutoff', 30.0),  # Bohr
        ('MM.UnitsEnergy', "eV"),
        ('MM.UnitsDistance', "Ang"),
        ('MM.Grimme.D', 20.0),
        ('MM.Grimme.S6', 1.66),
        ('BlockSize', 8),
        ('ProcessorY', 0),  # default depend the number of cpus
        ('Diag.Memory', 1.0),
        ('Diag.ParallelOverK', False),
        ('UseDomainDecomposition', False),
        ('UseSpatialDecomposition', False),
        ('RcSpatial', 0.0),  # max of the matrix element range
        ('DirectPhi', False),
        ('AllocReportLevel', 0),
        ('UseSaveData', False),
        ('WriteDenchar', False),
        ('MD.TypeOfRun', "Verlet"),
        ('MD.VariableCell', False),
        ('MD.ConstantVolume', False),
        ('MD.RelaxCellOnly', False),
        ('MD.MaxForceTol', 0.04),  # eV/Ang
        ('MD.MaxStressTol', 1.0),  # GPa
        ('MD.NumCGsteps', 0),
        ('MD.MaxCGDispl', 0.2),  # Bohr
        ('MD.PreconditioningVariableCell', 5.0),  # Ang
        ('ZM.ForceTolLength', 0.00155),  # Ry/Bohr
        ('ZM.ForceTolAngle', 0.0035),  # Ry/Rad
        ('ZM.MaxDiplLength', 0.2),  # Bohr
        ('ZM.MaxDiplAngle', 0.003),  # rad
        ('MD.UseSaveCG', False),
        ('MD.Broyden.History.Steps', 5),
        ('MD.Broyden.Cycle.On.Maxit', True),
        ('MD.Broyden.Initial.Inverse.Jacobian', 1.0),
        ('MD.FIRE.TimeStep', 0.0),  # ??
        ('MD.Quench', False),
        ('MD.FireQuench', False),
        ('MD.TargetPressure', 0.0),  # GPa
        ('MD.TargetStress', None),
        ('MD.RemoveIntramolecularPressure', False),
        ('MD.InitialTimeStep', 1),
        ('MD.FinalTimestep', 1),
        ('MD.LengthTimeStep', 1.0),  # fs
        ('MD.InitialTemperature', 0.0),  # K
        ('MD.TargetTemperature', 0.0),  # K
        ('MD.NoseMass', 100.0),  # Ry.fs^2
        ('MD.ParrinelloRahmanMass', 100.0),  # Ry.fs^2
        ('MD.AnnealOption', 0.0),
        ('MD.TauRelax', 100.0),  # fs
        ('MD.BulkModulus', 100.0),  # Ry/Bohr^{3}
        ('WriteCoorInitial', True),
        ('WriteCoorStep', False),
        ('WriteForces', False),
        ('WriteMDhistory', False),
        ('XML.Write', False),
        ('GeometryConstraints', None),
        ('MD.FCDispl', 0.04),  # Bohr
        ('MD.FCfirst', 1),
        ('MD.FClast', 0),
        ('PhononLabels', None),
        ('MD.ATforPhonon', None)])
#
#
#    allowed_fdf_keywords = OrderedDict([
#        ('SystemName',),
#        ('SystemLabel',),
#        ('MD.UseSaveXV',),
#        ('MD.UseSaveCG',),
#        ('LongOutput',),
#        ('NumberOfSpecies',),
#        ('NumberOfAtoms',),
#        ('ChemicalSpeciesLabel',),
#        ('AtomicMass',),
#        ('PAO.BasisType',),
#        ('PAO.SplitNorm',),
#        ('PAO.SplitNormH',),
#        ('PAO.NewSplitCode',),
#        ('PAO.FixSplitTable',),
#        ('PAO.FixSplitTailNorm',),
#        ('PAO.EnergyCutoff',),
#        ('PAO.EnergyPolCutoff',),
#        ('PAO.EnergyContractionCutoff',),
#        ('PAO.SoftDefault',),
#        ('PAO.SoftInnerRadius',),
#        ('PAO.SoftPotential',),
#        ('PS.lmax',),
#        ('PS.KBprojectors',),
#        ('KB.New.Reference.Orbitals',),
#        ('PAO.Basis',),
#        ('FilterCutoff',),
#        ('FilterTol',),
#        ('User.Basis',),
#        ('User.Basis.NetCDF',),
#        ('BasisPressure',),
#        ('ReparametrizePseudos',),
#        ('New.A.Parameter',),
#        ('New.B.Parameter',),
#        ('Rmax.Radial.Grid',),
#        ('Restricted.Radial.Grid',),
#        ('LatticeConstant',),
#        ('LatticeParameters',),
#        ('LatticeVectors',),
#        ('SuperCell',),
#        ('AtomicCoordinatesFormat',),
#        ('AtomicCoorFormatOut',),
#        ('AtomicCoordinatesOrigin',),
#        ('AtomicCoordinatesAndAtomicSpecies',),
#        ('Zmatrix',),
#        ('ZM.UnitsLength',),
#        ('ZM.UnitsAngle',),
#        ('WriteCoorXmol',),
#        ('WriteCoorCerius',),
#        ('WriteMDXmol',),
#        ('WarningMiniumAtomicDistance',),
#        ('MaxBondDistance',),
#        ('kgrid_cutoff',),
#        ('kgrid_Monkhorst_Pack',),
#        ('ChangeKgridInMD',),
#        ('TimeReversalSymmetryForKpoints',),
#        ('WriteKpoints',),
#        ('XC.functional',),
#        ('XC.authors',),
#        ('XC.hydrid',),
#        ('SpinPolarised',),
#        ('NonCollinearSpin',),
#        ('FixSpin',),
#        ('TotalSpin',),
#        ('SingleExcitation',),
#        ('Harris_functional',),
#        ('MinSCFIterations',),
#        ('MaxSCFIterations',),
#        ('SCFMustConverge',),
#        ('MixHamiltonian',),
#        ('DM.MixSCF1',),
#        ('SCF.MixAfterConvergence',),
#        ('DM.MixingWeight',),
#        ('DM.NumberPulay',),
#        ('SCF.PulayDamping',),
#        ('SCF.PulayMinimumHistory',),
#        ('SCF.PulayDmaxRegion',),
#        ('DM.NumberKick',),
#        ('DM.KickMixingWeight',),
#        ('DM.Pulay.Avoid.First.After.Kick',),
#        ('SCF.LinearMixingAfterPulay',),
#        ('SCF.MixingWeightAfterPulay',),
#        ('SCF.Pulay.UseSVD',),
#        ('SCF.Pulay.DebugSVD',),
#        ('SCF.Pulay.RcondSVD',),
#        ('DM.PulayOnFile',),
#        ('DM.NumberBroyden',),
#        ('DM.Broyden.Cycle.On.Maxit',),
#        ('DM.Broyden.Variable.Weight',),
#        ('MixCharge',),
#        ('SCF.Kerker.q0sq',),
#        ('SCF.RhoGMixingCutoff',),
#        ('SCF.RhoG.DIIS.Depth',),
#        ('SCF.RhoG.Metric.Preconditioner.Cutoff',),
#        ('SCF.DebugRhogMixing',),
#        ('DebugDIIS',),
#        ('SCF.MixCharge.SCF1',),
#        ('DM.UseSaveDM',),
#        ('DM.FormattedFiles',),
#        ('DM.FormattedInput',),
#        ('DM.FormattedOutput',),
#        ('DM.InitSpinAF',),
#        ('DM.InitSpin',),
#        ('DM.AllowReuse',),
#        ('DM.AllowExtrapolation',),
#        ('SCF.Read.Charge.NetCDF',),
#        ('SCF.ReadDeformation.Charge.NetCDF',),
#        ('WriteDM',),
#        ('WriteDM.NetCDF',),
#        ('WrireDMHS.NetCDF',),
#        ('WriteDM.History.NetCDF',),
#        ('WrireDMHS.History.NetCDF',),
#        ('DM.Tolerance',),
#        ('DM.Require.Energy.Convergence',),
#        ('DM.EnergyTolerance',),
#        ('DM.Require.Harris.Convergence',),
#        ('DM.Harris.Tolerance',),
#        ('MeshCutoff',),
#        ('MeshSubDivisions'
#        ('GridCellSampling',),
#        ('EggboxRemove',),
#        ('EggboxScale',),
#        ('NeglNonOverlapInt',),
#        ('SaveHS',),
#        ('FixAuxiliaryCell',),
#        ('NaiveAuxiliaryCell',),
#        ('SolutionMethod',),
#        ('NumberOfEigenStates',),
#        ('Use.New.Diagk',),
#        ('Diag.DivideAndConquer',),
#        ('Diag.AllInOne',),
#        ('Diag.NoExpert',),
#        ('Diag.PreRotate',),
#        ('Diag.Use2D',),
#        ('WriteEigenvalues',),
#        ('OccupationFunction',),
#        ('OccupationMPOrder',),
#        ('ElectronicTemperature',),
#        ('ON.functional',),
#        ('ON.MaxNumIter',),
#        ('ON.etol',),
#        ('ON.eta',),
#        ('ON.eta_alpha',),
#        ('ON.eta_beta',),
#        ('ON.RcLWF',),
#        ('ON.ChemicalPotential',),
#        ('ON.ChemicalPotentialUse',),
#        ('ON.ChemicalPotentialRc',),
#        ('ON.ChemicalPotentialTemperature',),
#        ('ON.ChemicalPotentialOrder',),
#        ('ON.LowerMemory',),
#        ('ON.UseSaveLWF',),
#        ('BandLinesScale',),
#        ('BandLines',),
#        ('BandPoints',),
#        ('WriteKbands',),
#        ('WriteBands',),
#        ('WFS.Write.For.Bands',),
#        ('WFS.Band.Min',),
#        ('WFS.Band.Max',),
#        ('WaveFuncPointScale',),
#        ('WaveFuncKPoints',),
#        ('WriteWaveFunctions',),
#        ('ProjectedDensityOfStates',),
#        ('LocalDensityOfStates',),
#        ('WriteMullikenPop',),
#        ('MullikenInSCF',),
#        ('WriteHirshfeldPop',),
#        ('WriteVoronoiPop',),
#        ('PartialChargesAtEveryGeometry',),
#        ('PartialChargesAtEveryScfStep',),
#        ('COOP.Write',),
#        ('WFS.Energy.Min',),
#        ('WFS.Energy.Max',),
#        ('OpticalCalculation',),
#        ('Optical.EnergyMinimum',),
#        ('Optical.EnergyMaximum',),
#        ('Optical.Broaden',),
#        ('Optical.Scissor',),
#        ('Optical.NumberOfBands',),
#        ('Optical.Mesh',),
#        ('Optical.OffsetMesh',),
#        ('Optical.PolarizationType',),
#        ('Optical.Vector',),
#        ('PolarizationGrids',),
#        ('BornCharge',),
#        ('NetCharge',),
#        ('SimulateDoping',),
#        ('ExternalElectricField',),
#        ('SlabDipoleCorrection',),
#        ('SaveRho',),
#        ('SaveDeltaRho',),
#        ('SaveElectrostaticPotential',),
#        ('SaveNeutralAtomPotential',),
#        ('SaveBaderCharge',),
#        ('SaveInitialChargeDensity',),
#        ('MM.Potentials',),
#        ('MM.Cutoff',),
#        ('MM.UnitsEnergy',),
#        ('MM.UnitsDistance',),
#        ('MM.Grimme.D',),
#        ('MM.Grimme.S6',),
#        ('BlockSize'
#        ('ProcessorY',),
#        ('Diag.Memory',),
#        ('Diag.ParallelOverK',),
#        ('UseDomainDecomposition',),
#        ('UseSpatialDecomposition',),
#        ('RcSpatial',),
#        ('DirectPhi',),
#        ('AllocReportLevel',),
#        ('UseSaveData',),
#        ('WriteDenchar',),
#        ('MD.TypeOfRun',),
#        ('MD.VariableCell',),
#        ('MD.ConstantVolume',),
#        ('MD.RelaxCellOnly',),
#        ('MD.MaxForceTol',),
#        ('MD.MaxStressTol',),
#        ('MD.NumCGsteps',),
#        ('MD.MaxCGDispl',),
#        ('MD.PreconditioningVariableCell',),
#        ('ZM.ForceTolLength',),
#        ('ZM.ForceTolAngle',),
#        ('ZM.MaxDiplLength',),
#        ('ZM.MaxDiplAngle',),
#        ('MD.UseSaveCG',),
#        ('MD.Broyden.History.Steps',),
#        ('MD.Broyden.Cycle.On.Maxit',),
#        ('MD.Broyden.Initial.Inverse.Jacobian',),
#        ('MD.FIRE.TimeStep',),
#        ('MD.Quench',),
#        ('MD.FireQuench',),
#        ('MD.TargetPressure',),
#        ('MD.TargetStress',),
#        ('MD.RemoveIntramolecularPressure',),
#        ('MD.InitialTimeStep',),
#        ('MD.FinalTimestep',),
#        ('MD.LengthTimeStep',),
#        ('MD.InitialTemperature',),
#        ('MD.TargetTemperature',),
#        ('MD.NoseMass',),
#        ('MD.ParrinelloRahmanMass',),
#        ('MD.AnnealOption',),
#        ('MD.TauRelax',),
#        ('MD.BulkModulus',),
#        ('WriteCoorInitial',),
#        ('WriteCoorStep',),
#        ('WriteForces',),
#        ('WriteMDhistory',),
#        ('GeometryConstraints',),
#        ('MD.FCDispl',),
#        ('MD.FCfirst',),
#        ('MD.FClast',),
#        ('PhononLabels',),
#        ('MD.ATforPhonon')]),


# Define the default siesta version.
Siesta = Siesta3_2
