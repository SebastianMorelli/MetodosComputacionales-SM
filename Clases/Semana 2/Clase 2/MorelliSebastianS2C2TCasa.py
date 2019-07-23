#EJERCICIO INTEGRALES PUNTO 1

###MÉTODO SUMA DE RECTANGULOS

import numpy as np
import matplotlib.pylab as plt

def fun(x0):
    return np.cos(x0)
    
div=10000
h = (((3*np.pi)/2)/(div-1)) 
interval = np.linspace(0,(3*np.pi)/2, div)
def analitica(a,b):
    return np.sin(b)-np.sin(a)


def sumaRec(x0):
    return np.sum(fun(x0))*h


print ('El resultado analítico de la integral de coseno entre 0 y 3pi/2 es de', analitica(0,3*np.pi/2),
       ', con el método de integración de suma de rectangulos se encontró un valor de', sumaRec(interval))


###MÉTODO TRAPEZOIDE

import numpy as np
import matplotlib.pylab as plt

def fun(x0):
    return np.cos(x0)

div=10000
h = (((3*np.pi)/2)/(div-1)) 
interval = np.linspace(0,(3*np.pi)/2, div)
def analitica(a,b):
    return np.sin(b)-np.sin(a)

def trapezoide(x0,a,b):
    return (np.sum(fun(x0[1:len(x0)-1]))*h)+h/2*fun(a)+h/2*fun(b)

print ('El resultado analítico de la integral de coseno entre 0 y 3pi/2 es de', analitica(0,3*np.pi/2),
       ', con el método de integración de trapezoides se encontró un valor de', trapezoide(interval,0,3*np.pi/2))
       
       
###MÉTODO SIMPSON

import numpy as np
import matplotlib.pylab as plt

def fun(x0):
    return np.cos(x0)

div=10000
h = (((3*np.pi)/2)/(div-1)) 
interval = np.linspace(0,(3*np.pi)/2, div)
def analitica(a,b):
    return np.sin(b)-np.sin(a)

def simpson(x0):
    return np.sum((4*h/3)*(fun(x0[1:len(x0)-1:2])))+np.sum((2*h/3)*(fun(x0[2:len(x0)-1:2])))+(h/3)*fun(x0[0])+(h/3)*fun(x0[len(x0)-1])
    
print ('El resultado analítico de la integral de coseno entre 0 y 3pi/2 es de', analitica(0,3*np.pi/2),
       ', con el método de integración de Simpson se encontró un valor de', simpson(interval))


#ERRORES PARA DIFERENTES MÉTODOS PUNTO 2


import numpy as np
import matplotlib.pylab as plt

def fun(x0):
    return np.cos(x0)

def h (inter):
    return (((3*np.pi)/2)/(len(inter)-1))

interval1 = np.linspace(0,(3*np.pi)/2, 10**2)
interval2 = np.linspace(0,(3*np.pi)/2, 10**3)
interval3 = np.linspace(0,(3*np.pi)/2, 10**4)
interval4 = np.linspace(0,(3*np.pi)/2, 10**5)
interval5 = np.linspace(0,(3*np.pi)/2, 10**6)
interval6 = np.linspace(0,(3*np.pi)/2, 10**7)

def analitica(a,b):
    return np.sin(b)-np.sin(a)

analitic = analitica(0,3*np.pi/2)

def sumaRec(x0):
    return np.sum(fun(x0))*h(x0)

sumaRec1 = sumaRec(interval1)
sumaRec2 = sumaRec(interval2)
sumaRec3 = sumaRec(interval3)
sumaRec4 = sumaRec(interval4)
sumaRec5 = sumaRec(interval5)
sumaRec6 = sumaRec(interval6)

def trapezoide(x0,a,b):
    return (np.sum(fun(x0[1:len(x0)-1]))*h(x0))+h(x0)/2*fun(a)+h(x0)/2*fun(b)

trap1 = trapezoide(interval1,0,3*np.pi/2)
trap2 = trapezoide(interval2,0,3*np.pi/2)
trap3 = trapezoide(interval3,0,3*np.pi/2)
trap4 = trapezoide(interval4,0,3*np.pi/2)
trap5 = trapezoide(interval5,0,3*np.pi/2)
trap6 = trapezoide(interval6,0,3*np.pi/2)

def simpson(x0):
    return np.sum((4*h(x0)/3)*(fun(x0[1:len(x0)-1:2])))+np.sum((2*h(x0)/3)*(fun(x0[2:len(x0)-1:2])))+(h(x0)/3)*fun(x0[0])+(h(x0)/3)*fun(x0[len(x0)-1])

simp1 = simpson(interval1)
simp2 = simpson(interval2)
simp3 = simpson(interval3)
simp4 = simpson(interval4)
simp5 = simpson(interval5)
simp6 = simpson(interval6)

def error (valAn, valNum):
    return np.abs((valNum - valAn)/valAn)

errorSum1 = error(analitic,sumaRec1)
errorSum2 = error(analitic,sumaRec2)
errorSum3 = error(analitic,sumaRec3)
errorSum4 = error(analitic,sumaRec4)
errorSum5 = error(analitic,sumaRec5)
errorSum6 = error(analitic,sumaRec6)

errortrap1 = error(analitic,trap1)
errortrap2 = error(analitic,trap2)
errortrap3 = error(analitic,trap3)
errortrap4 = error(analitic,trap4)
errortrap5 = error(analitic,trap5)
errortrap6 = error(analitic,trap6)

errorSimp1 = error(analitic,simp1)
errorSimp2 = error(analitic,simp2)
errorSimp3 = error(analitic,simp3)
errorSimp4 = error(analitic,simp4)
errorSimp5 = error(analitic,simp5)
errorSimp6 = error(analitic,simp6)

listerrorSum = []
listerrorSum.extend([errorSum1, errorSum2, errorSum3, errorSum4, errorSum5, errorSum6])
listerrorTrap = []
listerrorTrap.extend([errortrap1, errortrap2, errortrap3, errortrap4, errortrap5, errortrap6])
listerrorSimp = []
listerrorSimp.extend([errorSimp1, errorSimp2, errorSimp3, errorSimp4, errorSimp5, errorSimp6])

divisiones = np.logspace(2,7,6)

fig=plt.figure(figsize=(12,8))

ax0 = fig.add_subplot(111)
ax0.loglog(divisiones,listerrorSum,'or-', label = 'Suma de Rectangulos')
ax0.loglog(divisiones,listerrorTrap,'ob-', label = 'Trapezoides')
ax0.loglog(divisiones,listerrorSimp,'og-', label = 'Simpson')
ax0.set_xlabel('Número de intervalos')
ax0.set_ylabel('Error relativo')
ax0.legend()

plt.savefig('ErrorRTS.pdf')


#OTROS MÉTODOS DE INTEGRACIÓN PUNTO 3

import numpy as np
import matplotlib.pylab as plt

def fun(x0):
    return np.cos(x0)

def analitica(a,b):
    return np.sin(b)-np.sin(a)

analitic = analitica(0,np.pi/2)

def Mval (lima, limb, div):
    alea = np.random.random(div)*(limb-lima)
    cos = fun(alea)
    return np.sum(cos)*(1/div)*(limb-lima)

print ('El resultado analítico de la integral de coseno entre 0 y pi/2 es de', analitic,
       ', con el método de integración de Mean Value se encontró un valor de', Mval(0,np.pi/2,10000))


def MontCar (a,b,funct,div):
    k = np.linspace(a,b,10000); evalu = funct(k); maxi = np.max(evalu)
    area = (b-a)*maxi
    cont = 0
    
    for i in range (div):
        
        aleaX = np.random.random()*(b-a)
        aleaY = np.random.random()*maxi
    
        if (aleaY <= funct(aleaX)):
            cont = cont + 1
        
    return (cont/div)*area
    
print ('El resultado analítico de la integral de coseno entre 0 y pi/2 es de', analitic,
       ', con el método de integración de Monte Carlo se encontró un valor de', MontCar(0,np.pi/2, fun,10000))

interval = np.logspace(2,7,6)

def error (valAn, valNum):
    return np.abs((valNum - valAn)/valAn)

listerrorMval = []
listerrorMont = []

for i in interval:
    listerrorMval.append(error(analitic,Mval(0,np.pi/2,int(i))))
    listerrorMont.append(error(analitic,MontCar(0,np.pi/2,fun,int(i))))
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog(interval,listerrorMval, 'or-', label = 'Valor Medio')
ax.loglog(interval,listerrorMont, 'ob-', label = 'Monte Carlo')
ax.set_xlabel('Número de intervalos')
ax.set_ylabel('Error relativo')
ax.legend()

plt.savefig('MCMC_ErrorRTS.pdf')


#MUESTREO DIRECTO DE MONTE CARLO CON VALORES NEGATIVOS PUNTO 4

import numpy as np
import matplotlib.pylab as plt

def fun(x0):
    return np.cos(x0)

def analitica(a,b):
    return np.sin(b)-np.sin(a)

analitic = analitica(0,3*np.pi/2)

def Mval (lima, limb, div):
    alea = np.random.random(div)*(limb-lima)
    cos = fun(alea)
    return np.sum(cos)*(1/div)*(limb-lima)

print ('El resultado analítico de la integral de coseno entre 0 y 3pi/2 es de', analitic,
       ', con el método de integración de Mean Value se encontró un valor de', Mval(0,3*np.pi/2,10000))

def MontCar (a,b,funct,div):
    k = np.linspace(a,b,10000); evalu = funct(k); maxi = np.max(evalu); mini = np.min(evalu)
    area = (b-a)*(maxi-mini); cont1 = 0; cont2 = 0
    
    for i in range (div):
        aleaX = np.random.random()*(b-a) 
        aleaY = np.random.random()*(maxi-mini) +mini
        
        if (aleaY <= funct(aleaX) and aleaY > 0):
            cont1 = cont1 + 1
            
        elif(aleaY >= funct(aleaX) and aleaY < 0):
            cont2 = cont2 +1 
            
        
    return ((cont1-cont2)/div)*area

print ('El resultado analítico de la integral de coseno entre 0 y 3pi/2 es de', analitic,
       ', con el método de integración de Monte Carlo se encontró un valor de', MontCar(0,3*np.pi/2,fun,10000))

interval = np.logspace(2,7,6)

def error (valAn, valNum):
    return np.abs((valNum - valAn)/valAn)

listerrorMval = []
listerrorMont = []

for i in interval:
    listerrorMval.append(error(analitic,Mval(0,3*np.pi/2,int(i))))
    listerrorMont.append(error(analitic,MontCar(0,3*np.pi/2,fun,int(i))))
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.loglog(interval,listerrorMval, 'or-', label = 'Valor Medio')
ax.loglog(interval,listerrorMont, 'ob-', label = 'Monte Carlo')
ax.set_xlabel('Número de intervalos')
ax.set_ylabel('Error relativo')
ax.legend()

plt.savefig('ErrorRTS_random.pdf')

#VARIAS DIMENSIONES PUNTO 5

import numpy as np
import matplotlib.pylab as plt

def fun(x0,x1,x2,x3):
    return np.cos(x0+x1)*x2*x3

def Mval (lima, limb, funct, div,dimen):
    alea = np.random.random(div)*(limb-lima)
    cos = funct(alea,alea,alea,alea)
    return np.sum(cos)*(1/div)*(limb-lima)**dimen

Mval(0,1.5*np.pi,fun,10000,4)

#PREPARACION CLASE S2C3 DERIVACION NUMERICA

import numpy as np
import matplotlib.pylab as plt

interval = np.linspace(0,2*np.pi,1000000)

def fun(x0):
    return np.cos(x0)

analitic = fun(interval)

def dForward(funct,inter):
    results = []
    for i in range (len(inter)-1):
        derivative = (funct(inter[i]+inter[i+1])-funct(inter[i]))/inter[i+1]
        results.append(derivative)
    return (results)
    
def dCentral(funct,inter):
    results = []
    for i in range (len(inter)-1):
        derivative = (funct(inter[i]+(inter[i+1])/2)-funct(inter[i]-(inter[i+1])/2))/inter[i+1]
        results.append(derivative)
    return results
    
    
listdForward = dForward(fun,interval)
listdCentral = dCentral(fun,interval)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(interval,analitic, 'r-', label = 'cos(x)')
ax.plot(interval[1:], listdForward, 'b-', label = 'dForward')
ax.plot(interval[1:], listdCentral, 'g-', label = 'dCentral')
ax.legend()