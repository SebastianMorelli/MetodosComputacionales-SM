import numpy as np
import matplotlib.pylab as plt

x = np.genfromtxt('data.txt', usecols=(0))
y = np.genfromtxt('data.txt', usecols=(1))

fig0 = plt.figure(figsize=(10,6))
ax0 = fig0.add_subplot(111)
ax0.plot(x,y, 'r', label = 'Cuerda Extremos Fijos')
ax0.set_xlabel('$x[m]$', size = 15)
ax0.set_ylabel('$Amplitud[m]$', size = 15)
ax0.set_title('Posicion de una Cuerda de Extremos Fijos en Diferentes Tiempos de Oscilación')
ax0.legend()

plt.savefig('plotCuerdas.pdf')