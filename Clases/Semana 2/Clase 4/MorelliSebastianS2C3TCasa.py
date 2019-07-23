#DERIVADAS CENTRAL Y FORWARD PUNTO 1

import numpy as np
import matplotlib.pylab as plt

interval = np.linspace(0,2*np.pi,10000)

def fun(x0):
    return np.cos(x0)

analitic = fun(interval)

def dAnalitica(x0):
    return -np.sin(x0)

danalitic = dAnalitica(interval)

def dForward(funct,inter):
    results = np.empty(0)
    for i in range (len(inter)-1):
        h = np.abs(inter[i]-inter[i+1])
        derivative = np.array([(funct(inter[i]+h)-funct(inter[i]))/h])
        results = np.append(results,[derivative])
    return results
    
def dCentral(funct,inter):
    results = np.empty(0)
    for i in range (len(inter)-1):
        h = np.abs(inter[i]-inter[i+1])
        derivative = np.array([(funct(inter[i]+h/2)-funct(inter[i]-h/2))/(h)])
        results = np.append(results,([derivative]))
    return results

listdForward = dForward(fun,interval)
listdCentral = dCentral(fun,interval)

fig0 = plt.figure(figsize =(15,5))

ax0 = fig0.add_subplot(121)
ax0.plot(interval,analitic, 'r-', label = 'cos(x)')
ax0.plot(interval[1:], listdForward, 'b-', label = 'Forward Difference')
ax0.set_xlabel('Intervalo de 0 a 2pi')
ax0.set_ylabel('Funcion y Derivada evaluadas')
ax0.legend()

ax1= fig0.add_subplot(122) 
ax1.plot(interval,analitic, 'r-', label = 'cos(x)')
ax1.plot(interval[1:], listdCentral, 'g-', label = 'Central Difference')
ax1.set_xlabel('Intervalo de 0 a 2pi')
ax1.set_ylabel('Funcion y Derivada evaluadas')
ax1.legend()

plt.savefig('DerivadaFun.pdf')

def error (valAn, valNum):
    return np.abs((valNum - valAn))

listerrordForward = np.empty(0)
listerrordCentral = np.empty(0)

listerrordForward = np.append(listerrordForward, error(danalitic[:-1],listdForward))
listerrordCentral = np.append(listerrordCentral, error(danalitic[:-1],listdCentral))

fig1 = plt.figure(figsize =(18,6))

ax0 = fig1.add_subplot(121)
ax0.plot(interval[1:], listerrordForward, 'r-', label = 'Error Forward Difference')
ax0.set_xlabel('Intervalo de 0 a 2pi')
ax0.set_ylabel('Error Relativo')
ax0.legend()

ax1= fig1.add_subplot(122) 
ax1.plot(interval[1:], listerrordCentral, 'b-', label = ' Error Central Difference')
ax1.set_xlabel('Intervalo de 0 a 2pi')
ax1.set_ylabel('Error Relativo')
ax1.legend()

plt.savefig('ErrorDerivada.pdf')

def d2dt2 (funct,inter):
    results = np.empty(0)
    for i in range (len(inter)-1):
        h = np.abs(inter[i]-inter[i+1])
        secDerivative = ([(funct(inter[i]+h)+funct(inter[i]-h)-2*funct(inter[i]))/h**2])
        results = np.append(results,([secDerivative]))
    return results

fig2 = plt.figure(figsize =(18,6))

ax0 = fig2.add_subplot(121)
ax0.plot(interval,analitic, 'r-', label = 'cos(x)' )
ax0.plot(interval[1:], d2dt2(fun,interval), 'b-', label = 'Segunda Derivada')
ax0.set_xlabel('Intervalo de 0 a 2pi')
ax0.set_ylabel('Funciones Evaluadas')
ax0.legend()

plt.savefig('2DerivadaFun.pdf')



#DERIVADAS CON DATOS PUNTO 2

import numpy as np
import matplotlib.pylab as plt

x = np.genfromtxt('datosfun.dat', usecols=(0))
fx = np.genfromtxt('datosfun.dat', usecols=(1))

datX = np.array([])
datFx = np.array([])

for i in range (len(x)):
    
    datX = np.append(datX, x[i])
    datFx = np.append(datFx, fx[i])

def derivative (data1,data2):
    h = np.abs(data1[0]-data1[1])
    derivative = (data2[1:]-data2[:-1])/h
    return derivative

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(datX, datFx, '-', label = 'Función', color = 'black' )
ax.plot(datX[:-1], derivative(datX,datFx), '-', label = 'Derivada', color = 'red')
ax.set_xlabel('Datos de X')
ax.set_ylabel('Función Evaluada en X')
ax.legend()

plt.savefig('DerivadaDatos.pdf')


#BISECCIÓN Y NEWTON-RAPHSON PUNTO 3

import numpy as np
import matplotlib.pylab as plt

def fun(x):
    return x**3 +17*x-15

def bisec(funct,x0,x1):
    exact = 1e-15
    for i in range (100):
        if(np.abs(x0-x1)>exact):
            mid = (x0 + x1)/2
            if (funct(x0)*funct(mid)>0):
                x0 = mid
            elif(funct(x0)*funct(mid)<0):
                x1 = mid
        else:
            break
    return mid

print('El método de bisección dio un resultado',bisec(fun,0,1), 'al evaluar dicho resultado en la función obtenemos',
      fun(bisec(fun,0,1)))

def derivative(funct,inter):
    results = np.empty(0)
    for i in range (len(inter)-1):
        h = np.abs(inter[i]-inter[i+1])
        derivative = np.array([(funct(inter[i]+h/2)-funct(inter[i]-h/2))/(h)])
        results = np.append(results,([derivative]))
    return results

def NewRaph(funct,dfunct,x0):
    deriv = dfunct(funct,interval)
    exact = 1e-15
    for i in range(20):
        if(np.abs(funct(x0))>exact):
            x0 = x0 - (funct(x0)/deriv[int(x0)])
    return x0
    
    
interval = np.linspace(0,1000,10000)

print('El método de Newton Raphson dio un resultado', NewRaph(fun,derivative,1), 'al evaluar dicho resultado en la función obtenemos',
      fun(NewRaph(fun,derivative,1)))