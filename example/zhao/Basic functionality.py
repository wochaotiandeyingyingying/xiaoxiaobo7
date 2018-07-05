import pymatgen as mg

si = mg.Element("Si")
print("Atomic mass of Si is {}".format(si.atomic_mass))
print("Si has a melting point of {}".format(si.melting_point))
print("Ionic radii for Si: {}".format(si.ionic_radii))



print("Atomic mass of Si in kg:  {}".format(si.atomic_mass.to("kg")))

fe2 = mg.Specie("Fe", 2)
print(fe2.atomic_mass)
print(fe2.ionic_radius)


comp = mg.Composition("Fe2O3")
print("Weight of Fe2O3 is {}".format(comp.weight))
print("Amount of Fe in Fe2O3 is {}".format(comp["Fe"]))
print("Atomic fraction of Fe is {}".format(comp.get_atomic_fraction("Fe")))
print("Weight fraction of Fe is {}".format(comp.get_wt_fraction("Fe")))


# Creates cubic Lattice with lattice parameter 4.2
lattice = mg.Lattice.cubic(4.2)
print(lattice.lengths_and_angles)


structure = mg.Structure(lattice, ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
print("Unit cell vol = {}".format(structure.volume))
print("First site of the structure is {}".format(structure[0]))


structure.make_supercell([2, 2, 1]) #Make a 3 x 2 x 1 supercell of the structure
del structure[0] #Remove the first site
structure.append("Na", [0,0,0]) #Append a Na atom.
structure[-1] = "Li" #Change the last added atom to Li.
structure[0] = "Cs", [0.01, 0.5, 0] #Shift the first atom by 0.01 in fractional coordinates in the x-direction.
immutable_structure = mg.IStructure.from_sites(structure) #Create an immutable structure (cannot be modified).
print(immutable_structure)


#Determining the symmetry
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
finder = SpacegroupAnalyzer(structure)
print("The spacegroup is {}".format(finder.get_space_group_symbol()))


from pymatgen.analysis.structure_matcher import StructureMatcher
#Let's create two structures which are the same topologically, but with different elements, and one lattice is larger.
s1 = mg.Structure(lattice, ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
s2 = mg.Structure(mg.Lattice.cubic(5), ["Rb", "F"], [[0, 0, 0], [0.5, 0.5, 0.5]])
m = StructureMatcher()
print(m.fit_anonymous(s1, s2)) #Returns a mapping which maps s1 and s2 onto each other. Strict element fitting is also available.


#Convenient IO to various formats. Format is intelligently determined from file name and extension.
structure.to(filename="POSCAR")
structure.to(filename="CsCl.cif")

#Or if you just supply fmt, you simply get a string.
print(structure.to(fmt="poscar"))
print(structure.to(fmt="cif"))

#Reading a structure from a file.
structure = mg.Structure.from_file("POSCAR")
