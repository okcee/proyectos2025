''' Random Forest - Practicar con el algoritmo de Random Forest y sus métricas
El objetivo es implementar una función que:
Entrene un modelo Random Forest (RandomForestClassifier).
Haga predicciones en datos de prueba.
Evalúe el rendimiento del modelo con:
Precisión (accuracy_score)
Matriz de confusión (confusion_matrix)
Reporte de clasificación (classification_report)
Devuelva los resultados en un diccionario.
Supervise la implementación con pruebas unitarias (unittest).

Instrucciones
Implementa una función llamada entrenar_y_evaluar_random_forest(X_train, y_train, X_test, y_test) que:
Entrene un RandomForestClassifier(n_estimators=100, random_state=42).
Prediga los valores de X_test.
Calcule las métricas de evaluación mencionadas.
Devuelva un diccionario con:
"predicciones": Array de predicciones del modelo.
"accuracy": Precisión del modelo en los datos de prueba.
"matriz_confusion": Matriz de confusión.
"reporte": Reporte de clasificación.
Usa el dataset de vinos (wine dataset) de sklearn.datasets.
Asegúrate de que el modelo tenga al menos 90% de precisión en los datos de prueba.

Ejemplo de Uso
El siguiente código debería ejecutarse correctamente una vez que implementes la función:
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import numpy as np
# Cargar el dataset de vinos
wine = load_wine()
X = wine.data  # Características
y = wine.target  # Clases de vinos
# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Importar la función implementada
from solution import entrenar_y_evaluar_random_forest
# Llamar a la función y obtener las métricas
resultados = entrenar_y_evaluar_random_forest(X_train, y_train, X_test, y_test)
# Mostrar los resultados
print("Precisión del modelo:", resultados["accuracy"])
print("Matriz de Confusión:\n", resultados["matriz_confusion"])
print("Reporte de Clasificación:\n", resultados["reporte"])

Salida esperada (aproximada)
Precisión del modelo: 1.0
Matriz de Confusión:
[[14  0  0]
[ 0 14  0]
[ 0  0  8]]
Reporte de Clasificación:
            precision    recall  f1-score   support

Clase 0       1.00      1.00      1.00        14
Clase 1       1.00      1.00      1.00        14
Clase 2       1.00      1.00      1.00         8

    accuracy                            1.00         36
    macro avg       1.00      1.00      1.00         36
weighted avg        1.00      1.00      1.00         36
'''

from sklearn.datasets import load_iris, load_wine
from sklearn.ensemble import RandomForestClassifier
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


def entrenar_y_evaluar_random_forest(X_train, y_train, X_test, y_test):
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
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

# Entrenar y evaluar Árbol de Decisión
resultados = entrenar_y_evaluar_arbol(X_train, y_train, X_test, y_test)
print("Precisión del modelo Árbol de Decisión:", resultados["accuracy"])
print("Matriz de Confusión:\n", resultados["matriz_confusion"])
print("Reporte de Clasificación:\n", resultados["reporte"])

# Cargar el dataset de Vinos
wine = load_wine()
X_wine = wine.data  # Características
y_wine = wine.target  # Clases de vinos

# Dividir en conjunto de entrenamiento y prueba
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.2, random_state=42)

# Entrenar y evaluar Random Forest
resultados_rf = entrenar_y_evaluar_random_forest(X_train_wine, y_train_wine, X_test_wine, y_test_wine)
print("Precisión del modelo Random Forest:", resultados_rf["accuracy"])
print("Matriz de Confusión:\n", resultados_rf["matriz_confusion"])
print("Reporte de Clasificación:\n", resultados_rf["reporte"])
