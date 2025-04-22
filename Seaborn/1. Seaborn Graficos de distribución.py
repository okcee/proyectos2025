import seaborn as sns
import matplotlib.pyplot as plt


propinas = sns.load_dataset('tips') # Cargamos un dataset que viene con la librería para hacer pruebas
print("Los primeros 10 elementos del dataset son: ")
print(propinas.head(10))
''' Dataset
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
6        8.77  2.00    Male     No  Sun  Dinner     2
7       26.88  3.12    Male     No  Sun  Dinner     4
8       15.04  1.96    Male     No  Sun  Dinner     2
9       14.78  3.23    Male     No  Sun  Dinner     2
'''
# La función distplot de Seaborn fue declarada obsoleta en la versión v0.11.0, una versión que incluyó varias funciones nuevas para graficar distribuciones de datos. Llamar a distplot en la versión v0.11.0 o posterior genera una advertencia instando al usuario a actualizar su código con una de las dos nuevas funciones: displot (sin la 't') o histplot.

# Gráfico Histograma (displot o histplot)

sns.displot(propinas['total_bill']) # Sobre la columna "total_bill" vamos a crear un gráfico tipo histograma
plt.show()

sns.histplot(propinas['total_bill']) # Sobre la columna "total_bill" vamos a crear un gráfico tipo histograma
plt.show()

# Configurar número de barras
sns.displot(propinas['total_bill'], bins=20) # Con el atributo bins cambiamos el número de barras
plt.show()
sns.displot(propinas['tip'], bins=30) # Con el atributo bins cambiamos el número de barras
plt.show()

# Gráfico de Dispersión (jointplot)
# jointplot! Es una excelente herramienta de Seaborn para visualizar la relación entre dos variables
sns.jointplot(x='total_bill', y='tip', data=propinas)
plt.title("Gráfico de dispersión")
plt.show()
# Hexágonos, Cuánto más oscuro es un hexágono más concentración
sns.jointplot(x='total_bill', y='tip', data=propinas, kind='hex') # Se cambio el tipo de gráfico de dispersión
plt.title("Hexágonos")
plt.show()
# Regresión lineal
sns.jointplot(x='total_bill', y='tip', data=propinas, kind='reg')
plt.title("Regresión lineal")
plt.show()

# Gráfico de densidad
# Gráfico KDE
sns.jointplot(x='total_bill', y='tip', data=propinas, kind='kde')
plt.title("Gráfico de densidad")
plt.show()

# pairplot. Para comparar todas las columnas de tipo numérico
sns.pairplot(propinas)
plt.title("Gráfico de comparación")
plt.show()

# Se puede sacar la comparación de todas las columnas de tipo numérica en función de una no numérica, como si esta última fuese la categoría
sns.pairplot(propinas, hue='sex')
plt.title("Gráfico de comparación en función de la categoría sex")
plt.show()
sns.pairplot(propinas, hue='size')
plt.title("Gráfico de comparación en función de la categoría")
plt.show()

# Gráfico rayas. Representa cada dato con una raya en la gráfica y se ve donde se acumula más
sns.rugplot(propinas('total_bill'))
plt.title("Gráfico rayas total_bill")
plt.show()
