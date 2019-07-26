#EJERCICIO DATOS MÉDICOS PUNTO 1

import numpy as np
import matplotlib.pylab as plt

Data = np.genfromtxt('WDBC.dat', 
                     usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31), 
                     delimiter = (','))
DataT = np.transpose(Data)
print(DataT)

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

def FindMtxCov (Data):
    MtxCov = np.empty([len(Data),len(Data)])
    for i in range(len(Data)):
        for j in range(len(Data)):
            if (i == j):
                MtxCov[i,j] = FindsigmaVar(Data[i,:])
            else:           
                MtxCov[i,j] = FindsigmaCov(Data[i,:],Data[j,:])
    return MtxCov

MtxCovTum = FindMtxCov(DataT)
print(MtxCovTum)

eigValVec = np.linalg.eig(MtxCovTum)
print(eigValVec)
eigVal = eigValVec[0]
eigVec = eigValVec[1]

contBen = 0; contMal = 0
for i in range (len(Data)):
    if(Data[i,0]== 1):
        contBen = contBen + 1
        
    if(Data[i,0]==0):
        contMal = contMal + 1