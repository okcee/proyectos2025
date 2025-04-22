import numpy as np

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

#Lista de 1 dimensión
lista = [1, 2, 3, 4, 5]
array_numpy = np.array(lista)
print(array_numpy)
print(type(array_numpy))
#Lista de 2 dimensiones
lista2 = [1,2,3], [4,5,6], [7,8,9]
array2 = np.array(lista2)
print(type(array2))
print(array2)
# Numpy arrays: arange, zeros, ones, linspace, eye
array_arange = np.arange(0, 10, 2) # Matriz de una dimensión, de 0 a 10 cada 2 elementos
print("Array arange")
print(array_arange)
print(type(array_arange))

array_zeros = np.zeros(3)  # Matrices de ceros
array_zeros2 = np.zeros((3,4))
print("Array zeros")
print(array_zeros)
print(array_zeros2)

array_ones = np.ones(3) # Matrices de unos
array_ones2 = np.ones((3,4))
print("Array ones")
print(array_ones)
print

array_linspace = np.linspace(0, 10, 5) # 5 elemnstos entre el 0 y el 10
print("Array linspace")
print(array_linspace)
print(type(array_linspace))

array_eye = np.eye(4) # Matriz identidad, mismo número de filas y columnas con matriz diagonal de unos
print("Array eye")
print(array_eye)
print(type(array_eye))
