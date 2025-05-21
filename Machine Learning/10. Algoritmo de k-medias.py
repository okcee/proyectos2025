# Algoritmo de k-medias
'''
El algoritmo de k medias el algoritmo de k medias es un algoritmo de aprendizaje no supervisado para resolver el problema de la clusterización.  
Tiene como objetivo la partición de un conjunto de n observaciones en k grupos en el que cada observación pertenece al grupo cuyo valor medio es más cercano.  
Es un método utilizado en minería de datos.  
Aquí tienes un gráfico para distintas fases que pasa el algoritmo para conseguir agrupar las observaciones en tres grupos.  
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

# Usamos make_blobs para generar los datos para estas pruebas

datos = make_blobs(n_samples=200, n_features=2, centers=4) # Definimos el nº de ejemplos que vamos a generar, el nº de características que va a tener y el número de centros (grupos que queremos generar)

# print('Datos: \n', datos)

plt.scatter(datos[0][:,0], datos[0][:,1])
# plt.show()
plt.close()

# Ahora vamos a generar el algoritmo de las k-medias
from sklearn.cluster import KMeans
modelo = KMeans(n_clusters=4) # Instanciamos KMeans dentro del modelo creado y le pasamos el número de centros que queremos generar
modelo.fit(datos[0]) # Entrenamos el modelo

print('Modelo: \n', modelo)
print('Modelo: \n', modelo.cluster_centers_) # Saber los datos de los 4 grupos
print('Grupos que hemos asignado: \n', modelo.labels_) # Ver la agrupación de datos generada

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,4))

# Gráfico 1
ax1.scatter(datos[0][:,0], datos[0][:,1], c=modelo.labels_)
ax1.set_title('Algoritmos de k-medias')
# Gráfico 2
ax2.scatter(datos[0][:,0], datos[0][:,1], c=datos[1])
ax2.set_title('datos originales')

plt.show()
plt.close()