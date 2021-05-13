import math as m
import numpy as np
import matplotlib.pyplot as mpl
x=np.arange(-3,3,0.5)
y=m.e**(-x)-x
mpl.plot(x,y)
mpl.grid()
