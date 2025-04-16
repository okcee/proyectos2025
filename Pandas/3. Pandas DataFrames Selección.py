import pandas as pd
import numpy as np

# DataFrame: Selección de datos con una condición

filas = 'ventas1 ventas2 ventas3'.split() # método split() para dividir una cadena en varios valores
columnas = 'zonaA zonaB zonaC'.split()
datos = [[120,340,250],[210,450,250],[310, 210, 140]]
dataframe = pd.DataFrame(datos,filas,columnas)
print('El DataFrame original es:')
print(dataframe,'\n')

# Seleccionar según una determinada condición dentro de una zona, Columna
print('Seleccionar según una determinada condición')
condicion1 = dataframe > 200
print(dataframe[condicion1],'\n')


print('Seleccionar una columna del DataFrame')
condicion5 = ['zonaB']
print(dataframe[condicion5],'\n')

print("Seleccionar varias columnas del DataFrame, hay que hacerlo mediante una lista")
condicion6 = ['zonaA','zonaB']
print(dataframe[condicion6],'\n')

print("Por un valor")
condicion2 = dataframe['zonaA'] > 200
print(dataframe[condicion2],'\n')

print("Por más de un valor")
condicion3 = (dataframe['zonaA'] > 200) & (dataframe['zonaB'] > 300) # & = AND
print('AND')
print(dataframe[condicion3],'\n')

condicion4 = (dataframe['zonaA'] > 200) | (dataframe['zonaB'] > 300) # (Símbolo Pipe) | = OR
print('OR')
print(dataframe[condicion4],'\n')
