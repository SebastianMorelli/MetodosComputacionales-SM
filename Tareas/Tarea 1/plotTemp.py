import numpy as np
import matplotlib.pylab as plt

data = np.genfromtxt('TempPomedios.txt')

fig0 = plt.figure()
ax = fig0.add_subplot(111)
ax.plot(data[:,0],data[:,1], '.r-', label = 'Promedio Temp')
ax.set_xlabel('Años')
ax.set_ylabel('Promedio de Temperaturas')
ax.set_title('Promedio de Temperaturas por Año')
ax.legend()

plt.savefig('plotTemp.png')