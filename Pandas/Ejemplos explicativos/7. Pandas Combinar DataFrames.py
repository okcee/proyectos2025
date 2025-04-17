import pandas as pd

# Pandas: Combinar DataFrames

diccionario1 = {'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}
dataframe1 = pd.DataFrame(diccionario1)
print('El dataframe inicial es:')
print(dataframe1, '\n')

diccionario2 = {'A':[11,12,13], 'B':[14,15,16], 'C':[17,18,19]}
dataframe2 = pd.DataFrame(diccionario2)
print('El dataframe inicial es:')
print(dataframe2, '\n')

# Se pueden concatenar porque tienen el mismo número de filas y de columnas pd.concat()

print('El resultado de concatenar dataframe1 y dataframe 2 es:')
print(pd.concat([dataframe1, dataframe2]), '\n') # Los combina hacia abajo, por lo que añade el dataframe2 debajo del dataframe1

print('El resultado de concatenar dataframe1 y dataframe 2 con axis=1 es:')
print(pd.concat([dataframe1, dataframe2], axis=1), '\n') # Los combina hacia la derecha, por lo que añade el dataframe2 a la derecha del dataframe1

