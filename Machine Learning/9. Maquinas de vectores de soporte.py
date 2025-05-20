# CLASIFICACIÓN Y REGRESIÓN
# Máquinas d vectores de soporte (Support Vector Machine) SVM
''' SVM las máquinas de soporte vectorial son un conjunto de algoritmos de aprendizaje supervisado para resolver problemas de clasificación y regresión Dado un conjunto de ejemplos de entrenamiento podemos etiquetar las clases y entrenar una SVM para construir un modelo que prediga la clase de una nueva muestra.  
Representa los puntos de muestra en el espacio separando las clases en dos espacios lo más amplio posible mediante un hiperplano de separación que se denomina vector de soporte.  
Separamos los puntos verdes de los azules mediante unas líneas rectas o curvas que maximice el espacio entre las dos clases.  
Muestra una nueva clase según en qué espacio caigan en las verdes o en las azules las podemos etiquetar de una clase o de la otra.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flores = sns.load_dataset('iris') # Cargar dataset de ejemplo de Seaborn
# flores = pd.read_csv('S:\\_proyectos2025\\Machine Learning\\Datasets\\iris.csv') # Cargando uno propio
# print(flores.head(5))

flores['species'].unique()
sns.pairplot(flores)
# plt.show()
plt.close()

sns.pairplot(flores, hue='species') # Dividiendo el gráfico por especies
# plt.show()
plt.close()

# Pasamos al algoritmo de machine learnig
# Necesitamos definir las características, que serán todas las columnas menos la columna objetivo que son las especies, que realmente es lo queremos predecir.

from sklearn.model_selection import train_test_split
X = flores.drop('species', axis=1)
y = flores['species']

# Creamos las variables de entrenamiento y de test a partir de estos datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.svm import SVC
modelo = SVC(gamma='auto') # Instanciamos nuestro SVC para crear nuestro modelo
modelo.fit(X_train, y_train) # Entrenar el modelo
predicciones = modelo.predict(X_test) # Hacemos nuestras predicciones

print('Predicciones: \n', predicciones)
print('Datos reales: \n', y_test)

# Evaluación del modelo
from sklearn.metrics import classification_report, confusion_matrix
print('Precisiones del modelo: \n', classification_report(y_test, predicciones))
