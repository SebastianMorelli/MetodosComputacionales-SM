import numpy as np
import matplotlib.pylab as plt

#Distribución uniforme
unif = np.random.random(1000)*20 -10

fig0 = plt.figure(figsize=(8,4))
ax = fig0.add_subplot(111)
ax.hist(unif, bins = 100)
ax.set_xlabel('Números aleatorios')
ax.set_ylabel('Repeticiones')
ax.set_title('Distribución Uniforme de Números Aleatorios')

plt.savefig('uniforme.pdf')

#Distribución gaussiana
gauss = np.random.normal(17,5,1000)

fig1 = plt.figure(figsize=(8,4))
ax = fig1.add_subplot(111)
ax.hist(gauss, bins = 100)
ax.set_xlabel('Números aleatorios')
ax.set_ylabel('Repeticiones')
ax.set_title('Distribución Gaussiana de Números Aleatorios')

plt.savefig('gaussiana.pdf')

#Rectangulo Aleatorio
cuad1 = np.random.random(1000)*30.5 -0
cuad2 = np.random.random(1000)*30.5 -0

fig2 = plt.figure(figsize=(8,4))
ax = fig2.add_subplot(111)
ax.plot(cuad1, cuad2,'.r')
ax.set_xlabel('Números aleatorios $X$')
ax.set_ylabel('Números aleatorios $Y$')
ax.set_title('Distribución Aleatoria en Cuadrado de Lado 30.5')

plt.savefig('cuadrado.pdf')

#Círculo aleatorio
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

def meGustaCaminar (datax, datay, sigma):
    probPaso = np.random.random(100)*1
    onex = []
    oney = []
    caminatax = []
    caminatay = []
    
    for i in range(len(datax)):
        for j in range(len(probPaso)):
            tamPasox = np.random.normal(datax[i],sigma,100)
            tamPasoy = np.random.normal(datay[i],sigma,100)
            #Pa la derecha
            if (probPaso[j]<=0.25):
                datax[i] = datax[i]+tamPasox[j]
                datay[i] = datay[i]
                if(datax[i] > 30.5):
                    datax[i] = datax[i]-30.5
            #Pa la izquierda
            if (probPaso[j] > 0.25 and probPaso[j]<=0.50):
                datax[i] = datax[i]-tamPasox[j]
                datay[i] = datay[i]
                if(datax[i] < 0):
                    datax[i] = datax[i]+30.5
            #Suavecito para abajo
            if (probPaso[j] > 0.50 and probPaso[j]<=0.75):
                datax[i] = datax[i]
                datay[i] = datay[i]-tamPasoy[j]
                if(datay[i] < 0):
                    datay[i] = datay[i]+30.5
            #Suavecito para arriba
            if (probPaso[j] > 0.75 and probPaso[j]<=1):
                datax[i] = datax[i]
                datay[i] = datay[i]+tamPasoy[j]
                if(datay[i] > 30.5):
                    datay[i] = datay[i]-30.5
            if(i == 0):
                onex.append(datax[i])
                oney.append(datay[i])
        
        caminatax.append(datax[i])
        caminatay.append(datay[i])
    return np.array([onex, oney, caminatax, caminatay])

cCuad1 = np.copy(cuad1)
cCuad2 = np.copy(cuad2)

unPuntx0 = meGustaCaminar(cCuad1,cCuad2,0.25)[0]
unPunty0 = meGustaCaminar(cCuad1,cCuad2,0.25)[1]
posFinx = meGustaCaminar(cCuad1,cCuad2,0.25)[2]
posFiny = meGustaCaminar(cCuad1,cCuad2,0.25)[3]

unPuntx1 = meGustaCaminar(cCuad1,cCuad2,0.00025)[0]
unPunty1 = meGustaCaminar(cCuad1,cCuad2,0.00025)[1]

unPuntx2 = meGustaCaminar(cCuad1,cCuad2,2.5)[0]
unPunty2 = meGustaCaminar(cCuad1,cCuad2,2.5)[1]

fig4 = plt.figure(figsize = (8,6))
ax0 = fig4.add_subplot(111)
ax0.plot(unPuntx0, unPunty0, '.r-', label = 'Trayectoria de un solo punto')
ax0.legend()

plt.savefig('puntoCaminata.pdf')

fig5 = plt.figure(figsize = (8,6))
ax0 = fig5.add_subplot(111)
ax0.plot(posFinx, posFiny, '.k', label = 'Todos los puntos hicieeron recorrido')
ax0.legend()

plt.savefig('DistCaminata.pdf')

fig6 = plt.figure(figsize = (8,6))
ax0 = fig6.add_subplot(121)
ax0.plot(unPuntx1, unPunty1, '.b-', label = 'Trayectoria de un solo punto con sigma 0.00025')
ax0.legend()

ax1 = fig6.add_subplot(122)
ax1.plot(unPuntx2, unPunty2, '.b-', label = 'Trayectoria de un solo punto con sigma 2.5')
ax1.legend()

plt.savefig('sigmaCaminata.pdf')