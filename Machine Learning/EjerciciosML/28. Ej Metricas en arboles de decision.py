''' Métricas en árboles de decisión
El objetivo de este ejercicio es que los estudiantes implementen una función que:
Entrene un árbol de decisión usando DecisionTreeClassifier de sklearn.
Haga predicciones en un conjunto de prueba.
Evalúe el modelo utilizando métricas como precisión (accuracy), matriz de confusión y reporte de clasificación.
Pase pruebas unitarias (unittest) que validen el funcionamiento correcto del código.

Instrucciones
Implementa una función llamada entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test) que:
Entrene un modelo DecisionTreeClassifier con los datos de entrenamiento (X_train, y_train).
Prediga los valores de X_test.
Evalúe el modelo usando:
Precisión (accuracy_score)
Matriz de confusión (confusion_matrix)
Reporte de clasificación (classification_report)
Devuelva un diccionario con:
predicciones: Un array con las predicciones del modelo.
accuracy: Un número flotante con la precisión.
matriz_confusion: Una matriz de confusión.
reporte: Un string con el reporte de clasificación.
Usa random_state=42 en DecisionTreeClassifier para reproducibilidad.
Prueba la función con el dataset Iris, asegurando que el modelo tenga al menos 85% de precisión en los datos de prueba.

Ejemplo de Uso
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


Salida esperada (aproximada):

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

Practicar con las métricas en los árboles de decisión
'''

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import numpy as np


def graficar_temperaturas(dias, temperaturas):
    plt.figure(figsize=(10, 5))  # Tamaño del gráfico
    plt.plot(dias, temperaturas, marker='o', linestyle='--', color='b', markersize=8, linewidth=2, label='Temperatura')

    # Etiquetas y título
    plt.xlabel("Días")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperaturas Semanales")

    # Añadir leyenda
    plt.legend()

    # Mostrar la cuadrícula para mejor visualización
    plt.grid(True, linestyle='--', alpha=0.6)

    # Mostrar la gráfica
    plt.show()


def analizar_finanzas(ingresos, gastos):
    ingresos = np.array(ingresos)
    gastos = np.array(gastos)

    balance_mensual = ingresos - gastos
    total_ingresos = np.sum(ingresos)
    total_gastos = np.sum(gastos)
    saldo_final = total_ingresos - total_gastos

    return [balance_mensual.tolist(), total_ingresos, total_gastos, saldo_final]


def entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test):
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)

    accuracy = accuracy_score(y_test, predicciones)
    matriz_confusion = confusion_matrix(y_test, predicciones)
    reporte = classification_report(y_test, predicciones)

    return {
        "predicciones": predicciones,
        "accuracy": accuracy,
        "matriz_confusion": matriz_confusion,
        "reporte": reporte
    }


# Datos proporcionados
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temperaturas = [22, 24, 23, 25, 26, 28, 27]

graficar_temperaturas(dias, temperaturas)

# Datos de finanzas
ingresos = [1500, 1600, 1700, 1650, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]
gastos = [1000, 1100, 1200, 1150, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]

resultado = analizar_finanzas(ingresos, gastos)
print(resultado)

# Cargar el dataset de Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Clases de las flores

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar y evaluar
resultados = entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test)
print("Precisión del modelo:", resultados["accuracy"])
print("Matriz de Confusión:\n", resultados["matriz_confusion"])
print("Reporte de Clasificación:\n", resultados["reporte"])
