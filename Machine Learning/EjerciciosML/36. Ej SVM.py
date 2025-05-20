''' SVM - Máquinas de vectores de soporte - Practicar con el algoritmo SVM de máquinas de vectores de soporte y sus métricas, con un datset que contiene imágenes de numeros del 0 a 9.

Objetivo
El objetivo es implementar una función que:
Entrene un modelo de Máquina de Soporte Vectorial (SVM) usando SVC de sklearn.svm.
Realice predicciones en un conjunto de prueba.
Evalúe el modelo con las siguientes métricas:
Precisión (accuracy_score).
Matriz de confusión (confusion_matrix).
Reporte de clasificación (classification_report).
Devuelva los resultados en un diccionario.
Supervise la implementación con pruebas unitarias (unittest).

Instrucciones
Implementa una función llamada entrenar_y_evaluar_svm(X_train, y_train, X_test, y_test) que:
Entrene un modelo SVC(kernel='rbf', C=10.0, gamma='scale', random_state=42).
Prediga los valores de X_test.
Calcule las métricas de evaluación mencionadas.
Devuelva un diccionario con:
"predicciones": Array de predicciones del modelo.
"accuracy": Precisión del modelo en los datos de prueba.
"matriz_confusion": Matriz de confusión.
"reporte": Reporte de clasificación.
Usa el dataset de digits de sklearn.datasets, que contiene imágenes de números escritos a mano.
Asegúrate de que el modelo tenga al menos 90% de precisión en los datos de prueba.

Ejemplo de Uso
Una vez que la función esté implementada, el siguiente código debería ejecutarse correctamente:
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
# Cargar el dataset de dígitos escritos a mano
digits = load_digits()
X = digits.data  # Características (matriz de píxeles)
y = digits.target  # Etiquetas (números del 0 al 9)
# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Llamar a la función y obtener las métricas
resultados = entrenar_y_evaluar_svm(X_train, y_train, X_test, y_test)
# Mostrar los resultados
print("Precisión del modelo:", resultados["accuracy"])
print("Matriz de Confusión:\n", resultados["matriz_confusion"])
print("Reporte de Clasificación:\n", resultados["reporte"])

Salida esperada (aproximada)
Precisión del modelo: 0.9861111111111112
Matriz de Confusión:
[[33  0  0  0  0  0  0  0  0  0]
[ 0 28  0  0  0  0  0  0  0  0]
[ 0  0 33  0  0  0  0  0  0  0]
[ 0  0  0 33  0  1  0  0  0  0]
[ 0  0  0  0 46  0  0  0  0  0]
[ 0  0  0  0  0 46  1  0  0  0]
[ 0  0  0  0  0  0 35  0  0  0]
[ 0  0  0  0  0  0  0 33  0  1]
[ 0  0  0  0  0  1  0  0 29  0]
[ 0  0  0  0  0  0  0  1  0 39]]
Reporte de Clasificación:
                precision    recall  f1-score   support

            0       1.00      1.00      1.00        33
            1       1.00      1.00      1.00        28
            2       1.00      1.00      1.00        33
            3       1.00      0.97      0.99        34
            4       1.00      1.00      1.00        46
            5       0.96      0.98      0.97        47
            6       0.97      1.00      0.99        35
            7       0.97      0.97      0.97        34
            8       1.00      0.97      0.98        30
            9       0.97      0.97      0.97        40

    accuracy                            0.99       360
    macro avg       0.99      0.99      0.99       360
weighted avg        0.99      0.99      0.99       360
'''

# svm_digits.py

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import unittest


def entrenar_y_evaluar_svm(X_train, y_train, X_test, y_test):
    """
    Entrena un modelo SVM y evalúa su rendimiento.

    Parámetros:
    X_train (array-like): Características de entrenamiento.
    y_train (array-like): Etiquetas de entrenamiento.
    X_test (array-like): Características de prueba.
    y_test (array-like): Etiquetas de prueba.

    Retorna:
    dict: Diccionario con los resultados del modelo.
    """
    # Entrenar el modelo SVM
    modelo = SVC(kernel='rbf', C=10.0, gamma='scale', random_state=42)
    modelo.fit(X_train, y_train)

    # Predecir en el conjunto de prueba
    predicciones = modelo.predict(X_test)

    # Calcular métricas de evaluación
    accuracy = accuracy_score(y_test, predicciones)
    matriz_confusion = confusion_matrix(y_test, predicciones)
    reporte = classification_report(y_test, predicciones)

    # Retornar resultados en un diccionario
    return {
        "predicciones": predicciones,
        "accuracy": accuracy,
        "matriz_confusion": matriz_confusion,
        "reporte": reporte
    }


# Ejemplo de uso
if __name__ == "__main__":
    # Cargar el dataset de dígitos escritos a mano
    digits = load_digits()
    X = digits.data  # Características (matriz de píxeles)
    y = digits.target  # Etiquetas (números del 0 al 9)

    # Dividir en conjunto de entrenamiento (80%) y prueba (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Llamar a la función y obtener las métricas
    resultados = entrenar_y_evaluar_svm(X_train, y_train, X_test, y_test)

    # Mostrar los resultados
    print("Precisión del modelo:", resultados["accuracy"])
    print("Matriz de Confusión:\n", resultados["matriz_confusion"])
    print("Reporte de Clasificación:\n", resultados["reporte"])


# Pruebas unitarias
class TestSVM(unittest.TestCase):
    def setUp(self):
        # Cargar el dataset de dígitos
        self.digits = load_digits()
        self.X = self.digits.data
        self.y = self.digits.target

        # Dividir en conjunto de entrenamiento y prueba
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )

    def test_entrenar_y_evaluar_svm(self):
        # Llamar a la función
        resultados = entrenar_y_evaluar_svm(self.X_train, self.y_train, self.X_test, self.y_test)

        # Verificar que los resultados son del tipo correcto
        self.assertIsInstance(resultados, dict)
        self.assertIn("predicciones", resultados)
        self.assertIn("accuracy", resultados)
        self.assertIn("matriz_confusion", resultados)
        self.assertIn("reporte", resultados)

        # Verificar que la precisión es mayor o igual al 90%
        self.assertGreaterEqual(resultados["accuracy"], 0.90)

        # Verificar que la matriz de confusión tiene la forma correcta
        self.assertEqual(resultados["matriz_confusion"].shape, (10, 10))


# Ejecutar las pruebas unitarias
if __name__ == "__main__":
    unittest.main()
