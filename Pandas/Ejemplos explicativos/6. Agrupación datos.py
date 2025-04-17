import pandas as pd

# Pandas: Agrupación de datos

diccionario = {'dias':['dia1','dia1','dia2','dia2','dia3'],
               'vendedores':['Antonio','Maria','Jose','Marta','Juan'],
               'ventas':[100,400,200,500,300]}

print('El diccionario original es:')
print(diccionario)

dataframe1 = pd.DataFrame(diccionario)
print('El dataframe1 original es:')
print(dataframe1,'\n')

# Para agrupar los datos de ventas

dataframe2 = dataframe1.groupby('dias').mean(numeric_only=True) # dataframe1.groupby('dias') genera un objeto de tipo groupby y podemos establecer por ejemplo la media de los valores (mean())
print('El dataframe2, Media agrupando los días:')
print(dataframe2,'\n')

dataframe3 = dataframe1.groupby('dias').sum() # dataframe1.groupby('dias') genera un objeto de tipo groupby y podemos establecer por ejemplo la suma de los valores de vcentas por dia (sum())
print('El dataframe3, Suma de los valores por día:')
print(dataframe3,'\n')

dataframe4 = dataframe1.groupby('dias').describe()  # dataframe1.groupby('dias') genera un objeto de tipo groupby y podemos obtener estadísticas de los datos de nuestro dataframe agrupados por la columna dias (describe())
print('El dataframe4, Estadisticas del DataFrame por día:')
print(dataframe4,'\n')
