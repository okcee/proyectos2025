import pandas as pd

# Pandas: Join en DataFrames

diccionario1 = {'A':[1,2,3,4], 'B':[4,5,6,7]}
dataframe1 = pd.DataFrame(diccionario1, index=['i1', 'i2', 'i3', 'i4'])
print('--- dataframe 1 ---')
print(dataframe1, '\n')

diccionario2 = {'C':[11,12,13], 'D':[14,15,16]}
dataframe2 = pd.DataFrame(diccionario2, index=['i1', 'i2', 'i3'])
print('--- dataframe 2 ---')
print(dataframe2, '\n')

# Hacemos el Join de los 2 dataframes

dataframe3 = dataframe1.join(dataframe2)
print('--- dataframe 3 ---')
print(dataframe3, '\n')
