from pymatgen import Molecule

coords = [[0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 1.089000],
          [1.026719, 0.000000, -0.363000],
          [-0.513360, -0.889165, -0.363000],
          [-0.513360, 0.889165, -0.363000]]
mol = Molecule(["C", "H", "H", "H", "H"], coords)
print(mol)
print(mol[0])
print(mol[1])
for frag in mol.break_bond(0, 1):
    print(frag)
print(mol.get_neighbors(mol[0], 3))
print(mol.get_covalent_bonds())
structure = mol.get_boxed_structure(10, 10, 10)
print(structure)
from pymatgen.io.xyz import XYZ
xyz = XYZ(mol)
xyz.write_file("methane.xyz")