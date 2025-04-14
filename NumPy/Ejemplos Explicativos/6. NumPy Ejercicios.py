import numpy as np

'''Ejercicio 1
Crea una lista de números secuenciales con el valor mínimo de 10 y el valor máximo de 39.
Convierte esta lista en una lista o matriz de 2 dimensiones (3 filas por 10 columnas).
Muestra por pantalla el valor del elemento de la esquina superior derecha de la matriz
'''
array = np.arange(10, 40)
list = array # Pasamos el array a una lista
print("El array como una lista: \n", list)
matriz = array.reshape(3, 10)  # Pasamos el array, mediante el método reshape podemos establecer el número de filas(3) y columnas(10)
print("El array como una matriz 3x10 es: \n", matriz)
print("El valor del elemento de la esquina superior derecha de la matriz es: ", matriz[0][-1])

'''Ejercicio 2
Crea un array de una dimensión con 9 valores enteros aleatorios entre 0 y 100.
Convierte ese array en una matriz de 2 dimensiones (3 filas y 3 columnas).
Muestra por pantalla el valor del elemento de la matriz, de la esquina inferior derecha.
'''
array2 = np.random.randint(0, 101, 9) # Números aleatorios enteros entre 0 y 101, dos dimensiones, 9 elementos
print("El array2 es: \n", array2)
matriz1 = array2.reshape(3, 3)   # Pasamos el array, mediante el método reshape podemos establecer el número de filas(3) y columnas(3)
print("La matriz1 es: \n", matriz1)
print("El valor del elemento de la matriz, de la esquina inferior derecha es: ", matriz1[2][-1])
