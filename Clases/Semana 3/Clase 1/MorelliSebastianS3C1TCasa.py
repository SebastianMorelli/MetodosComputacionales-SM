#GAUSS-JORDAN Y MATRICES PUNTO 1

import numpy as np
A=np.array([[8.,2.,1.],[1.,-2.,-3.],[-1.,1.,2,]])
A1=np.array([[8.,2.,1.],[1.,-2.,-3.],[-1.,1.,2,]])

B=np.array([-8.,0.,3.])
B1=np.array([-8.,0.,3.])

for i in range (len(A)):
    for j in range (len(A[i])):
        if(j == i):
            B[i] = B[i]/A[i,i]
            A[i,:] = A[i,:]/A[i,i]
            print(A,B)
        elif(j > i):
            B[j] = B[j]-((B[i])*(A[j,i]))
            A[j,:] = A[j,:]-((A[i,:])*(A[j,i]))
            print(A,B)
            
for k in range (len(A), -1):
    for m in range (len(A[k]), -1):
        if(m > k):
            B[m] = B[m]-((B[k])*(A[m,k]))
            A[m,:] = A[m,:]-((A[k,:])*(A[m,k]))
            
print(A,B)

print (np.linalg.solve(A1,B1))
print (np.linalg.inv(A1))


#GAUSS-JORDAN PARA MATRICES ALEATORIAS PUNTO 2

N=np.random.randint(3 , 8)
print (N)
Arreglo=(np.random.random((N,N))*10.0)-5.0
B=(np.random.random((N,1))*10.0)-5.0

print (Arreglo)
print (B)