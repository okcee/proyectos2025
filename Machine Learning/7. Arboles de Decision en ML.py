# Importamos las librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

''' Árboles de decisión en Machine Learning
Un árbol de decisión es un modelo de predicción utilizado en diversos ámbitos que van desde la inteligencia artificial hasta la economía
Dado un conjunto de datos, se fabrican diagramas de construcciones lógicas, que sirven para representar y categorizar una serie de condiciones que ocurren de forma sucesiva, para resolución de un problema
'''
# Cargamos el dataset desde un archivo CSV
vinos = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/vino.csv")
# Mostramos las primeras filas para inspeccionar los datos (opcional, descomentar para ver)
# print(vinos.head())
# Mostramos los nombres de las columnas (opcional, descomentar para ver)
# print(vinos.columns)
# Mostramos los valores únicos en la columna objetivo 'Wine Type' (opcional, descomentar para ver)
# print(vinos['Wine Type'].unique()) # Datos de la columna: ['One' 'Two' 'Three']

# Contamos cuántas muestras hay de cada tipo de vino en la columna 'Wine Type'
print(vinos['Wine Type'].value_counts())
''' Salida:
Wine Type
Two      71
One      59
Three    48
Name: count, dtype: int64 # Indica que hay 71 vinos del tipo 'Two', 59 del 'One' y 48 del 'Three'
'''

# Separamos las características (X) de la variable objetivo (y)
# X contiene todas las columnas excepto 'Wine Type'
X = vinos.drop('Wine Type', axis=1)
# y contiene solo la columna 'Wine Type', que es lo que queremos predecir
y = vinos['Wine Type']

# Dividimos los datos: 70% para entrenamiento (X_train, y_train) y 30% para prueba (X_test, y_test)
# random_state asegura que la división sea la misma cada vez que se ejecute el código
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

# Creamos una instancia del clasificador de Árbol de Decisión
arbol = DecisionTreeClassifier() # Asignamos el método de machine learning tipo árbol de decisión para clasificación de datos
# Entrenamos el modelo usando los datos de entrenamiento
arbol.fit(X_train, y_train) # Entrenamiento
# Realizamos predicciones sobre el conjunto de datos de prueba
predicciones = arbol.predict(X_test)

# Imprimimos la matriz de confusión para ver los aciertos y errores por clase
print("\nMatriz de confusión")
print(confusion_matrix(y_test, predicciones))
# Imprimimos el reporte de clasificación, que incluye precisión, recall, f1-score por clase y la accuracy general
print("\nReporte de clasificación")
print(classification_report(y_test, predicciones))

''' Árboles de decisión en Machine Learning - Versión mediante función
Podemos refactorizar el código para encapsular la lógica principal de carga, entrenamiento y predicción dentro de una función. Esto hace que el código sea más reutilizable y fácil de probar con diferentes datasets o parámetros.

Este script encapsula la lógica de entrenamiento y evaluación
de un árbol de decisión en una función reutilizable.
'''
def entrenar_evaluar_arbol_decision(
    ruta_csv: str,
    columna_objetivo: str,
    test_size: float = 0.3,
    random_state: int = 45,
    **tree_params # Para pasar parámetros al DecisionTreeClassifier
):
    """
    Carga datos desde un CSV, entrena un Árbol de Decisión, realiza
    predicciones en el conjunto de prueba y devuelve los resultados clave.
    Args:
        ruta_csv (str): Ruta al archivo CSV del dataset.
        columna_objetivo (str): Nombre de la columna que contiene la variable objetivo.
        test_size (float): Proporción del dataset a usar para el conjunto de prueba.
                            Por defecto es 0.3 (30%).
        random_state (int): Semilla para la división aleatoria y el clasificador, para asegurar la reproducibilidad. Por defecto es 45.
        **tree_params: Argumentos adicionales que se pasarán directamente al constructor de DecisionTreeClassifier (ej. max_depth, min_samples_leaf).
    Returns:
        tuple: Una tupla conteniendo: 
                - model (DecisionTreeClassifier): El modelo de árbol de decisión entrenado.
                - y_pred (np.ndarray): Las predicciones hechas sobre el conjunto de prueba.
                - y_test (pd.Series): Los valores reales del conjunto de prueba.
                - X_test (pd.DataFrame): Las características del conjunto de prueba.
                    Devuelve (None, None, None, None) si ocurre un error durante el proceso.
    """
    try:
        # Cargamos el dataset desde un archivo CSV
        df = pd.read_csv(ruta_csv)
        print(f"--- Información del Dataset ({ruta_csv}) ---")
        print(f"Objetivo: '{columna_objetivo}'")
        print("Distribución de clases en la columna objetivo:")
        print(df[columna_objetivo].value_counts())
        print("-" * (30 + len(ruta_csv)))

        # Separamos las características (X) de la variable objetivo (y)
        X = df.drop(columna_objetivo, axis=1)
        y = df[columna_objetivo]

        # Dividimos los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        # Creamos una instancia del clasificador de Árbol de Decisión
        # Aseguramos que random_state se use también en el árbol si no se pasa explícitamente
        if 'random_state' not in tree_params:
            tree_params['random_state'] = random_state

        arbol = DecisionTreeClassifier(**tree_params)
        print(f"\nEntrenando DecisionTreeClassifier con parámetros: {tree_params}...")

        # Entrenamos el modelo usando los datos de entrenamiento
        arbol.fit(X_train, y_train)
        print("Modelo entrenado.")

        # Realizamos predicciones sobre el conjunto de datos de prueba
        predicciones = arbol.predict(X_test)
        print("Predicciones realizadas sobre el conjunto de prueba.")

        # Devolvemos el modelo, las predicciones y los datos de prueba para evaluación externa
        return arbol, predicciones, y_test, X_test

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta: {ruta_csv}")
        return None, None, None, None
    except KeyError:
        print(f"Error: La columna objetivo '{columna_objetivo}' no se encontró en el archivo CSV.")
        return None, None, None, None
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el proceso: {e}")
        return None, None, None, None

# --- Ejemplo de Uso de la Función ---
archivo_datos = "S:/_proyectos2025/Machine Learning/Datasets/vino.csv"
col_objetivo = 'Wine Type'

# Llamamos a la función para entrenar y obtener resultados
modelo_dt, preds, y_real, X_eval = entrenar_evaluar_arbol_decision(archivo_datos, col_objetivo)

# Si la función se ejecutó correctamente, evaluamos los resultados
if modelo_dt is not None:
    print("\n--- Evaluación del Modelo ---")
    # Imprimimos la matriz de confusión
    print("\nMatriz de confusión:")
    print(confusion_matrix(y_real, preds))
    # Imprimimos el reporte de clasificación
    print("\nReporte de clasificación:")
    print(classification_report(y_real, preds))
else:
    print("\nEl entrenamiento no pudo completarse debido a un error.")