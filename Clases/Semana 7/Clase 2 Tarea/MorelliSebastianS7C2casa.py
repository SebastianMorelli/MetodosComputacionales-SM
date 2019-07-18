import numpy as np
import matplotlib.pylab as plt

x0 = np.linspace(-4,4,1000)
sigmas = np.array([5, 0.2, 0.01, 0.1, 0.1, 0.1])
pasos = np.array([100000, 100000, 100000, 1000, 100000, 500000])

def mifun(x):
    x_a = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_a)**2 + a**2)

graph = mifun(x0)

fig0 = plt.figure(figsize=(8,6))
ax = fig0.add_subplot(111)
ax.plot(x0,graph, 'r', label = 'Función original')
ax.set_xlabel('$x$', size = 15)
ax.set_ylabel('$f(x)$', size = 15)
ax.legend()

plt.savefig('Funorigi.png')

def MetropolisHastings (numpas, sigma, func, x_guess):
    x_old = x_guess
    cont = np.empty([numpas])
    cont[0] = x_old
    
    for i in range (1,numpas):
        x_new = np.random.normal(x_old,sigma,1)
        alpha = func(x_new)/(func(x_old)+1e-5)
        if(alpha >= 1):
            cont[i] = x_new
        elif(alpha < 1):
            Beta = np.random.random(1)
            if(Beta < alpha):
                cont[i] = x_new
            elif(Beta > alpha):
                cont[i] = x_old
        x_old = x_new
    return cont
  
  for i in range (5):
    fig1 = plt.figure()
    ax = fig1.add_subplot(111)
    ax.plot(x0,graph, 'r', label = 'Función original')
    ax.set_xlabel('Valores hallados')
    ax.set_ylabel('Repeticiones')

    plt.savefig(('histograma_'+ str(sigmas[i])+'_'+ str(pasos[i])+'.pdf'))
