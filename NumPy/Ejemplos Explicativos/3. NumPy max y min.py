import numpy as np

# Averiguar valores máximos y mínimos de arrays
array1 = np.random.randint(1, 100, 50)
print("El array aleatorio generado es:/n",array1)
print(type(array1))

valor_maximo = array1.max() # Saber el valor máximo en el array, el número de mayor valor.
posicion_valor_maximo = array1.argmax() # Saber la posición del valor máximo.
print("El valor máximo es:",valor_maximo)
print("La posición del valor máximo es:",posicion_valor_maximo)

valor_minimo = array1.min() # Saber el valor mínimo en el arrya, el número de menor valor.
posicion_valor_minimo = array1.argmin() # Saber la posición del valor mínimo.
print("El valor mínimo es:",valor_minimo)
print("La posición del valor mínimo es:",posicion_valor_minimo)
