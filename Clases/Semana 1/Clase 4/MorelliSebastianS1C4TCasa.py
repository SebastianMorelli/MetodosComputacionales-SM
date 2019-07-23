#LEER DATOS DE UN ARCHIVO EXTERNO PUNTO 1

import numpy as np

dat = np.genfromtxt('resorte.dat', skip_header=52, usecols=(1))
print (dat[0])


#LEER DATOS DE UN ARCHIVO UN POCO MÁS PROBLEMÁTICO PUNTO 2

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

datos = np.genfromtxt('sismos.txt', delimiter="\t", skip_header=1, usecols=(20,21))
print(datos)

fig= plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datos[:,1],datos[:,0],label='Latitud vs. Longitud',alpha = 0.5, c='darkred')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.set_title('Latitud vs. Longitud')
ax.legend()
plt.savefig('sismos.pdf')


#GRÁFICAS CON MATPLOTLIB PUNTO 3

###HISTOGRAMA RADIOS

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = np.genfromtxt('radios.dat')

plt.hist(data, bins=100, color='darkred')
plt.savefig('radios.pdf')
plt.show()


###GRÁFICA CON SUBPLOTS

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = np.genfromtxt('room-temperature.csv', delimiter=',', skip_header=1, usecols=(1,2,3,4))

fig=plt.figure(figsize=(12,8))
ax1=fig.add_subplot(221)
ax1.plot(data[:,0], color = 'C0', label = 'Temperature 1')
ax1.set_xlabel('Time (30 minutes lapse between each value)')
ax1.set_ylabel('Temperatue 1')
ax1.legend()

ax2=fig.add_subplot(222)
ax2.plot(data[:,0], color = 'C1', label = 'Temperature 2')
ax2.set_xlabel('Time (30 minutes lapse between each value)')
ax2.set_ylabel('Temperatue 2')
ax2.legend()

ax3=fig.add_subplot(223)
ax3.plot(data[:,0], color = 'C2', label = 'Temperature 3')
ax3.set_xlabel('Time (30 minutes lapse between each value)')
ax3.set_ylabel('Temperatue 3')
ax3.legend

ax4=fig.add_subplot(224)
ax4.plot(data[:,0], color = 'C3', label = 'Temperature 4')
ax4.set_xlabel('Time (30 minutes lapse between each value)')
ax4.set_ylabel('Temperatue 4')
ax4.legend()

plt.savefig('Temperaturas.pdf')


#PROGRAMACIÓN ORIENTADA A OBJETOS PUNTO 4


import numpy as np
import matplotlib.pylab as plt

class Robot:
    def __init__(self,posc,size):
        self.posc = posc
        self.size = size
        self.path = [self.posc]
        
    def walk (self):
        x = np.random.random(1)*300
        
        if (x <= 100):
            self.posc = self.posc - self.size
        elif (x > 200):
            self.posc = self.posc + self.size
        else:
            self.posc = self.posc
            
        return self.posc
            
    def route(self):
        newposc = self.walk()
        self.path.append(newposc)
        return self.path
    
Hugo = Robot(5,1)
Paco = Robot(8,2)
Luis = Robot(3,3)

for _ in range (100):
    Hugo.route()
    Paco.route()
    Luis.route()

H = Hugo.path
P = Paco.path
L = Luis.path

fig = plt.figure()
ax=fig.add_subplot(111)
ax.plot(H, color = 'C0', label = 'Hugo')
ax.plot(P, color = 'C2', label = 'Paco')
ax.plot(L, color = 'C3', label = 'Luis')
ax.set_xlabel('Pasos')
ax.set_ylabel('Posición')
ax.set_title('The Walking Robots')
ax.legend()
plt.savefig('Robot.pdf')


#PREPARACIÓN S2C1 INTEGRACION NUMERICA

###MÉTODO SUMA DE RECTANGULOS


###MÉTODO TRAPEZOIDE


###MÉTODO SIMPSON
