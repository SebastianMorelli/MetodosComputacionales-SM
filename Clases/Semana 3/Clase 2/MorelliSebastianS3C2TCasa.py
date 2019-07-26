#ELIMINACIÓN POR GAUUSS-JORDAN PUNTO 1

import numpy as np
import matplotlib.pylab as plt

def GaussJordan (A,B):
    for i in range (len(A)):
        for j in range (len(A[i])):
            if(j == i):
                B[i] = B[i]/A[i,i]
                A[i,:] = A[i,:]/A[i,i]
            
            elif(j > i):
                B[j] = B[j]-((B[i])*(A[j,i]))
                A[j,:] = A[j,:]-((A[i,:])*(A[j,i]))
            
    for k in range (len(A)-1,-1, -1):
        for m in range (len(A[k])-1,-1, -1):
            if(m < k):
                B[m] = B[m]-((B[k])*(A[m,k]))
                A[m,:] = A[m,:]-((A[k,:])*(A[m,k]))
                
    return B

#MINIMOS CUADRADOS PUNTO 2

time = np.genfromtxt ('parabolico.dat', usecols=(0))
position = np.genfromtxt ('parabolico.dat', usecols=(1))

fig0 = plt.figure()
ax = fig0.add_subplot(111)
ax.plot(time, position, 'r', label = 'data')
ax.set_xlabel('time')
ax.set_ylabel('Position')
ax.legend()

plt.savefig('plotdatos.pdf')

MtxG = np.empty([len(time),3])

for i in range (len(time)):
    MtxG[i,0] = 1
    MtxG[i,1] = time[i]
    MtxG[i,2] = 0.5*(time[i])**2
    
MtxGTrans = MtxG.T
MtxA = np.dot(MtxGTrans,MtxG)
MtxB = np.dot(MtxGTrans,position)
m = GaussJordan(MtxA,MtxB)

Ajust = np.empty(0)
for i in range (len(time)):
    Ajust = np.append(Ajust, m[0]+m[1]*time[i]+m[2]*0.5*(time[i])**2)
    
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(time,Ajust, 'r', label = 'Ajuste')
ax.set_xlabel('time')
ax.set_ylabel('Ajuste')
ax.legend()

plt.savefig('plotAjustedatos.pdf')

#EJERCICIO EN CASA -PCA PUNTO 3

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

M = len(t)
k = np.linspace(1,M,9)
def sigma ():
    return (np.sum((u**k-u)*(v**k-v)))/M-1

print(sigma())