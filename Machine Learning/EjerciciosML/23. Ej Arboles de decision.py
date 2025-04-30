''' Ejercicio de codificación 23 - Arboles de decisión
〰 Implementar una función en Python que entrene un árbol de decisión y lo use para hacer predicciones en un conjunto de datos.

〰 Instrucciones
Implementa una función llamada entrenar_arbol_decision(X_train, y_train, X_test) que:
Entrene un árbol de decisión con los datos de entrenamiento X_train y y_train.
Prediga los valores de X_test.
Devuelva un array con las predicciones.
Usa DecisionTreeClassifier de sklearn.tree con random_state=42 para asegurar reproducibilidad.
No modifiques los parámetros de entrenamiento (como la profundidad del árbol o la función de división).
Prueba la función con un conjunto de datos real como el conjunto de datos de flores Iris.

〰 Ejemplo de Uso
Tu función debe funcionar correctamente con este código de prueba:
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
# Cargar el dataset de flores Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Clases de las flores (Setosa, Versicolor, Virginica)
# Dividir en conjunto de entrenamiento y prueba (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Llamar a la función que debes implementar
predicciones = entrenar_arbol_decision(X_train, y_train, X_test)
# Mostrar algunas predicciones
print("Predicciones del Árbol de Decisión:", predicciones[:10])
print("Valores reales:                    ", y_test[:10])

〰 Objetivo de aprendijaje: Practicar creando un modelo de árbol de decision utilizando DecisionTreeClassifier para realizar predicciones sobre un dataset
'''
# import pandas as pd
# import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Implementa una función llamada entrenar_arbol_decision(X_train, y_train, X_test
def entrenar_arbol_decision(X_train, 
                            y_train, 
                            X_test):
    predicciones = [] # Lista vacía para los datos de salida de la función
    try:
        # Iniciamos el método DecisionTreeClassifier()
        arbol = DecisionTreeClassifier()
        print("\nEntrenando DecisionTreeClassifier...")
        # 1.1. Entrene un árbol de decisión con los datos de entrenamiento X_train y y_train.
        arbol.fit(X_train, y_train)
        print("Modelo entrenado.")
        # Prediga los valores de X_test, sobre el conjunto de datos de prueba
        predicciones = arbol.predict(X_test)
        print("Predicciones realizadas sobre el conjunto de prueba.")
        # Devolvemos un array con las predicciones.
        return predicciones
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo")
        return None, None, None, None
    except KeyError:
        print("Error: La columna objetivo 'y' no se encontró en el archivo CSV.")
        return None, None, None, None
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el proceso: {e}")
        return None, None, None, None

# Cargar el dataset de flores Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Clases de las flores (Setosa, Versicolor, Virginica)
# Dividir en conjunto de entrenamiento y prueba (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Llamar a la función que debes implementar
predicciones = entrenar_arbol_decision(X_train, y_train, X_test)
# Mostrar algunas predicciones
print("Predicciones del Árbol de Decisión:", predicciones[:10])
print("Valores reales:                    ", y_test[:10])