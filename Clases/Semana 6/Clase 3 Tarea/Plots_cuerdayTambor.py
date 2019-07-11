import numpy as np
import matplotlib.pylab as plt

xFijos = np.genfromtxt('dataFijos.txt', usecols=(0))
yFijos = np.genfromtxt('dataFijos.txt', usecols=(1))

xLibres = np.genfromtxt('dataLibres.txt', usecols=(0))
yLibres = np.genfromtxt('dataLibres.txt', usecols=(1))

xFor = np.genfromtxt('dataForzado.txt', usecols=(0))
yFor = np.genfromtxt('dataForzado.txt', usecols=(1))

fig0 = plt.figure(figsize=(15,20))
ax0 = fig0.add_subplot(311)
ax0.plot(xFijos,yFijos, 'r', label = 'Cuerda Extremos Fijos')
ax0.set_xlabel('$x[m]$', size = 15)
ax0.set_ylabel('$Amplitud[m]$', size = 15)
ax0.set_title('Posicion de una Cuerda de Extremos Fijos en Diferentes Tiempos de Oscilación')
ax0.legend()

ax1 = fig0.add_subplot(312)
ax1.plot(xLibres,yLibres, 'b', label = 'Cuerda Extremos Libres')
ax1.set_xlabel('$x[m]$', size = 15)
ax1.set_ylabel('$Amplitud[m]$', size = 15)
ax1.set_title('Posicion de una Cuerda de Extremos Libres en Diferentes Tiempos de Oscilación')
ax1.legend()

ax2 = fig0.add_subplot(313)
ax2.plot(xFor,yFor, 'k', label = 'Cuerda Forzada')
ax2.set_xlabel('$x[m]$', size = 15)
ax2.set_ylabel('$Amplitud[m]$', size = 15)
ax2.set_title('Posicion de una Cuerda de un Extremo Libre y otro Forzado en Diferentes Tiempos de Oscilación')
ax2.legend()

plt.savefig('plotCuerdas.pdf')
