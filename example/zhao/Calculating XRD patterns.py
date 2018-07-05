from pymatgen import Lattice, Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from IPython.display import Image, display
from matplotlib import pyplot


# Create CsCl structure
a = 4.209 #Angstrom(埃:一个长度单位，用来表示原子尺寸、键长和电磁波波长。)
latt = Lattice.cubic(a)

#latt:点阵一个长度为a的立方体
#species：物质，这里是["Cs", "Cl"]
#坐标：三位数组的列表，表示物质的坐标
structure = Structure(latt, ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])

c = XRDCalculator()

#get_plot返回的结果就是一个pyplot类型的图片
image = c.get_plot(structure, two_theta_range=(0, 90), annotate_peaks=True, ax=None, with_labels=True, fontsize=16)

#image.show()
image.savefig("alpha CsCl.jpg")
#display(Image(filename=('./PDF - alpha CsCl.png')))
a = 6.923 #Angstrom
latt = Lattice.cubic(a)
structure = Structure(latt, ["Cs", "Cs", "Cs", "Cs", "Cl", "Cl", "Cl", "Cl"],
                      [[0, 0, 0], [0.5, 0.5, 0], [0, 0.5, 0.5], [0.5, 0, 0.5],
                       [0.5, 0.5, 0.5], [0, 0, 0.5], [0, 0.5, 0], [0.5, 0, 0]])

image = c.get_plot(structure, two_theta_range=(0, 90), annotate_peaks=True, ax=None, with_labels=True, fontsize=16)
#display(Image(filename=('./PDF - beta CsCl.png')))这段代码display我还没有弄明白，帮我看看哪里出问题了
#image.show()
image.savefig("beta CsCl.jpg")