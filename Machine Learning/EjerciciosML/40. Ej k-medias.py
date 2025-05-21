''' Algoritmo de k-medias - Practicar con el algoritmo de k-medias y sus métricas

El objetivo es implementar una función que:
Entrene un modelo K-Means (KMeans de sklearn.cluster).
Agrupe los datos en k clusters.
Evalúe el rendimiento del modelo utilizando:
Inercia (inertia_): mide qué tan bien se agrupan los datos.
Puntuación de Silueta (silhouette_score): evalúa qué tan bien están separados los clusters.
Precisión ajustada (adjusted_rand_score): mide la similitud con las etiquetas reales.
Devuelva los resultados en un diccionario.
Supervise la implementación con pruebas unitarias (unittest).

Instrucciones:
Implementa una función llamada entrenar_y_evaluar_kmeans(X, y, k) que:
Entrene un modelo KMeans(n_clusters=k, random_state=42).
Asigne cada muestra a un cluster (labels_).
Calcule las métricas de evaluación mencionadas.
Devuelva un diccionario con:
"clusters": Array con las asignaciones de cluster para cada muestra.
"inertia": Suma de las distancias al centroide más cercano.
inertia = modelo.inertia_
"silhouette_score": Puntuación de silueta (qué tan bien se separan los clusters).
silhouette = silhouette_score(X, clusters)
"adjusted_rand_score": Similaridad con las etiquetas reales.
rand_score = adjusted_rand_score(y, clusters)
Usa el dataset de flores iris de sklearn.datasets.
Asegúrate de que k=3 (correspondiente a las 3 clases reales de Iris).

Ejemplo de Uso:
El siguiente código debería ejecutarse correctamente una vez que implementes la función:
from sklearn.datasets import load_iris
import numpy as np
# Cargar el dataset de flores Iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Etiquetas reales (para evaluación)
# Llamar a la función con k=3 clusters
resultados = entrenar_y_evaluar_kmeans(X, y, k=3)
# Mostrar los resultados
print("Inercia del modelo:", resultados["inertia"])
print("Silhouette Score:", resultados["silhouette_score"])
print("Adjusted Rand Score:", resultados["adjusted_rand_score"])
print("Clusters asignados:\n", resultados["clusters"][:10])  # Mostrar primeras 10 asignaciones

Salida esperada:
Inercia del modelo: 78.85144142614601
Silhouette Score: 0.5528190123564095
Adjusted Rand Score: 0.7302382722834697
Clusters asignados:
[1 1 1 1 1 1 1 1 1 1]
'''

# kmeans_iris.py

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score
import unittest


def entrenar_y_evaluar_kmeans(X, y, k):
    """
    Entrena un modelo K-Means y evalúa su rendimiento.

    Parámetros:
    X (array-like): Características de los datos.
    y (array-like): Etiquetas reales (para evaluación).
    k (int): Número de clusters.

    Retorna:
    dict: Diccionario con los resultados del modelo.
    """
    # Entrenar el modelo K-Means
    modelo = KMeans(n_clusters=k, random_state=42)
    modelo.fit(X)

    # Obtener las asignaciones de cluster
    clusters = modelo.labels_

    # Calcular métricas de evaluación
    inercia = modelo.inertia_
    silhouette = silhouette_score(X, clusters)
    rand_score = adjusted_rand_score(y, clusters)

    # Retornar resultados en un diccionario
    return {
        "clusters": clusters,
        "inertia": inercia,
        "silhouette_score": silhouette,
        "adjusted_rand_score": rand_score
    }


# Ejemplo de uso
if __name__ == "__main__":
    # Cargar el dataset de flores Iris
    iris = load_iris()
    X = iris.data  # Características
    y = iris.target  # Etiquetas reales (para evaluación)

    # Llamar a la función con k=3 clusters
    resultados = entrenar_y_evaluar_kmeans(X, y, k=3)

    # Mostrar los resultados
    print("Inercia del modelo:", resultados["inertia"])
    print("Silhouette Score:", resultados["silhouette_score"])
    print("Adjusted Rand Score:", resultados["adjusted_rand_score"])
    print("Clusters asignados:\n", resultados["clusters"][:10])  # Mostrar primeras 10 asignaciones


# Pruebas unitarias
class TestKMeans(unittest.TestCase):
    def setUp(self):
        # Cargar el dataset de flores Iris
        self.iris = load_iris()
        self.X = self.iris.data
        self.y = self.iris.target

    def test_entrenar_y_evaluar_kmeans(self):
        # Llamar a la función con k=3 clusters
        resultados = entrenar_y_evaluar_kmeans(self.X, self.y, k=3)

        # Verificar que los resultados son del tipo correcto
        self.assertIsInstance(resultados, dict)
        self.assertIn("clusters", resultados)
        self.assertIn("inertia", resultados)
        self.assertIn("silhouette_score", resultados)
        self.assertIn("adjusted_rand_score", resultados)

        # Verificar que las métricas tienen valores razonables
        self.assertGreater(resultados["inertia"], 0)
        self.assertGreaterEqual(resultados["silhouette_score"], -1)
        self.assertLessEqual(resultados["silhouette_score"], 1)
        self.assertGreaterEqual(resultados["adjusted_rand_score"], -1)
        self.assertLessEqual(resultados["adjusted_rand_score"], 1)

        # Verificar que el número de clusters es correcto
        self.assertEqual(len(set(resultados["clusters"])), 3)


# Ejecutar las pruebas unitarias
if __name__ == "__main__":
    unittest.main()
