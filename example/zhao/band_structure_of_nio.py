import pymatgen as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from pymatgen import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter

import matplotlib.pyplot as plt



#The file "vasprun.xml" is in aim_data. Rename it after unzip.
run = BSVasprun("vasprun.xml", parse_projected_eigen=True)

bs = run.get_band_structure("KPOINTS")

print("number of bands", bs.nb_bands)
print("number of kpoints", len(bs.kpoints))

print(bs.is_metal())
print(bs.is_spin_polarized)

print(bs.bands)

print(bs.bands[Spin.up].shape)
print(bs.bands[Spin.down][9,:])


n=0

for kpoints,e in zip(bs.kpoints,bs.bands[Spin.down][9.:]):
    n += 1
    if n == 11:
        print("...")
        if 10 < n < 190:
            continue
            print("kx = %5.3f ky = %5.3f kz = %5.3f eps(k) = %8.4f" % (tuple(kpoints.frac_coords) + (e,)))










