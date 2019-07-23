# CICLOS Y CONDICIONALES PUNTO 1

import numpy as np
x = np.int_(np.random.random(100)*900)
print("arreglo x: ",x)

for i in range (len(x)):
    if (x[i]%2 != 0 and x[i]<800):
        print(x[i])
    elif(x[i]>800):
        break
        
#FUNCIONES PUNTO 2

def division (v1,v2):
    return v1/v2

a=11
b=17
print(division(a,b))


# CICLOS Y CONDICIONALES PUNTO 3

y = np.int_(np.random.random(100)*900)
print("arreglo y: ", y)

min = y[0]
for i in range (len(y)):
    if(y[i] < min):
        min = y[i]
print(min)

npmin = np.min(y)
print(npmin)

if(min==npmin):
    print ('El valor hallado con numpy es', npmin, 'y el valor hallado con mi implementación es', min, '. Son igules Yayyyy')
else:
    print ('Algo salió mal:(')
    


# ARRAYS 2D PUNTO 4

N=np.random.randint(3 , 8)
print (N)
Mat=(np.random.random((N,N))*10.0)-7.0
print ("Matriz Mat: ", Mat)

for i in range (len(Mat)):
    counter = 0
    for j in range (len(Mat[i])):
        if(Mat[i,j]>2):
            counter = counter + 1
    if(counter<1):
        print (Mat[i,:])

        
# ARRAYS DE NUMPY, CICLOS Y SLICING PUNTO 5

### USANDO CICLOS

import numpy as np
N1=np.random.randint(30 , 80)
z = np.int_(np.random.random(N1)*150)
print("arreglo z: ",z)

lista1=[]
lista2=[]
for i in range (10):
    lista1.append(z[i])
print (lista1)

for j in range (N1-10, N1):
    lista2.append(z[j])
print(lista2)

result = np.array([])
for k in range (10):
    num = (lista1[k]+lista2[k])/len(z)
    result = np.append(result, num)
    
print(result)


### SIN USAR CICLOS

import numpy as np
N1=np.random.randint(30 , 80)
z = np.int_(np.random.random(N1)*150)
print("arreglo z: ",z)

(z[0:10]+z[N1-10:])/len(z)


#PROBLEMA DE GEOMETRIA PUNTO 6

import numpy as np
c = np.random.random(3)*300 -150 
print (c)

def radioMax (x0, y0, z0):
    distOrig = np.sqrt(x0**2+y0**2+z0**2)
    VolCube = (x0**4)*(y0**4)*(z0**4)
    return distOrig, VolCube
    
print(radioMax(c[0],c[1],c[2]))