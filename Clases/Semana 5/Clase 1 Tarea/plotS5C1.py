import numpy as np
import matplotlib.pylab as plt

x = np.genfromtxt ('Data.txt', usecools=(0), delimiter=(','))
cos = np.genfromtxt ('Data.txt', usecools=(1), delimiter=(','))
Deriv = np.genfromtxt ('Data.txt', usecools=(2), delimiter=(','))

fig0 = plt.figure(figsize(12,6))
ax = fig0.add_subplot(111)
ax.plot(x,cos,'r', label='cos(x)')
ax.plot(x,Deriv,'b', label='Derivada')
ax.set_xlabel('x')
ax.set_ylabel('Función evaluada en x')
ax.set_title('cos(x) y su Derivada')
ax.legend()

plt.savefig('S5C1PLOT.pdf')
