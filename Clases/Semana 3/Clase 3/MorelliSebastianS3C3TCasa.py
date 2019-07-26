#PREPARACION CASA COVARIANZA PUNTO 1

import numpy as np
import matplotlib.pylab as plt

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([-12.,-45.,-6.,-78.,-34.,-22.,10.,-31.,27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

fig0 = plt.figure()
ax = fig0.add_subplot(111)
ax.plot(t, u, 'or-', label = 'Serie u')
ax.plot(t, v, 'ob-', label = 'Serie v')
ax.set_xlabel('time')
ax.set_ylabel('Series')
ax.legend()

plt.savefig('serie.pdf')

def FindsigmaCov (x,y):
    M = len(x)
    sigi = x - np.mean(x)
    sigj = y - np.mean(y)
    
    sigmaCov = (np.sum(sigi * sigj))/(M-1)
    return sigmaCov

def FindsigmaVar (x):
    M = len(x)
    sigi = x - np.mean(x)
    
    sigmaVar = (np.sum(sigi**2))/(M-1)
    return sigmaVar

print('La covarianza tiene un valor de', FindsigmaCov(u,v)) 
print('La varianza de u tiene un valor de', FindsigmaVar(u))
print('La varianza de v tiene un valor de', FindsigmaVar(v))

print('La covariancia entre u y v fue', FindsigmaCov(u,v), '. Esto significa las series de datos estan anti-correlacionadas',
      'ya que el resultado es un número grande pero negativo.' )

#MATRIZ DE COVARIANZA PUNTO 2 

MtxData = np.empty([2,len(u)])

for i in range (len(u)):
    MtxData[0,i] = u[i]
    MtxData[1,i] = v[i]
    
    
def FindMtxCov (Data):
    MtxCov = np.empty([len(Data),len(Data)])
    for i in range(len(Data)):
        for j in range(len(Data)):
            if (i == j):
                MtxCov[i,j] = FindsigmaVar(Data[i,:])
            else:           
                MtxCov[i,j] = FindsigmaCov(Data[i,:],Data[j,:])
    return MtxCov

CovData = FindMtxCov(MtxData)
print(CovData)

#MATRIZ DE COVARIANZA AUTOVALORES Y AUTOVECTORES PUNTO 3

Temp1 = np.genfromtxt('room-temperature.csv', usecols=(1), skip_header=(1), delimiter = ',')
Temp2 = np.genfromtxt('room-temperature.csv', usecols=(2), skip_header=(1), delimiter = ',')
Temp3 = np.genfromtxt('room-temperature.csv', usecols=(3), skip_header=(1), delimiter = ',')
Temp4 = np.genfromtxt('room-temperature.csv', usecols=(4), skip_header=(1), delimiter = ',')

MtxTemp = np.empty([4,len(Temp1)])

for i in range (len(Temp1)):
    MtxTemp[0,i] = Temp1[i]
    MtxTemp[1,i] = Temp2[i]
    MtxTemp[2,i] = Temp3[i]
    MtxTemp[3,i] = Temp4[i]

CovTemp = FindMtxCov(MtxTemp)
print(CovTemp)

fig1 = plt.figure(figsize=(15,7))
ax0 = fig1.add_subplot(221); ax1 = fig1.add_subplot(222); ax2 = fig1.add_subplot(223); ax3 = fig1.add_subplot(224);
ax0.plot(Temp1, '.r-', label = 'Temp1')
ax0.legend()
ax1.plot(Temp2, '.b-', label = 'Temp2')
ax1.legend()
ax2.plot(Temp3, '.g-', label = 'Temp3')
ax2.legend()
ax3.plot(Temp4, '.C1-', label = 'Temp4')
ax3.legend()

plt.savefig('serieTemp.pdf')

eigVecVal = np.linalg.eig(CovTemp)
print(eigVecVal)