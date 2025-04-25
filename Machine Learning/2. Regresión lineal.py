'''
La regresión lineal es un algoritmo de aprendizaje supervisado, para datos estructurados.
la regresión lineal es una aproximación para modelar la relación entre una variable escalar dependiente "y" y una o más variables explicativas "X".
La idea es dibujar una recta que indicará la tendencia del conjuntoi de datos.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/Housing.csv")
# print(casas.head()) # Visualizar primeros elementos
# print(casas.info()) # Información de cada una de las columnas
# print(casas.describe()) # Información estadística como: número de elementos, precio medio
# print(casas.columns) # Lista con los nombres de todas las columnas
# print('Price') # Ver la columna Price

# Ver la distribución del precio de nuestro dataset, mediante displot
sns.displot(casas['Price'])
# plt.show()
plt.close()

# Mapa de correlación entre las columnas numéricas del dataset
casas_numericas = casas.select_dtypes(include=np.number) # Seleccionar solo columnas numéricas
sns.heatmap(casas_numericas.corr(), annot=True)
plt.show()
plt.close()
