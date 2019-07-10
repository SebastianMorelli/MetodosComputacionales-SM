import numpy as np 
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d

EarthOrbit = np.genfromtxt('EarthOrbit.dat', usecols=(1,2,3))*149597870700
MarsOrbit = np.genfromtxt('MarsOrbit.dat', usecols=(1,2,3))*149597870700
EarthOrbitTime = np.genfromtxt('EarthOrbit.dat', usecols=(0))*3.154e7
MarsOrbitTime = np.genfromtxt('MarsOrbit.dat', usecols=(0))*3.154e7

fig0 = plt.figure(figsize = (10,5))
ax = fig0.add_subplot(111,projection='3d')
ax.plot(EarthOrbit[:,0], EarthOrbit[:,1], EarthOrbit[:,2], color='black', label='Earth Orbit')
ax.plot(MarsOrbit[:,0], MarsOrbit[:,1], MarsOrbit[:,2], color='blue', label='Mars Orbit')
ax.set_xlabel('X [AU]')
ax.set_ylabel('Y [AU]')
ax.set_zlabel('Z [AU]')
ax.set_title('ORBIT OF EARTH AND MARS CENTERED IN THE SUN')
ax.legend()

plt.savefig('Orbitas.pdf')

def segDeriv (data1,data2):
    h = np.abs(data1[0]-data1[1])
    derivative = (data2[2:]+data2[:-2]-2*data2[1:-1])/h**2
    return derivative

acEaX = segDeriv(EarthOrbitTime,EarthOrbit[:,0])
acEaY = segDeriv(EarthOrbitTime,EarthOrbit[:,1])
acEaZ = segDeriv(EarthOrbitTime,EarthOrbit[:,2])

acMaX = segDeriv(MarsOrbitTime,MarsOrbit[:,0])
acMaY = segDeriv(MarsOrbitTime,MarsOrbit[:,1])
acMaZ = segDeriv(MarsOrbitTime,MarsOrbit[:,2])

G = 6.674e-11

def normVec(x,y,z):
    norm = np.sqrt(x**2+y**2+z**2)
    return norm

def MassSun(acelX,acelY,acelZ,Orbit):
    r = normVec(Orbit[1:-1,0],Orbit[1:-1,1],Orbit[1:-1,2])
    a = normVec(acelX,acelY,acelZ)
    #print (r)
    mass = ((a)*(r**2))/G
    return mass

MassSunEarth = np.mean(MassSun(acEaX,acEaY,acEaZ,EarthOrbit))
MassSunMars = np.mean(MassSun(acMaX,acMaY,acMaZ,MarsOrbit))

print('La masa estimada del Sol obtenida a partir de las posiciones de la Tierra es', MassSunEarth, 
      '[kg] y la obtenida a partir de las posiciones de Marte es', MassSunMars, '[kg]')