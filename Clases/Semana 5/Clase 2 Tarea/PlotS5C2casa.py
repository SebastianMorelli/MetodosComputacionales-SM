import numpy as np
import matplotlib.pylab as plt

x = np.genfromtxt('Data.txt', usecols=(0), skip_header=(0))
Euler = np.genfromtxt('Data.txt', usecols=(1), skip_header=(0))
RugenKutta = np.genfromtxt('Data.txt', usecols=(2), skip_header=(0))

fig = plt.figure(figsize=(15,10))

ax0 = fig.add_subplot(221)
ax0.plot(x,Euler, '.r-', label= 'Solución Euler')
ax0.set_xlabel('$x$', size=15)
ax0.set_ylabel('Ecuación Dif. Evaluada')
ax0.legend()

ax1 = fig.add_subplot(222)
ax1.plot(x,RugenKutta, '.b-', label= 'Solución Rugen-Kutta')
ax1.legend()
ax1.set_xlabel('$x$', size=15)
ax1.set_ylabel('Ecuación Dif. Evaluada')


ax2 = fig.add_subplot(223)
ax2.plot(x[2:],np.abs(np.exp(-x)-Euler)[2:], '.k-', label= 'Error Euler')
ax2.set_xlabel('$x$', size=15)
ax2.set_ylabel('Porcentaje de error')
ax2.legend()

ax3 = fig.add_subplot(224)
ax3.plot(x[2:],np.abs(np.exp(-x)-RugenKutta)[2:], '.g-', label= 'Error Rugen-Kutta')
ax3.set_xlabel('$x$', size=15)
ax3.set_ylabel('Porcentaje de error')
ax3.legend()

plt.savefig('plotMetodoyError.pdf')