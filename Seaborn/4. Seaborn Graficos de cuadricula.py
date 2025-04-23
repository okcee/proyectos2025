from matplotlib import pyplot as plt
import seaborn as sns

flores = sns.load_dataset('iris') # Cargamos un dataset que viene con la librería para hacer pruebas
print("Los primeros 5 elementos del dataset son: ")
print(flores.head())
''' Dataset
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
'''

# Seaborn: Gráficos de cuadrícula (grids): PairGrid y FacetGrid
# Creamos un gráfico pairplot para comparar 2 a 2, los datos entre columnas de datos numéricos
sns.pairplot(flores)
plt.title("Conjunto de gráficos Pairplot")
# plt.show()
plt.close()
# Si queremos tener más control sobre los tipos de gráficos que se ponen en el conjunto, utilizaremos otro tipo de gráfico que se llama PairGrid
graficos = sns.PairGrid(flores) # definimos una variable graficos
graficos.map(plt.scatter) # Vamos a poner gráficos de puntos Scatter a todos los gráficos del conjunto
plt.title("Conjunto de gráficos Pairplot")
# plt.show()
plt.close()
# Dibujamos gráficos directamente sobre un objeto Axes de Matplotlib que se les proporciona (que es lo que PairGrid les pasa a través de las funciones map_)
# PairGrid
graficos = sns.PairGrid(flores) # Así creamos las gráficas (sus ejes)
graficos.map_diag(sns.histplot) # Aquí asignamos el tipo de gráfico que queremos, en este aso un gráfico tipo Histograma (displot) sobre la diagonal principal de los gráficos (map_diag)
graficos.map_upper(plt.scatter) # map_upper - parte superior de la diagonal
graficos.map_lower(sns.kdeplot) # map_lower - parte inferior de la diagonal
plt.suptitle("Conjunto de gráficos Pairplot", y=1.02)
# plt.show()
plt.close()
# FacetGrid
propinas = sns.load_dataset('tips')
propinas.head()
print(propinas.head())
''' Dataset
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''
# Para saber cuantos valores únicos y diferentes hay para una columna
print(propinas['time'].unique())
'''
['Dinner', 'Lunch']
Categories (2, object): ['Lunch', 'Dinner']
'''
print(propinas['sex'].unique())
'''
['Female', 'Male']
Categories (2, object): ['Male', 'Female']
'''
print(propinas['day'].unique())
'''
['Sun', 'Sat', 'Thur', 'Fri']
Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']
'''
graficos2 = sns.FacetGrid(data=propinas, col='time', row='smoker')
graficos2.map(sns.histplot, 'total_bill')
graficos3 = sns.FacetGrid(data=propinas, col='time', row='smoker')
graficos3.map(plt.scatter, 'total_bill', 'tip')
plt.suptitle("Conjunto de gráficos Facetplot", y=1.02)
plt.show()
plt.close()