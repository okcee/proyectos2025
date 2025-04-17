import numpy as np
import pandas as pd

# Pandas: Merge en DataFrames

diccionario1 = {'A':[1,2,3], 'B':[4,5,6], 'clave':['c1','c2', 'c3']}
dataframe1 = pd.DataFrame(diccionario1)
print('--- dataframe 1 ---')
print(dataframe1, '\n')

diccionario2 = {'C':[11,12,13], 'D':[14,15,16], 'clave':['c1','c2', 'c3']}
dataframe2 = pd.DataFrame(diccionario2)
print('--- dataframe 2 ---')
print(dataframe2, '\n')

# Hacemos el Merge de los 2 dataframes
# pd.merge(dataframe1, dataframe2, on='clave') Le decimos sobre que columna va a hacer el Mergue
dataframe3 = pd.merge(dataframe1, dataframe2, on='clave')
print('--- dataframe 3 ---')
print(dataframe3, '\n')
