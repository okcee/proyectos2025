import numpy as np

'''Ejercicio1
Generar N números aleatorios enteros entre un valor mínimo y máximo
Desarrolla una función llamada generar_numeros_enteros_aleatorios que tome como entrada el número de elementos N, un valor mínimo minimo y un valor máximo maximo, y utilice NumPy para generar una lista de N números enteros aleatorios en el rango [minimo, maximo].
def generar_numeros_enteros_aleatorios(N, minimo, maximo):
# Ejemplo de uso
N = 5
minimo = 1
maximo = 10
resultado = generar_numeros_enteros_aleatorios(N, minimo, maximo)
print(resultado)
Resultado:
[4, 10, 1, 8, 2]
'''
def generar_numeros_enteros_aleatorios (N, minimo, maximo):
    