import pandas as pd

# DataFrame: Modificación de los nombres de las filas

filas = 'ventas1 ventas2 ventas3'.split() # método split() para dividir una cadena en varios valores
columnas = 'zonaA zonaB zonaC'.split()
datos = [[120,340,250],[210,450,250],[310, 210, 140]]
dataframe = pd.DataFrame(datos,filas,columnas)
print('El DataFrame original es:')
print(dataframe,'\n')

# Primero se crea los nuevos nombres de fila
nuevas_filas = 'dia1 dia2 dia3'.split()
dataframe['dias'] = nuevas_filas

# Se procede al cambio mediante dataframe.set_index('dias')

print('El nuevo DataFrame es:')
print(dataframe.set_index('dias')) # Para cambio temporal

dataframe2 = dataframe.set_index('dias')
print('El nuevo DataFrame pasa a ser:')
print(dataframe2) # Para cambio permanente
