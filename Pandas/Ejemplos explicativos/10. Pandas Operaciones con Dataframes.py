import pandas as pd

# Pandas: Operaciones

diccionario1 = {'A':[11,12,10,12], 'B':[14,18,16,17]}
dataframe1 = pd.DataFrame(diccionario1, index=['i1', 'i2', 'i3', 'i4'])
print('--- dataframe 1 ---')
print(dataframe1, '\n')

# Cómo ver si un elemento está repetido
# Podemos sacar un array de los elementos únicos, los que no se repiten
print('Valores únicos en la columna A')
print(dataframe1['A'].unique(), '\n')

# Podemos saber también el número de valores unicos
print('Número de valores únicos en la columna A')
print(dataframe1['A'].nunique(), '\n')

# Podemos contar el número de ocurrencias que tiene cada valor (value_conts)
print('Contar las apariciones de los valores en la columna A')
print(dataframe1['A'].value_counts(), '\n')

# Podemos definir una función que dado un número, devuelve ese numero multiplicado por 2 y, podemos aplicarle la función a una columna del Dataframe
def multiplicar(x):
    return x*2
print('Aplicamos la función "multiplicar"(x*2) a los elementos de la columna A')
print(dataframe1['A'].apply(multiplicar), '\n')

# También se puede aplicar una función lambda a los elementos de un dataframe
print('Usamos una función lambda (x*3) con los elementos de la columna A')
print(dataframe1['A'].apply(lambda x: x*3), '\n')

# Método Drop para borrar una columna
print('Borramos la columna B con el método drop')
print(dataframe1.drop('B', axis=1), '\n')

# Método Drop para borrar una fila
print('Borramos la fila i1 con el método drop')
print(dataframe1.drop('i1'), '\n')

# Saber los nombres de todas las columnas de un dataframe
print('Obtener los nombres de todas las columnas del dataframe1')
print(dataframe1.columns, '\n') # Los nombres de las columnas

# Saber los nombres de todas las filas de un dataframe
print('Obtener los nombres de todas las columnas del dataframe1')
print(dataframe1.index, '\n') # Los nombres de las filas, que son los índices

# Ordenar los valores por la columna B
print('Ordenar los valores por la columna B')
print(dataframe1.sort_values('B'), '\n')
