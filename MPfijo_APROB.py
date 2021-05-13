import math as m
import numpy as np
from matplotlib import pylab
from pylab import*
from math import*
print("METODO DE PUNTO FIJO  e**x-x")
print("******************************")
x0=float(input("ingrese el punto inicial:"))
dgx0=-e**(-x0)
if abs(dgx0)>1:
    print("el metodo diverge")
else:
    raiz=[]
    n=int(input("ingrese el numero de iteraciones:"))
    for i in range(n):
        gx0=e**(-x0)
        x0=gx0        
        print(x0)       
    raiz.append(x0)
    x=arange(-3,3,0.5)
    y=m.e**(-x)-x
    import matplotlib.pyplot as mpl
    mpl.plot(x,y)
    mpl.scatter(raiz,0)
    mpl.grid()
    plot(x,y,color="red",label="EXPONENCIAL")
    legend()
    xlabel("EJE X")
    ylabel("EJE Y")
    title("GRÁFICA FUNCIÓN $Y=e^{-x}-x$")
