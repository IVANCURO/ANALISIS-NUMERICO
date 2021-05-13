import math as m
import numpy as np
from matplotlib import pylab
from pylab import*
from math import*
print("METODO DE LA BISECCION  e**x-x")
print("******************************")
xi=float(input("ingrese el extremo izquierdo del intervalo:"))
xd=float(input("ingrese el extremo derecho del intervalo:"))
n=int(input("ingrese el numero de iteraciones:"))
fxi=e**(-xi)-xi
fxd=e**(-xd)-xd
if fxi*fxd>0:
    print("No hay raiz en este intervalo. Gracias por su intento")
else:
    raiz=[]
    print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Nro.I","xi","xd","xr","fxi","fxd","fxr"))
    for i in range(n):
        xr=round((xi+xd)/2,5)
        fxi=e**(-xi)-xi
        fxd=e**(-xd)-xd
        fxr=e**(-xr)-xr
        if fxi*fxr<0:
            xd=xr
        else:
            xi=xr
        print("{:^10}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}".format(i+1,xi,xd,xr,fxi,fxd,fxr))
 
    print("La raiz aproximada es:",xr)
    raiz.append(xr)
    opc=str(input("DESEA VER LA GRÁFICA SI/NO:"))
    if opc=="SI":
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
        show()
    else:
        print("...............GRACIAS POR SU VISITA..............") 
