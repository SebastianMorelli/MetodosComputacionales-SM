import numpy as np
import matplotlib.pylab as plt

unif = np.random.random(1000)*20 -10

fig0 = plt.figure(figsize=(8,4))
ax = fig0.add_subplot(111)
ax.hist(unif, bins = 100)
ax.set_xlabel('Números aleatorios')
ax.set_ylabel('Repeticiones')
ax.set_title('Distribución Uniforme de Números Aleatorios')

plt.savefig('uniforme.pdf')

gauss = np.random.normal(17,5,1000)

fig1 = plt.figure(figsize=(8,4))
ax = fig1.add_subplot(111)
ax.hist(gauss, bins = 100)
ax.set_xlabel('Números aleatorios')
ax.set_ylabel('Repeticiones')
ax.set_title('Distribución Gaussiana de Números Aleatorios')

plt.savefig('gaussiana.pdf')

cuad1 = np.random.random(1000)*30.5 -0
cuad2 = np.random.random(1000)*30.5 -0

fig2 = plt.figure(figsize=(8,4))
ax = fig2.add_subplot(111)
ax.plot(cuad1, cuad2,'.r')
ax.set_xlabel('Números aleatorios $X$')
ax.set_ylabel('Números aleatorios $Y$')
ax.set_title('Distribución Aleatoria en Cuadrado de Lado 30.5')

plt.savefig('cuadrado.pdf')

r = 23
circX = np.random.random(1000)*46 -23
circY = np.empty([1000])

for i in range(len(circX)):
    y = np.sqrt((r**2 - np.abs(circX[i])**2))
    circY[i] = np.random.random(1)*np.abs(y*2) -y

fig3 = plt.figure(figsize=(8,8))
ax = fig3.add_subplot(111)
ax.plot(circX, circY,'.r')
ax.set_xlabel('Números aleatorios $X$')
ax.set_ylabel('Números aleatorios $Y$')
ax.set_title('Distribución Aleatoria en Circulo de Radio 23')

plt.savefig('circulo.pdf')
