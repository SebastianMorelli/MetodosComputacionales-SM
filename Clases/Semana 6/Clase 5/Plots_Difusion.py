import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d

x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
planx, plany = np.meshgrid(x,y)

temp = np.genfromtxt('data.txt')
fig0 = plt.figure(figsize=(15,12))

ax0 = fig0.add_subplot(111, projection='3d')
ax0.plot_surface(planx,plany,temp, color = 'darkred', label = 'Condición inicial')
ax0.set_xlabel('$y$',size=15)
ax0.set_ylabel('$x$',size=15)
ax0.set_zlabel('$temp$',size=15)
ax0.set_title('Temperaturas Iniciales', size = 20)

plt.savefig('Plots_Difusion.pdf')
