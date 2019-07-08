import numpy as np
import matplotlib.pylab as plt

t = np.genfromtxt('datos.txt', usecols=(0), skip_header=(0))
Pos = np.genfromtxt('datos.txt', usecols=(1), skip_header=(0))
Vel = np.genfromtxt('datos.txt', usecols=(2), skip_header=(0))

fig = plt.figure(figsize=(12,8))

ax0 = fig.add_subplot(111)
ax0.plot(t,Pos, 'r-', label= 'Oscilación Armónica')
ax0.set_xlabel('$tiempo [s]$', size=15)
ax0.set_ylabel('$Posición [m]$', size = 15)
ax0.set_title('Posición de un oscilador armónico con respecto al tiempo', size =18)
ax0.legend()

plt.savefig('MorelliSebastianResorte.pdf')