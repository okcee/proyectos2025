import numpy as np
import pandas as pd

# DataFrames
filas1 = ["ventas 1", "ventas 2", "ventas 3"]
columnas1 = ["zona A", "zona B", "zona C"]
datos1 = [[123,421,256],[234,541,257],[120,451,258]]

dataframe = pd.DataFrame(datos1,filas1,columnas1) # Obtenermos una tabla de 3 x 3
print("El dataframe 1 es: ")
print(dataframe)

# Seleccionar Filas
print("La primera fila del dataframe 1 es: ") # Usamos el método dataframe.loc[""]
print(dataframe.loc["ventas 1"])

print("Para seleccionar varias filas del dataframe 1 es: ") # Hay que poner una lista de valores en vez de un valor. Usamos [["",""]]
print(dataframe.loc[["ventas 2", "ventas 3"]])

# Seleccionar Columnas
print("La primera columna del dataframe 1 es: ") # Usamos el método dataframe[""]
print(dataframe["zona A"])

print("Para seleccionar varias columnas del dataframe 1 es: ")  # Hay que poner una lista de valores. Usamos dataframe[["",""]]
print(dataframe[["zona A", "zona C"]])

# Seleccionar Elementos
print("Para seleccionar un valor conreto del dataframe 1 es: ") # Usamos dataframe.loc[""][""]
print(dataframe.loc["ventas 1"][ "zona A"])

# Añadir una columna
# "Para añadir una columna al dataframe 1 es: " Usamos dataframe.loc[""]
dataframe["TodasLasZonas"] = dataframe["zona A"] + dataframe["zona B"] + dataframe["zona C"]
print(" El valor del nuevo dataframe1 añadiendo una nueva columna es:\n", dataframe)

# Excluye una columna
# "Para excluír una columna del dataframe 1 es: " Usamos dataframe.drop("NombreColumna", axis=1) donde axis hace referencia a que es una columna y se define la cantidad =1
print("Imprime sin una columna", dataframe.drop("TodasLasZonas", axis=1))
print("No la borra", dataframe)

# Borrar una columna
# "Para borrar una columna del dataframe 1 es: " Usamos dataframe.drop("NombreColumna", axis=1) donde axis hace referencia a que es una columna y se define la cantidad =1, pero añadimos el parámetro inplace=True
# Opción 1: dataframe1 = dataframe1.drop("TodasLasZonas", axis=1)
dataframe.drop("TodasLasZonas", axis=1, inplace=True) # Tal que así
print(" El valor del nuevo dataframe1 comprobando que quedo borrada una columna es:\n", dataframe)

# Excluír una fila
print("El valor del dataframe1 excluyendo la fila ventas 3 es:\n", dataframe.drop("ventas 3"))
print("No la borra", dataframe)

# Borrar una fila
dataframe.drop("ventas 3", inplace=True)
print("El valor del dataframe1 borrando la fila es:\n", dataframe)

