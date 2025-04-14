import numpy as np

# Numpy arrays - números aleatorios
# rand
array1 = np.random.rand(5) # Números aleatorios entre 0 y 1 con una distribución uniforme, una dimensión
print(array1)
array2 = np.random.rand(2, 3) # Números aleatorios entre 0 y 1 con una distribución uniforme, dos dimensiones
print(array2)
#randn
array3 = np.random.randn(5) # Números aleatorios entre 0 y 1 con una distribución normal, una dimensión
print(array3)
array4 = np.random.randn(2, 3) # Números aleatorios entre 0 y 1 con una distribución normal, dos dimensiones
print(array4)
# randint
array5 = np.random.randint(1, 100) # Números aleatorios enteros entre 1 y 100, una dimensión
print(array5)
array6 = np.random.randint(1, 100, 12) # Números aleatorios enteros entre 1 y 100, dos dimensiones, 12 elementos
print(array6)
# reshape
matriz1 = array6.reshape(3, 4) # Mediante el método reshape podemos cambiar el número de filas(3) y columnas(4)
print(matriz1)

'''
Una distribución uniforme significa que todos los valores dentro de un intervalo dado tienen la misma probabilidad de ocurrir. No hay valores "más probables" que otros dentro del intervalo.
Una distribución normal, también conocida como distribución Gaussiana o "campana de Gauss", es una distribución de probabilidad continua que es simétrica alrededor de su media. Los valores cercanos a la media son más probables de ocurrir, y la probabilidad disminuye a medida que te alejas de la media en cualquier dirección. Está completamente definida por su media (el centro de la distribución) y su desviación estándar (la dispersión de los datos alrededor de la media).
'''