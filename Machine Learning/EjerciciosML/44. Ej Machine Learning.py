''' Predicción de abandono escolar - Practicar con la eleccion del modelo a utilizar y mostrar una predicción

Imagina que formas parte del equipo de analítica de datos de una universidad.
Tu objetivo es construir un modelo de machine learning que prediga si un estudiante probablemente abandonará sus estudios, basándote en ciertas características académicas y de comportamiento.

📊 Los responsables del área te proporcionan un conjunto de datos simulados con la siguiente información para cada estudiante:
Edad: edad del estudiante (entre 18 y 29 años).
Horas_estudio: promedio de horas semanales dedicadas al estudio.
Asistencia: porcentaje de asistencia a clase.
Promedio: nota media del estudiante (en escala de 0 a 10).
Uso_online: número de horas por semana que usa la plataforma educativa online.
Abandono: variable objetivo (0 = continúa, 1 = abandona).

🧠 Tu misión:
Construir un sistema basado en árboles de decisión que permita:
Simular los datos como si fueran recolectados de 200 estudiantes.
Entrenar un modelo de machine learning que prediga la variable Abandono.
Evaluar el modelo con métricas adecuadas.
Predecir si un nuevo estudiante abandonará o no, a partir de sus datos.

✅ Requisitos técnicos
Debes organizar tu solución en al menos tres clases:
🔹 Clase SimuladorDatos
La clase SimuladorDatos tiene como tarea generar un conjunto de datos simulados para entrenar un modelo de Machine Learning que prediga si un estudiante abandonará o no sus estudios.
Este conjunto de datos estará compuesto por 200 registros (estudiantes), y cada registro tendrá varias características, como edad, horas de estudio, asistencia y promedio académico.
Además, debe incluir una columna Abandono que será nuestra variable objetivo (el valor que queremos predecir).
Tareas:
Definir la clase SimuladorDatos:
La clase debe tener dos atributos:
n: número de registros (por defecto 200).
seed: semilla para la aleatoriedad (por defecto 42) para que los resultados sean reproducibles.
La clase debe tener un método llamado generar(), que será el encargado de crear y devolver un conjunto de datos simulado en formato pandas.DataFrame.
Generar las columnas del DataFrame:
El método generar() debe crear un DataFrame con las siguientes columnas (variables) y valores aleatorios:
Edad: Un valor aleatorio entre 18 y 30 años.
Horas de estudio: Un valor decimal aleatorio entre 0 y 30 horas por semana.
Asistencia: Un valor decimal aleatorio entre 50% y 100% de asistencia a clases.
Promedio: Un valor decimal aleatorio entre 5 y 10, que representa el promedio académico del estudiante.
Uso_online: Un valor decimal aleatorio entre 0 y 15 horas semanales de uso de plataformas de aprendizaje online.
Abandono: Un valor binario (0 o 1) que indica si el estudiante abandonará sus estudios o no.
Aquí, el valor 0 indica que el estudiante no abandonará y 1 indica que abandonará.
La probabilidad de que un estudiante abandone es del 30% (probabilidad de 0.3) y la probabilidad de que no abandone es del 70% (probabilidad de 0.7).
🔹 Clase ModeloAbandono
La clase ModeloAbandono se encargará de entrenar un modelo de Machine Learning para predecir si un estudiante abandonará o no sus estudios, basándose en las características proporcionadas en el conjunto de datos generado anteriormente (como edad, horas de estudio, asistencia, etc.).
El modelo se construirá utilizando un árbol de decisión (Decision Tree) que es un algoritmo comúnmente usado para tareas de clasificación.
Qué Debe Hacer el Alumno
Definir la clase ModeloAbandono:
La clase debe ser capaz de:
Entrenar un modelo de Machine Learning utilizando un conjunto de datos de estudiantes.
Evaluar el rendimiento del modelo.
Predecir si un estudiante específico abandonará o no sus estudios.
Atributos de la clase:
max_depth: Este es un parámetro del clasificador de árbol de decisión que define la profundidad máxima del árbol (por defecto, 4).
random_state: Semilla para la aleatoriedad, lo que asegura que los resultados sean reproducibles.
modelo: Este atributo será el modelo de árbol de decisión que se entrenará.
Métodos de la clase:
entrenar(data):
Este método debe recibir un DataFrame con los datos de los estudiantes, separar las características (X) de la variable objetivo (y), y dividir los datos en conjuntos de entrenamiento y prueba.
Debe entrenar un clasificador de árbol de decisión (DecisionTreeClassifier), ajustando el modelo a los datos de entrenamiento.
evaluar():
Este método debe evaluar el rendimiento del modelo usando los datos de prueba y calcular la precisión del modelo utilizando accuracy_score.
También debe mostrar un reporte de clasificación usando la función classification_report, que incluye métricas como precisión, recall, y f1-score.
predecir_estudiante(estudiante_df):
Este método debe recibir un DataFrame con los datos de un estudiante y predecir si ese estudiante abandonará o no.
La salida debe ser "Abandonará" si el modelo predice 1 (abandono), o "Seguirá estudiando" si el modelo predice 0 (no abandono).
🔹 Clase TestBasicoModeloAbandono
La clase TestBasicoModeloAbandono tiene como propósito hacer pruebas simples para validar que la solución de predicción del abandono estudiantil funciona correctamente.
El alumno debe asegurarse de que el entrenamiento del modelo, su evaluación y las predicciones para nuevos estudiantes se realicen correctamente.
Qué Debe Hacer el Alumno
Definir la clase TestBasicoModeloAbandono:
Esta clase tiene como objetivo integrar los componentes de simulación, entrenamiento, evaluación y predicción de manera que sea fácil verificar el funcionamiento de las clases previas (como SimuladorDatos y ModeloAbandono).
Método ejecutar():
Este método será el punto de entrada donde se llevarán a cabo las siguientes acciones:
Generar datos simulados utilizando la clase SimuladorDatos.
Entrenar el modelo utilizando la clase ModeloAbandono.
Evaluar el modelo y mostrar los resultados de la precisión y el reporte de clasificación.
Realizar una predicción para un nuevo estudiante y mostrar el resultado.
Estructura de la Clase TestBasicoModeloAbandono
Método ejecutar()
Este método tiene como objetivo ejecutar una serie de pasos secuenciales que permitan probar la funcionalidad del flujo completo de la predicción:
Generar los datos simulados:
Usar la clase SimuladorDatos para generar un conjunto de datos de 200 estudiantes, con diferentes características y etiquetas de abandono.
Entrenar el modelo:
Utilizar la clase ModeloAbandono para entrenar un modelo con los datos generados.
El modelo debe entrenarse con las características como Edad, Horas_estudio, Asistencia, etc., y aprender a predecir la variable Abandono.

Evaluar el modelo:
Evaluar el modelo utilizando el conjunto de datos de prueba, calcular la precisión, y generar el reporte de clasificación. Esto verificará que el modelo está funcionando correctamente.

Realizar una predicción:
Crear un nuevo estudiante con características específicas y utilizar el modelo entrenado para predecir si ese estudiante abandonará o no sus estudios.

🎯 Ejemplo de uso
test = TestModeloAbandono()
test.ejecutar()
Resultado esperado
Datos simulados:
    Edad  Horas_estudio  Asistencia  Promedio  Uso_online  Abandono
0    24      10.128455   55.803632  7.777159    7.845981         0
1    21      28.287291   52.300132  8.844937    5.382457         0
2    28       9.696088   52.036440  9.723829   13.158008         0
3    25      15.563719   92.773029  9.248237    5.886677         0
4    22      21.090569   85.182893  6.236741   12.248992         1
Entrenamiento completado.
Precisión del modelo: 0.57
Reporte de clasificación:
               precision    recall  f1-score   support
 
           0       0.59      0.96      0.73        24
           1       0.00      0.00      0.00        16
 
    accuracy                           0.57        40
   macro avg       0.29      0.48      0.37        40
weighted avg       0.35      0.57      0.44        40
El estudiante probablemente: Seguirá estudiando
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

class SimuladorDatos:
    """
    Genera un conjunto de datos simulados para predecir el abandono estudiantil.
    """
    def __init__(self, n=200, seed=42):
        """
        Inicializa el simulador.

        Args:
            n (int): Número de registros a generar (por defecto 200).
            seed (int): Semilla para la generación aleatoria (por defecto 42).
        """
        self.n = n
        self.seed = seed
        # Define los nombres de las columnas para asegurar el orden y consistencia
        self.column_names = ['Edad', 'Horas_estudio', 'Asistencia', 'Promedio', 'Uso_online', 'Abandono']

    def generar(self):
        """
        Genera y devuelve un DataFrame de pandas con datos simulados de estudiantes.

        Returns:
            pandas.DataFrame: DataFrame con los datos simulados.
        """
        np.random.seed(self.seed) # Asegura la reproducibilidad
        data = pd.DataFrame({
            'Edad': np.random.randint(18, 30 + 1, size=self.n), # Edad entre 18 y 30 (inclusive)
            'Horas_estudio': np.random.uniform(0, 30, size=self.n), # Horas de estudio entre 0 y 30
            'Asistencia': np.random.uniform(50, 100, size=self.n), # Asistencia entre 50% y 100%
            'Promedio': np.random.uniform(5, 10, size=self.n), # Promedio entre 5 y 10
            'Uso_online': np.random.uniform(0, 15, size=self.n), # Uso online entre 0 y 15 horas
            'Abandono': np.random.choice([0, 1], size=self.n, p=[0.7, 0.3]) # 0: No abandona (70%), 1: Abandona (30%)
        })
        # Reordena las columnas según self.column_names para mantener el formato esperado
        data = data[self.column_names]
        return data

class ModeloAbandono:
    """
    Entrena, evalúa y realiza predicciones con un modelo de árbol de decisión
    para predecir el abandono estudiantil.
    """
    def __init__(self, max_depth=4, random_state=42):
        """
        Inicializa el modelo de abandono.

        Args:
            max_depth (int): Profundidad máxima del árbol de decisión (por defecto 4).
            random_state (int): Semilla para la aleatoriedad del modelo (por defecto 42).
        """
        self.max_depth = max_depth
        self.random_state = random_state
        self.modelo = None # El modelo DecisionTreeClassifier se almacenará aquí
        # Atributos para almacenar los datos de entrenamiento/prueba y nombres de características
        # Se nombran sin guion bajo al final según requerimiento del entorno de prueba.
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.feature_names = None # Lista con los nombres de las columnas de características

    def entrenar(self, data):
        """
        Entrena el modelo de árbol de decisión.

        Args:
            data (pandas.DataFrame): DataFrame con los datos de los estudiantes,
                                     incluyendo la columna 'Abandono'.
        """
        if 'Abandono' not in data.columns:
            raise ValueError("La columna 'Abandono' no se encuentra en los datos.")
        
        # Separa las características (X) de la variable objetivo (y)
        X = data.drop('Abandono', axis=1)
        y = data['Abandono']
        self.feature_names = X.columns.tolist() # Guarda los nombres de las características

        # Divide los datos en conjuntos de entrenamiento y prueba
        # stratify=y asegura que la proporción de clases se mantenga en ambos conjuntos
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=self.random_state, stratify=y
        )
        
        # Inicializa y entrena el clasificador de árbol de decisión
        self.modelo = DecisionTreeClassifier(
            max_depth=self.max_depth, 
            random_state=self.random_state
        )
        self.modelo.fit(self.X_train, self.y_train)
        print("Entrenamiento completado.")

    def evaluar(self):
        """
        Evalúa el rendimiento del modelo entrenado utilizando los datos de prueba.
        Muestra la precisión y el reporte de clasificación.
        """
        if self.modelo is None or self.X_test is None or self.y_test is None:
            print("El modelo no ha sido entrenado o los datos de prueba no están disponibles.")
            return

        # Realiza predicciones sobre el conjunto de prueba
        y_pred = self.modelo.predict(self.X_test)
        
        # Calcula la precisión
        accuracy = accuracy_score(self.y_test, y_pred)
        
        # Genera el reporte de clasificación (precisión, recall, f1-score)
        # zero_division=0 evita warnings si alguna clase no tiene predicciones, mostrando 0.0
        report = classification_report(self.y_test, y_pred, zero_division=0) 
        
        print(f"Precisión del modelo: {accuracy:.2f}")
        print(f"Reporte de clasificación:\n{report}")

    def predecir_estudiante(self, estudiante_df):
        """
        Predice si un estudiante específico abandonará o no sus estudios.

        Args:
            estudiante_df (pandas.DataFrame): DataFrame con los datos de un único estudiante.
                                             Debe contener las mismas columnas de características
                                             que los datos de entrenamiento.

        Returns:
            str: "Abandonará" o "Seguirá estudiando", o un mensaje de error.
        """
        if self.modelo is None:
            print("El modelo no ha sido entrenado.")
            return "Error: Modelo no entrenado"
        
        if not isinstance(estudiante_df, pd.DataFrame):
            raise ValueError("Los datos del estudiante deben ser un DataFrame de pandas.")

        # Asegura que el DataFrame del estudiante tenga las columnas correctas y en el orden esperado
        try:
            # Reordena/selecciona las columnas del DataFrame del estudiante para que coincidan con self.feature_names
            estudiante_df_aligned = estudiante_df[self.feature_names]
        except KeyError as e:
            print(f"Error: Faltan columnas en los datos del estudiante o nombres incorrectos: {e}")
            print(f"Se esperaban las columnas: {self.feature_names}")
            return "Error: Datos del estudiante incompletos o incorrectos"

        # Realiza la predicción
        prediccion = self.modelo.predict(estudiante_df_aligned)[0] # [0] para obtener el valor de la predicción
        
        return "Abandonará" if prediccion == 1 else "Seguirá estudiando"

class TestBasicoModeloAbandono:
    """
    Clase para probar el flujo completo: simulación, entrenamiento, evaluación y predicción.
    """
    def ejecutar(self):
        """
        Ejecuta el proceso completo de prueba del modelo de abandono.
        """
        # 1. Generar datos simulados
        print("Generando datos simulados...")
        simulador = SimuladorDatos(n=200, seed=42)
        datos_simulados = simulador.generar()
        print("Datos simulados (primeras 5 filas):")
        print(datos_simulados.head())
        print("-" * 30)

        # 2. Entrenar el modelo
        print("Entrenando el modelo...")
        # Se usa max_depth=4 y random_state=42 según los requisitos de la clase ModeloAbandono
        modelo_abandono = ModeloAbandono(max_depth=4, random_state=42) 
        modelo_abandono.entrenar(datos_simulados)
        print("-" * 30)

        # 3. Evaluar el modelo
        print("Evaluando el modelo...")
        modelo_abandono.evaluar()
        print("-" * 30)

        # 4. Realizar una predicción para un nuevo estudiante
        print("Realizando predicción para un nuevo estudiante...")
        # Crear un DataFrame para el nuevo estudiante.
        # Es crucial que las columnas coincidan con `modelo_abandono.feature_names`
        # en nombre y orden.
        nuevo_estudiante_datos = pd.DataFrame({
            'Edad': [22],
            'Horas_estudio': [5],    # Bajas horas de estudio, posible indicador de abandono
            'Asistencia': [60],      # Baja asistencia, posible indicador de abandono
            'Promedio': [5.5],       # Bajo promedio, posible indicador de abandono
            'Uso_online': [2]        # Bajo uso online
        }, columns=modelo_abandono.feature_names) # Asegura el orden y nombres de columnas

        prediccion_nuevo = modelo_abandono.predecir_estudiante(nuevo_estudiante_datos)
        print(f"Predicción para el nuevo estudiante: {prediccion_nuevo}")


# Ejemplo de uso según el problema
if __name__ == "__main__":
    # El problema indica TestModeloAbandono() en el ejemplo de uso,
    # pero la clase se llama TestBasicoModeloAbandono.
    test = TestBasicoModeloAbandono() 
    test.ejecutar()
