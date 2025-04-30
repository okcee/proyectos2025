''' Ejercicio de codificación 24 - Métricas en árboles de decisión

〰  El objetivo de este ejercicio es que los estudiantes implementen una función que:
    1. Entrene un árbol de decisión usando DecisionTreeClassifier de sklearn.
    2. Haga predicciones en un conjunto de prueba.
    3. Evalúe el modelo utilizando métricas como precisión (accuracy), matriz de confusión y reporte de clasificación.
    4. Pase pruebas unitarias (unittest) que validen el funcionamiento correcto del código.

〰 Instrucciones
1. Implementa una función llamada entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test) que:
    - Entrene un modelo DecisionTreeClassifier con los datos de entrenamiento (X_train, y_train).
    - Prediga los valores de X_test.
    - Evalúe el modelo usando:
        - Precisión (accuracy_score)
        - Matriz de confusión (confusion_matrix)
        - Reporte de clasificación (classification_report)
    - Devuelva un diccionario con:
        - predicciones: Un array con las predicciones del modelo.
        - accuracy: Un número flotante con la precisión.
        - matriz_confusion: Una matriz de confusión.
        - reporte: Un string con el reporte de clasificación.
2. Usa random_state=42 en DecisionTreeClassifier para reproducibilidad.
3. Prueba la función con el dataset Iris, asegurando que el modelo tenga al menos 85% de precisión en los datos de prueba.

〰 Ejemplo de Uso
Una vez implementada la función, debe ejecutarse correctamente con este código de prueba:
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
# Cargar el dataset de flores Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Clases de las flores (Setosa, Versicolor, Virginica)
# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Importar la función implementada
from solution import entrenar_y_evaluar_arbol
# Llamar a la función y obtener las métricas
resultados = entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test)
# Mostrar los resultados
print("Precisión del modelo:", resultados["accuracy"])
print("Matriz de Confusión:\n", resultados["matriz_confusion"])
print("Reporte de Clasificación:\n", resultados["reporte"])

〰 Salida esperada (aproximada):
Precisión del modelo: 1.0
Matriz de Confusión:
[[10  0  0]
[ 0  9  0]
[ 0  0 11]]
Reporte de Clasificación:
               precision    recall  f1-score   support
 
      Setosa       1.00      1.00      1.00        10
  Versicolor       1.00      1.00      1.00         9
   Virginica       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30

〰 Objetivo de aprendizaje: Practicar con las métricas en los árboles de decisión
'''
# 1. Implementa una función llamada entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test)
def entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test):
    
#     - Entrene un modelo DecisionTreeClassifier con los datos de entrenamiento (X_train, y_train).
#     - Prediga los valores de X_test.
#     - Evalúe el modelo usando:
#         - Precisión (accuracy_score)
#         - Matriz de confusión (confusion_matrix)
#         - Reporte de clasificación (classification_report)
#     - Devuelva un diccionario con:
#         - predicciones: Un array con las predicciones del modelo.
#         - accuracy: Un número flotante con la precisión.
#         - matriz_confusion: Una matriz de confusión.
#         - reporte: Un string con el reporte de clasificación.
# 2. Usa random_state=42 en DecisionTreeClassifier para reproducibilidad.
# 3. Prueba la función con el dataset Iris, asegurando que el modelo tenga al menos 85% de precisión en los datos de prueba.