from  pymatgen.electronic_structure.cohp  import Cohp
from pymatgen.electronic_structure.plotter import CohpPlotter
from pymatgen.io.lobster import Cohpcar

COHPCAR_path = "E:/Python/pymatgen-master/test_files/cohp/COHPCAR.lobster"
cohpcar = Cohpcar(filename=COHPCAR_path)
cdata = cohpcar.cohp_data
cdata_processed = {}
for key in cdata:
    c = cdata[key]
    c["efermi"] = 0
    c["energies"] = cohpcar.energies
    c["are_coops"] = False
    cdata_processed[key] = Cohp.from_dict(c)
cp = CohpPlotter()
cp.add_cohp_dict(cdata_processed)
x = cp.get_plot()
x.ylim([-6, 6])
x.show()