import numpy as np
import pandas as pd

# Pandas: Tratamiento de datos nuelos o sin valor

diccionario = {'A':[4,5,np.nan], 'B':[6,1,5], 'C':[np.nan, 4, np.nan]}

dataframe = pd.DataFrame(diccionario)
print('El DataFrame original es:')
print(dataframe,'\n')

# Borra filas que contengan algún valor nulo.  dataframe.dropna()
print("Aplicando borrado de filas con datos nulos")
print(dataframe.dropna()) # Si no se pone inplace=True se considera temporal

# Borra columnas que contengan algún valor nulo.  dataframe.dropna(axis=1)
print("Aplicando borrado de columnas con datos nulos")
print(dataframe.dropna(axis=1))

# Rellena filas que contengan algún valor nulo.  dataframe.fillna(value=numero)
print("Aplicando rellenado de filas con datos nulos por valor 100")
print(dataframe.fillna(value=100))

# Rellena filas que contengan algún valor nulo.  dataframe.fillna(value=valor_medio) con los valores medios de cada columna
valor_medio = dataframe.mean()
print("Aplicando rellenado de filas con datos nulos por valor medio")
print(dataframe.fillna(value=valor_medio))

