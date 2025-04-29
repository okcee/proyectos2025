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
import os # Importar os para manejo de rutas
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# --- Carga de Datos ---
# Es mejor manejar la ruta de forma más robusta
script_dir = os.path.dirname(__file__) if '__file__' in locals() else '.' # Directorio del script
# Construir la ruta relativa al archivo CSV
relative_path = os.path.join("Datasets", "iris.csv")
# Intentar construir la ruta absoluta desde el directorio del script
absolute_path_from_script = os.path.join(script_dir, relative_path)

original_path = "S:/_proyectos2025/Machine Learning/Datasets/iris.csv" # O la ruta que corresponda
file_path_to_use = None

if os.path.exists(absolute_path_from_script):
    file_path_to_use = absolute_path_from_script
    print(f"Cargando datos desde: {file_path_to_use}")
elif os.path.exists(original_path):
    file_path_to_use = original_path
    print(f"Cargando datos desde ruta original: {file_path_to_use}")
else:
    # Intentar cargar desde el directorio actual como último recurso
    
    try:
        pd.read_csv("iris.csv") # Solo para probar si existe
        file_path_to_use = "iris.csv"
        print("Cargando 'iris.csv' desde el directorio actual.")
    except FileNotFoundError:
        print("Error: No se pudo encontrar 'iris.csv' en las rutas esperadas:")
        print(f" - {absolute_path_from_script}")
        print(f" - {original_path}")
        print(" - Directorio actual")
        # Decide qué hacer: salir, lanzar excepción, o continuar sin datos
        exit() # Salir si el archivo es esencial

# Cargar los datos usando la ruta encontrada
data_iris = pd.read_csv(file_path_to_use)
# print(data_iris.head())

def knn_clasificacion(datos: pd.DataFrame, k: int = 3) -> KNeighborsClassifier:
    """
    Entrena un modelo K-Nearest Neighbors para clasificación.
    Args:
        datos (pd.DataFrame): DataFrame que contiene las características y la columna objetivo 'Especies'.
        k (int): Número de vecinos a considerar.
    Returns:
        KNeighborsClassifier: El modelo KNN entrenado.
    """
    # 1. Separar características (X) y objetivo (y) DEL DATAFRAME DE ENTRADA 'datos'
    try:
        # Asume que las características son todas las columnas excepto 'Especies'
        features = datos.drop('Especies', axis=1).columns.tolist()
        X = datos[features]
        y = datos['Especies']
    except KeyError as e:
        print(f"Error: Falta la columna requerida en el DataFrame de entrada: {e}")
        raise # Re-lanzar el error para detener la ejecución si falta una columna clave

    # 2. Crear una instancia del clasificador KNN
    modelo = KNeighborsClassifier(n_neighbors=k)

    # 3. Entrenar (ajustar) el modelo con TODOS los datos proporcionados
    #    No se usa train_test_split porque queremos entrenar con todo para predecir nuevas muestras
    modelo.fit(X, y)

    # 4. Devolver el modelo entrenado
    return modelo

# --- Ejemplo de uso ---
# Llamar a la función con los datos cargados
modelo_knn = knn_clasificacion(data_iris, k=3)

# Estimaciones de clasificación para nuevas muestras
nuevas_muestras = pd.DataFrame({
    'LargoSepalo': [5.1, 6.0, 4.4],
    'AnchoSepalo': [3.5, 2.9, 3.2],
    'LargoPetalo': [1.4, 4.5, 1.3],
    'AnchoPetalo': [0.2, 1.5, 0.2]
})

# Asegurarse de que las columnas de las nuevas muestras coinciden y están en el mismo orden que en el entrenamiento
# Esto es importante si las nuevas muestras vinieran de otra fuente
try:
    nuevas_muestras_ordenadas = nuevas_muestras[modelo_knn.feature_names_in_]
    estimaciones_clasificacion = modelo_knn.predict(nuevas_muestras_ordenadas)
    print("\nEstimaciones de Clasificación:")
    print(estimaciones_clasificacion)
except ValueError as e:
    print(f"\nError al predecir: Las columnas de 'nuevas_muestras' no coinciden con las usadas en el entrenamiento.")
    print(f" - Columnas esperadas: {modelo_knn.feature_names_in_}")
    print(f" - Columnas recibidas: {nuevas_muestras.columns.tolist()}")
    print(f" - Error original: {e}")


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

def knn_clasificacion(datos: pd.DataFrame, k: int = 3) -> KNeighborsClassifier:
    """
    Entrena un modelo K-Nearest Neighbors para clasificación.
    Args:
        datos (pd.DataFrame): DataFrame que contiene las características y la columna objetivo 'Especies'.
        k (int): Número de vecinos a considerar.
    Returns:
        KNeighborsClassifier: El modelo KNN entrenado.
    """
    features = datos.drop('species', axis=1).columns.tolist()
    X = datos[features]
    y = datos['species']
    
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X, y)
    
    return modelo

# Cargar los datos de Iris desde sklearn
iris = load_iris()
data_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data_iris['species'] = iris.target_names[iris.target]

# Usar la función para entrenar el modelo
modelo_knn = knn_clasificacion(data_iris, k=3)

# Nuevas muestras para clasificación
nuevas_muestras = pd.DataFrame({
    'sepal length (cm)': [5.1, 6.0, 4.4],
    'sepal width (cm)': [3.5, 2.9, 3.2],
    'petal length (cm)': [1.4, 4.5, 1.3],
    'petal width (cm)': [0.2, 1.5, 0.2]
})

# Clasificación para nuevas muestras
estimaciones_clasificacion = modelo_knn.predict(nuevas_muestras)
print("\nEstimaciones de Clasificación:")
print(estimaciones_clasificacion)
