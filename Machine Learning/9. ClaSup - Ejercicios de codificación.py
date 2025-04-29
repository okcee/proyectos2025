''' Ejercicio de codificación 19
K Vecinos Más Cercanos para Clasificación
En este ejercicio debes desarrollar una función que aplique el algoritmo de los k vecinos más cercanos (KNN) para un problema de clasificación.
Supongamos que tienes un conjunto de datos que contiene información sobre diferentes tipos de flores, y deseas predecir el tipo de flor en función de las características de pétalos y sépalos.
Utilizaremos el conjunto de datos Iris, que es un conjunto de datos de clasificación ampliamente utilizado en el aprendizaje automático.

def knn_clasificacion(datos, k=3):
# Ejemplo de uso con el conjunto de datos Iris
data = pd.read_csv('iris.csv')  # Reemplaza 'iris.csv' con tu archivo de datos
modelo_knn = knn_clasificacion(data, k=3)
# Estimaciones de clasificación para nuevas muestras
nuevas_muestras = pd.DataFrame({
    'LargoSepalo': [5.1, 6.0, 4.4],
    'AnchoSepalo': [3.5, 2.9, 3.2],
    'LargoPetalo': [1.4, 4.5, 1.3],
    'AnchoPetalo': [0.2, 1.5, 0.2]
})
estimaciones_clasificacion = modelo_knn.predict(nuevas_muestras)
print("Estimaciones de Clasificación:")
print(estimaciones_clasificacion)
Resultados:
Estimaciones de Clasificación:
['setosa' 'versicolor' 'setosa']
'''
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/iris.csv")
# # print(data.head())

# Función de clasificación KNN
def knn_clasificacion(datos, k=3):
    y = data['Especies']
    X = data.drop('Especies', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=45)
    modelo = KNeighborsClassifier(n_neighbors=3)
    modelo.fit(X_train, y_train)
    return modelo

# Estimaciones de clasificación para nuevas muestras
nuevas_muestras = pd.DataFrame({
    'LargoSepalo': [5.1, 6.0, 4.4],
    'AnchoSepalo': [3.5, 2.9, 3.2],
    'LargoPetalo': [1.4, 4.5, 1.3],
    'AnchoPetalo': [0.2, 1.5, 0.2]
})
estimaciones_clasificacion = modelo_knn.predict(nuevas_muestras)
print("Estimaciones de Clasificación:")
print(estimaciones_clasificacion)

