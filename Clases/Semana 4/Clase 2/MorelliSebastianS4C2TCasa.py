# TRANSFORMADA DE FOURIER EN 1D

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

signalruido = np.genfromtxt('signalruido.dat', delimiter=(','))

fig0 = plt.figure(figsize = (10,6))
ax = fig0.add_subplot(111)
ax.plot(signalruido[:,0],signalruido[:,1], 'r-', label = 'Signal Ruido')
ax.set_xlabel('time[s]')
ax.set_ylabel('Signal Ruido')
ax.set_title('Signal Ruido in function of time')
ax.legend()

plt.savefig('senial.png')

def Fourier(data):
    TransFou = np.array([])
    k = np.linspace(0,len(data[:,0]),len(data[:,0]),dtype=int)
    
    for i in range (len(data[:,0])):
        Trans = np.sum(data[:,1]*np.exp(-1j*2*np.pi*k*(int(i)/len(data[:,0]))))
        TransFou = np.append(TransFou, Trans)
    
    return TransFou

TransSignal = Fourier(signalruido)

def fftfreq(data):
    
    n = len(data)
    dif = np.abs(data[0,0]-data[1,0])
    if (n%2 == 0): 
    
        arrayEvenGen = np.array([])
        arrayEven1 = np.linspace(0, n/2, n/2, dtype=int)
        arrayEven2 = np.linspace(-n/2, -1, n/2, dtype=int)
        arrayEvenGen = np.append(arrayEvenGen, arrayEven1)
        arrayEvenGen = np.append(arrayEvenGen, arrayEven2)
        return arrayEvenGen/(dif*n)
    
    if (n%2 != 0):
        
        arrayOddGen = np.array([])
        arrayOdd1 = np.linspace(0, (n-1)/2, (n-1)/2, dtype=int)
        arrayOdd2 = np.linspace((-n-1)/2, -1, (n-1)/2, dtype=int)
        arrayOddGen = np.append(arrayOddGen, arrayOdd1)
        arrayOddGen = np.append(arrayOddGen, arrayOdd2)
        return arrayEvenGen/(dif*n)
    
freq = fftfreq(signalruido)
freqMetod = np.fft.fftfreq(len(signalruido), np.abs(signalruido[0,0]-signalruido[1,0]))

print('Los arrays encontrados para las frecuencias, por mi implementación y el método de numpy son iguales')

fig1 = plt.figure(figsize = (12,6))
ax = fig1.add_subplot(111)
ax.plot(freq, TransSignal, 'r', label = 'Transformada de Fourier')
ax.set_xlabel('Frecuencias')
ax.set_ylabel('Transformada de Fourier')
ax.set_title('Transformada de Fourier en función de la frecuencia')
ax.legend()

plt.savefig('FFTsenial.png')

def filtro(trans, frecuen):
    copyFou = np.copy(trans)
    for i in range (len(frecuen)):
        if(frecuen[i]>600 or frecuen[i]<-600):
            copyFou[i] = 0
    return copyFou   

filtrado = filtro(TransSignal, freq)

def FourierInv(data):
    TransFou = np.array([])
    k = np.linspace(0,len(data),len(data),dtype=int)
    
    for i in range (len(data)):
        Trans = np.sum(data*np.exp(1j*2*np.pi*k*(int(i)/len(data))))
        TransFou = np.append(TransFou, Trans/len(data))
    
    return TransFou

OrigFil = FourierInv(filtrado)

fig2 = plt.figure(figsize = (12,6))
ax = fig2.add_subplot(111)
ax.plot(signalruido[:,0], signalruido[:,1], 'r', label = 'Signal Ruido')
ax.plot(signalruido[:,0], OrigFil, 'b', label = 'Signal Ruido Filtrado')
ax.set_xlabel('time[s]')
ax.set_ylabel('Signal Ruido con y sin ruido')
ax.set_title('Signal Ruido con y sin ruido en función del tiempo')
ax.legend()

plt.savefig('senialfiltrada.png')