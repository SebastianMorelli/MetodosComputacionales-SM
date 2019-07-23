#########################################################################################
#########################################################################################
# Ejercicio 
#a) Inicializar dos variables (con valores escogidos por ustedes), una entera y otra flotante.\\

Variableint = 11
VariableFloat = 8.0

#b) Imprimir los valores de las variables en un mensaje:\\
#\verb"la primera tiene un valor de XX y la segunda variable tiene un valor de YY"\\

print('La primera variable tiene un valor de ', Variableint, ' y la segunda un valor de ', VariableFloat)

#c) Calcular el valor de la segunda variable dividida por la primera e imprimir : \verb"El resultado es ZZ" \\
		
    
ZZ = VariableFloat/Variableint
print('El resultado  es ', ZZ)

#d) Crear una lista con los elementos: 101, 26, rio, gato, 31 y 28 e imprimirla.\\

lista1 = [ 101, 26, 'rio', 'gato', 31, 28]
print(lista1)

#e) Agregarle a esa lista los elementos: 257, 348, 583 \\

lista1.extend([257, 348, 583])
print(lista1)

#f) Hacer una iteracion para recorrer dicha lista e imprimir sus elementos.\\

for i in range(len(lista1)):
    print (lista1[i])

#g) Eliminar el tercer elemento de la lista e imprimirla nuevamente.\\

lista1.pop(3)
print (lista1)

#h) Calcular la longitud de la lista e imprimir: \verb"la longitud de la lista es XX"\\

XX = len(lista1)
print ('La longitud de la lista es', XX)

#End