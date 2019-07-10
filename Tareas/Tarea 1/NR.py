import numpy as np 
import matplotlib.pylab as plt

def poli(x0):
    return  (x0**5)-(2.0*x0**4)-(10.0*x0*x0*x0)+(20.0*x0*x0)+ (9.0*x0)-18.0

interval = np.linspace(-3.5,3.5,1000)

fig0 = plt.figure()
ax = fig0.add_subplot(111)
ax.plot(interval,poli(interval), 'r-', label = 'Función polinómica')
ax.set_xlabel('Intervalo')
ax.set_ylabel('Función evaluada en intervalo')
ax.legend()

plt.savefig('NRpoli.pdf')

def derivative(funct,inter):
    results = np.empty(0)
    for i in range (len(inter)-1):
        h = np.abs(inter[i]-inter[i+1])
        derivative = np.array([(funct(inter[i]+h/2)-funct(inter[i]-h/2))/(h)])
        results = np.append(results,([derivative]))
    return results

def NewRaph(funct,dfunct,x0):
    deriv = dfunct(funct,interval)
    exact = 1e-10
    cont = 0
    while(np.abs(funct(x0))>exact):
        x0 = x0 - (funct(x0)/deriv[int(x0)])
        cont = cont +1
    return x0

def NewRaphCont(funct,dfunct,x0):
    deriv = dfunct(funct,interval)
    exact = 1e-10
    cont = 0
    while(np.abs(funct(x0))>exact):
        x0 = x0 - (funct(x0)/deriv[int(x0)])
        cont = cont +1
    return cont

print(NewRaph(poli,derivative,-3),poli(NewRaph(poli,derivative,-3)))

print(NewRaph(poli,derivative,-1),poli(NewRaph(poli,derivative,-1)))

results = np.empty(0)
itera = np.empty(0)
numguess = np.empty(0)
for i in range (1000):
    alea = np.random.random(1)*8 -4
    numguess = np.append(numguess,alea)
    root = NewRaph(poli,derivative,alea)
    results = np.append(results, root)
    counters = NewRaphCont(poli,derivative,alea)
    itera = np.append(itera, counters)
    
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.scatter(numguess,itera, color ='red', label = 'Número de iteraciones')
ax.legend()
plt.savefig('NR_itera.pdf')