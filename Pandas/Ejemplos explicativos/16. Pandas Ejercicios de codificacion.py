import pandas as pd
import numpy as np

'''Ejercicio de codificación 8
Calcular promedio
Desarrolla una función llamada calcular_promedio que tome como entrada un DataFrame de pandas que contiene datos numéricos y calcule el promedio de cada columna. La función debe devolver un nuevo DataFrame que contenga los promedios de cada columna.
def calcular_promedio(dataframe):
# Ejemplo de uso
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)
resultado = calcular_promedio(df)
print(resultado)

Resultado
A     2.5
B     6.5
C    10.5
dtype: float64
'''
print('Inicio del Ejercicio 8')
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

def calcular_promedio(dataframe):
    promedios = dataframe.mean()
    return promedios

resultado = calcular_promedio(df)
print(resultado)
print('Fin del Ejercicio 8','\n')


'''Ejercicio de codificación 9 - Practicar con pandas y la función query()
Seleccionar datos
Desarrolla una función llamada seleccionar_datos que tome como entrada un DataFrame de pandas que contiene información sobre estudiantes (por ejemplo, nombre, edad, calificaciones, etc.) y seleccione un subconjunto de datos basado en ciertos criterios.
Los criterios se pueden basar en el nombre, edad o calificaciones

def seleccionar_datos(dataframe, criterio):
# Ejemplo de uso
data = {
    'nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'edad': [20, 22, 18, 25],
    'calificaciones': [90, 88, 75, 95]
}

df = pd.DataFrame(data)
criterio = 'edad > 18'
resultado = seleccionar_datos(df, criterio)
print(resultado)
    nombre  edad  calificaciones
0  Alice    20              90
1    Bob    22              88
3  David    25              95
'''
print('Inicio del Ejercicio 9')
data = {'nombre': ['Alice', 'Bob', 'Charlie', 'David'], 'edad': [20, 22, 18, 25], 'calificaciones': [90, 88, 75, 95]}
df = pd.DataFrame(data)
criterio = 'edad > 18'

def seleccionar_datos(dataframe, criterio):
    df_filtrado = dataframe.query(criterio)
    return df_filtrado

resultado = seleccionar_datos(df, criterio)
print(resultado)
print('Fin del Ejercicio 9','\n')

''' Ejercicio de codificación 10 - Practicar con pandas y sus funciones mean() y fillna()
Rellenar Valores Nulos con la Media de una Columna
Desarrolla una función llamada rellenar_con_media que tome como entrada un DataFrame de pandas y el nombre de una columna. La función debe calcular la media de esa columna y luego llenar los valores nulos en esa columna con la media calculada.

def rellenar_con_media(dataframe, columna):

# Ejemplo de uso
data = {
    'nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'edad': [20, None, 18, 25, None],
    'calificaciones': [90, 88, None, None, 95]
}

df = pd.DataFrame(data)
columna = 'calificaciones'

resultado = rellenar_con_media(df, columna)
print(resultado)

Resultado:
    nombre  edad  calificaciones
0    Alice  20.0            90.0
1      Bob   NaN            88.0
2  Charlie  18.0            91.0
3    David  25.0            91.0
4      Eve   NaN            95.0
'''
print('Inicio del Ejercicio 10')

data = {
    'nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'edad': [20, None, 18, 25, None],
    'calificaciones': [90, 88, None, None, 95]
}
df = pd.DataFrame(data)
columna = 'calificaciones'

def rellenar_con_media(dataframe, columna):
    media = dataframe[columna].mean()
    dataframe[columna] = dataframe[columna].fillna(media)
    return dataframe

resultado = rellenar_con_media(df, columna)
print(resultado)

print('Fin del Ejercicio 10','\n')
