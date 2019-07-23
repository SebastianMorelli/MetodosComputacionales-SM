import numpy as np
import matplotlib.pylab as plt

x = np.genfromtxt('Canal_ionico.txt', usecols=(0))
y = np.genfromtxt('Canal_ionico.txt', usecols=(1))

def HaciendoCirculos(Posx, Posy):
    rad = np.sqrt(Posx**2+Posy**2)
    return rad

def HallandoPoros(x_guess, y_guess, sigma):
    
    x_new = np.random.normal(x_guess, sigma, 1)
    y_new = np.random.normal(y_guess, sigma, 1)
    rad_old = HaciendoCirculos(x_guess, y_guess)
    rad_new = HaciendoCirculos(x_new, y_new)
    best_x = x_guess
    best_y = y_guess
    
    for k in range (1000):
        for i in range (len(x)):
            if(x_new + rad_new < x[i] and y_new + rad_new < y[i] and rad_new > rad_old):
                best_x = x_new
                best_y = y_new
                
        x_guess = x_new
        y_guess = y_new
    
    return [best_x, best_y, HaciendoCirculos(best_x, best_y)] 
    
    Mejores = HallandoPoros(5,5,1)
    
    fig0 = plt.figure(figsize=(8,8))
ax = fig0.add_subplot(111)
ax.plot(x, y, '.k', label='Posiciones Átomos')
circle1 = plt.Circle((Mejores[0], Mejores[1]), Mejores[2] , color='r', fill=False)
ax.add_artist(circle1)
ax.set_xlabel('$x$', size=15)
ax.set_ylabel('$y$', size=15)
ax.legend()

plt.savefig('Canal.png')
