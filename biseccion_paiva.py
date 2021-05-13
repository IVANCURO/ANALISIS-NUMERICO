from math import*
print("METODO DE LA BISECCION  f(h)=12.4 - 10*((0.5)*pi-asin(h)-h*(1-h*h)**(0.5))")
print("**************************************************************************")
xi=float(input("ingrese el extremo izquierdo del intervalo:"))
xd=float(input("ingrese el extremo derecho del intervalo:"))
n=int(input("ingrese el numero de iteraciones:"))
print("{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}".format("Nro.I","xi","xd","xr","fxi","fxd","fxr","error"))
for i in range(n):
    xr=round((xi+xd)/2,5)
    fxi=12.4 - 10*((0.5)*pi-asin(xi)-xi*(1-xi*xi)**(0.5))
    fxd=12.4 - 10*((0.5)*pi-asin(xd)-xd*(1-xd*xd)**(0.5))
    fxr=12.4 - 10*((0.5)*pi-asin(xr)-xr*(1-xr*xr)**(0.5))
    error=(xr-xi)/xr
    if fxi*fxr<0:
        xd=xr
    else:
        xi=xr
    print("{:^10}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}".format(i+1,xi,xd,xr,fxi,fxd,fxr,error))
print("")
print("La raiz aproximada de",n,"es:",xr)
print("LA PROFUNDIDAD ES:",round(1-xr,3))

