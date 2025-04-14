import numpy as np

# Numpy: Indexación en arrays de una dimensiión
array = np.arange(0,10)
print(array)

print(array[0]) # Imprime llamando por índice
print(array[1])
print(array[-1]) # La última del array
print(array[2:4]) # Rango de la posición 2 a la 4
print(array[:]) # Todo el array
print(array[5:]) # De la posición 5 hasta el final
print(array[:4]) # De la posición inicial 0 hasta la 4
print(array[0],array[1],array[6])

array2 = array.copy()
print(array2)
array2[0] = 100
print(array2)

# Numpy: Indexación en arrays de 2 o más dimensiones
array3 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # Matriz de dos dimensiones de 3x3
print(array3)

print(array3[0]) # Imprime la fila 0
print(array3[0:2]) # Imprime las fila 2 primeras filas
print(array3[0][0]) # Imprime el elemento de fila 0 y columna 0
print(array3[0, 0]) # Imprime el elemento de fila 0 y columna 0
print(array3[1][1]) # Imprime el elemento de fila 1 y columna 1
print(array3[:, 0]) # Imprime la columna 0
print(array3[:,: 2]) # Todas las filas, y columnas 0 y 1. Así obtenemos las dos primeras columnas
