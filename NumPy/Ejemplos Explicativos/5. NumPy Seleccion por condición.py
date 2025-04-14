import numpy as np

# Numpy: Seleccionar elementos de una array según una condición
array = np.arange(1,19) # Crea un array NumPy con números del 1 al 18.
print("El array es:",array) # Imprime el array creado.

condicion1 = array > 5 # Crea una máscara booleana: True si el elemento es mayor que 5, False en caso contrario.
print(condicion1) # Imprime la máscara booleana.

array2 = array[condicion1] # Selecciona los elementos de 'array' donde 'condicion1' es True.
print(array2) # Imprime el nuevo array con los elementos seleccionados.

array3 = array[array > 8] # Selecciona directamente los elementos de 'array' que son mayores que 8.
print(array3) # Imprime el nuevo array con los elementos seleccionados.

array4 = array[array % 2 == 0] # Selecciona los elementos de 'array' que son pares (resto de la división por 2 es 0).
print(array4) # Imprime el nuevo array con los elementos pares.

array5 = array[array % 2 != 0] # Selecciona los elementos de 'array' que son impares (resto de la división por 2 no es 0).
print(array5) # Imprime el nuevo array con los elementos impares.

# Numpy: Operaciones sobre un array

array6 = np.arange(0,10) # Crea un array NumPy con números del 0 al 9.
print("El array es:",array6) # Imprime el array creado.
print(array6 + 2) # Suma 2 a cada elemento del array e imprime el resultado.
print(array6 - 2) # Resta 2 a cada elemento del array e imprime el resultado.
print(array6 * 2) # Multiplica cada elemento del array por 2 e imprime el resultado.
print(array6 / 2) # Divide cada elemento del array por 2 e imprime el resultado.
print(array6 ** 2) # Eleva cada elemento del array al cuadrado e imprime el resultado.
print(array6 * 100) # Multiplica cada elemento del array por 100 e imprime el resultado.
print(array6 + array6) # Suma el array consigo mismo elemento a elemento e imprime el resultado.
print(array6 - array6) # Resta el array consigo mismo elemento a elemento e imprime el resultado.
print(array6 * array6) # Multiplica el array consigo mismo elemento a elemento e imprime el resultado.
print(array6 / array6) # Divide el array consigo mismo elemento a elemento e imprime el resultado (puede generar NaN o inf para la división por cero).
print(array6 ** array6) # Eleva cada elemento del array a la potencia de sí mismo e imprime el resultado (puede generar valores grandes o NaN).
print(np.sqrt(array6)) # Calcula la raíz cuadrada de cada elemento del array e imprime el resultado.
print(np.exp(array6)) # Calcula la exponencial (e^x) de cada elemento del array e imprime el resultado.
print(np.mean(array6)) # Calcula la media (promedio) de los elementos del array e imprime el resultado.
print(np.std(array6)) # Calcula la desviación estándar de los elementos del array e imprime el resultado.
print(np.var(array6)) # Calcula la varianza de los elementos del array e imprime el resultado.
print(np.sin(array6)) # Calcula el seno de cada elemento del array (en radianes) e imprime el resultado.
print(np.cos(array6)) # Calcula el coseno de cada elemento del array (en radianes) e imprime el resultado.
print(np.tan(array6)) # Calcula la tangente de cada elemento del array (en radianes) e imprime el resultado.
print(np.log(array6)) # Calcula el logaritmo natural de cada elemento del array e imprime el resultado (puede generar -inf o NaN para el logaritmo de 0).
print(np.max(array6)) # Encuentra el valor máximo en el array e imprime el resultado.
print(np.min(array6)) # Encuentra el valor mínimo en el array e imprime el resultado.
print(np.argmax(array6)) # Encuentra el índice (posición) del valor máximo en el array e imprime el resultado.
print(np.argmin(array6)) # Encuentra el índice (posición) del valor mínimo en el array e imprime el resultado.
print(np.sort(array6)) # Devuelve una copia ordenada (de menor a mayor) del array e imprime el resultado.
print(np.argsort(array6)) # Devuelve los índices que ordenarían el array original e imprime el resultado.
