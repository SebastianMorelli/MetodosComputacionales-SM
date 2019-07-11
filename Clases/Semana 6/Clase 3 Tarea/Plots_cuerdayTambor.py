import numpy as np
import matplotlib.pylab as plt

x = np.genfromtxt('data.txt', usecols=(0))
y = np.genfromtxt('data.txt', usecols=(1))

fig0 = plt.figure(figsize=(10,6))
ax = fig0.add_subplot(111)
ax.plot(x,y, 'r', label = 'Cuerda')
ax.set_xlabel('$x[m]$', size = 15)
ax.set_ylabel('$Amplitud[m]$', size = 15)
ax.set_title('Posicion de una Cuerda')
ax.legend()
