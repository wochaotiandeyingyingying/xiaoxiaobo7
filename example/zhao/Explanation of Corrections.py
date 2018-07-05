import re
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from  pymatgen  import MPRester
#To do our testing, let's use the MPRester to get a sample computed entry from the Materials Project.
m = MPRester()
entries = m.get_entries("LiFePO4")
entry = entries[0]