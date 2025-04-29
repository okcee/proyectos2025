''' k vecinos más cercanos - KNN
El método de los k vecinos más cercanos es un método de clasificación supervisada, que estima la probabilidad de que un elemento 'x' pertenezca a una clase 'C' a partir de la información proporcionada
En el reconocimiento de patrones, este algoritmo es usado como método de clasificación de objetos, basado en un entrenamiento mediante ejemplos cercacnos en el espacio de los elementos
Es sencillo, fácil de entrenar y trabaja con cualquier número de clases

El método K Vecinos Más Cercanos (KNN) es un algoritmo simple que funciona de la siguiente manera:
    1. Para clasificar o predecir un nuevo punto, calcula la distancia entre este punto y todos los puntos de datos existentes en el conjunto de entrenamiento.
    2. Identifica los 'k' puntos más cercanos (los "vecinos") al nuevo punto, donde 'k' es un número que se define previamente.
    3. Para clasificación, asigna al nuevo punto la clase que sea más frecuente entre sus 'k' vecinos. Para regresión, predice el valor como el promedio de los valores de sus 'k' vecinos.
En esencia, clasifica o predice basándose en la mayoría (o promedio) de sus vecinos más cercanos ya conocidos.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# cargamos el csv en un dataframe
dataframe = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/vehiculos.csv")
# print("\nDataframe original vehículos:")
# print(dataframe.head()) # 5 primeras filas
# print(dataframe.columns) # Columnas que hay y sus nombres
# print(dataframe['vehicle_class'].unique()) # Tipo de vehículos dentro de la columna 'vehicle_class' mediante el método .unique() Salida: ['van' 'saab' 'bus' 'opel']

Y = dataframe['vehicle_class']
X = dataframe.drop('vehicle_class', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=45)
print("\nCaracterísticas de entrenamiento:")
print(X_train)
print("\nCaracterísticas de prueba:")
print(X_test)
# Entrenamos el modelo
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
# Predicciones
predicciones = knn.predict(X_test)
print("\nPredicciones:")
print(predicciones)
# Evaluación (Metricas y matriz de confusión)
print("\nMatriz de confusión")
print(confusion_matrix(Y_test, predicciones))
print("\nReporte de clasificación")
print(classification_report(Y_test, predicciones))

# Sitema para evaluar k, el número de vecinos k más óptimo para que nos de una precisión mayor
tasa_error = []
for i in range(1, 30):
    knn = KNeighborsClassifier(n_neighbors=i) # Valor de k en cada ciclo
    knn.fit(X_train, Y_train) # Entrenamiento del modelo con el valor del k en cada ciclo
    predicciones_i = knn.predict(X_test) # Predicción con el valor de k
    tasa_error.append(np.mean(predicciones_i != Y_test)) # Se regrista la tasa de error de las predicciones da cada una de las k en función a los datos originales
# Explicación: Se recorre 30 veces el bucle, creará la variable knn con el KNeighbors con k igual a 1 en el primer ciclo y así hasta que k sea igual a 30. Se entrena con todos esos valores de k, a continuación, se efectúan las predicciones con todos esos valores de k y, en función de los datos de las predicciones, se registra en la variable tasa_error una lista con los valores de las predicciones da cada una de las k en función a los datos originales. La que de un número más bajo, es decir, una tasa de error menor, es la que debemos de elegir para tener el modelo más optimizado

# Ver la tasa de error
print("\nTasa de error:")
print(tasa_error)

# Ver la tasa de error a nivel Gráfico
valores = range(1, 30)
plt.plot(valores, tasa_error, color='green', marker='o', markerfacecolor='red', markersize=8)
plt.xlabel('Valor de k')
plt.ylabel('Tasa de Error')
plt.title('Tasa de Error vs. Valor de k')
plt.show()
plt.close()