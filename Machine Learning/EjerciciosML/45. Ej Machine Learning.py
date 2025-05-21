''' Predicción del Precio de una Vivienda - Practicar con la eleccion de algoritmo y realizar estimación del precio de una vivienda

🎯 Objetivo
Desarrollar un sistema de predicción que estime el precio de una vivienda en función de sus características (como superficie, número de habitaciones, antigüedad, etc.) utilizando regresión lineal. El sistema debe construirse completamente con clases en Python.

🧱 Paso 1: Simular los datos
Clase: SimuladorViviendas
Esta clase se encargará de generar un conjunto de datos sintéticos con pandas y numpy.
✔️ Instrucciones:
La clase debe llamarse SimuladorViviendas.
Debe tener un método generar_datos() que devuelva un DataFrame con 200 registros y las siguientes columnas:

🔍 Paso 2: Crear el modelo de predicción
Clase: ModeloPrecioVivienda
Esta clase representará el modelo de regresión lineal. Se encargará del entrenamiento, evaluación y predicción.
✔️ Métodos obligatorios:
entrenar(data: pd.DataFrame):
Separa los datos en variables independientes y la variable objetivo (Precio).
Divide los datos en entrenamiento (80%) y prueba (20%).
Entrena un modelo de regresión lineal con scikit-learn.
evaluar():
Muestra el error cuadrático medio (MSE).
Muestra el coeficiente de determinación R².
predecir(nueva_vivienda: pd.DataFrame) -> float:
Recibe un DataFrame con las características de una vivienda.
Devuelve el precio estimado.

🧪 Paso 3: Probar todo en conjunto
Clase: TestModeloPrecio
Esta clase servirá como lanzador general para probar que todo funcione correctamente. Dentro del método ejecutar() debe:
Generar los datos usando SimuladorViviendas.
Entrenar y evaluar el modelo con ModeloPrecioVivienda.
Crear una vivienda de ejemplo (por ejemplo: superficie 120 m², 3 habitaciones, 10 años de antigüedad, 5 km al centro, 2 baños).
Imprimir el precio estimado.
✅ Requisitos técnicos
Usar pandas, numpy y scikit-learn (LinearRegression, train_test_split, mean_squared_error, r2_score).
Las clases deben estar bien documentadas.
El código debe poder ejecutarse de principio a fin sin errores.

🧪 Ejemplo de uso
test = TestModeloPrecio()
test.ejecutar()
Salida esperada
Primeras filas de datos simulados:
    Superficie  Habitaciones  Antigüedad  Distancia_centro  Baños  \
0   87.454012             4          32          9.810270      3   
1  145.071431             3          39          7.713692      1   
2  123.199394             1           9         12.089466      2   
3  109.865848             4          42          2.476958      2   
4   65.601864             4          43         19.513501      2   

          Precio  
0  259267.477436  
1  314958.241175  
2  467942.246565  
3  238538.397746  
4  238781.280758  
Modelo entrenado correctamente.
Error Cuadrático Medio (MSE): 14748907009.71
R² del modelo: 0.02
El precio estimado de la vivienda es: $284,716.76
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class SimuladorViviendas:
    """
    Clase para simular datos de viviendas.
    """

    def generar_datos(self):
        """
        Genera un DataFrame con datos simulados de viviendas.

        Returns:
            pd.DataFrame: DataFrame con las columnas 'Superficie', 'Habitaciones', 
                          'Antigüedad', 'Distancia_centro', 'Baños' y 'Precio'.
        """
        np.random.seed(42)  # Para reproducibilidad
        n_registros = 200
        data = pd.DataFrame({
            'Superficie': np.random.normal(100, 20, n_registros),  # Superficie en m²
            'Habitaciones': np.random.randint(1, 5, n_registros),  # Número de habitaciones
            'Antigüedad': np.random.randint(0, 50, n_registros),  # Antigüedad en años
            'Distancia_centro': np.random.normal(10, 5, n_registros),  # Distancia al centro en km
            'Baños': np.random.randint(1, 4, n_registros)  # Número de baños
        })

        # Generar precio con una relación lineal con las características, más ruido
        precio_base = 100000
        precio_por_m2 = 2000
        precio_por_habitacion = 15000
        precio_por_baño = 10000
        factor_antiguedad = -1000
        factor_distancia = -5000

        data['Precio'] = (precio_base +
                          data['Superficie'] * precio_por_m2 +
                          data['Habitaciones'] * precio_por_habitacion +
                          data['Baños'] * precio_por_baño +
                          data['Antigüedad'] * factor_antiguedad +
                          data['Distancia_centro'] * factor_distancia +
                          np.random.normal(0, 50000, n_registros))  # Ruido

        return data

class ModeloPrecioVivienda:
    """
    Clase para el modelo de regresión lineal de precios de viviendas.
    """

    def __init__(self):
        """
        Inicializa el modelo de regresión lineal.
        """
        self.modelo = LinearRegression()

    def entrenar(self, data: pd.DataFrame):
        """
        Entrena el modelo con los datos proporcionados.

        Args:
            data (pd.DataFrame): DataFrame con las características y el precio de las viviendas.
        """
        # Separar variables independientes (X) y dependiente (y)
        X = data.drop('Precio', axis=1)
        y = data['Precio']

        # Dividir en conjuntos de entrenamiento y prueba
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Entrenar el modelo
        self.modelo.fit(self.X_train, self.y_train)
        print("Modelo entrenado correctamente.")  # Mensaje de confirmación

    def evaluar(self):
        """
        Evalúa el modelo con el conjunto de prueba.

        Returns:
            None: Imprime el MSE y el R².
        """
        # Predecir con el conjunto de prueba
        y_pred = self.modelo.predict(self.X_test)

        # Calcular y mostrar métricas
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
        print(f"R² del modelo: {r2:.2f}")

    def predecir(self, nueva_vivienda: pd.DataFrame) -> float:
        """
        Predice el precio de una nueva vivienda.

        Args:
            nueva_vivienda (pd.DataFrame): DataFrame con las características de la vivienda.

        Returns:
            float: Precio estimado de la vivienda.
        """
        precio_estimado = self.modelo.predict(nueva_vivienda)
        return precio_estimado[0]

class TestModeloPrecio:
    """
    Clase para probar el modelo de predicción de precios de viviendas.
    """

    def ejecutar(self):
        """
        Ejecuta el proceso de generación de datos, entrenamiento, evaluación y predicción.
        """
        # Generar datos
        simulador = SimuladorViviendas()
        datos = simulador.generar_datos()
        print("Primeras filas de datos simulados:")
        print(datos.head())

        # Entrenar y evaluar el modelo
        modelo = ModeloPrecioVivienda()
        modelo.entrenar(datos)
        modelo.evaluar()

        # Crear una vivienda de ejemplo
        vivienda_ejemplo = pd.DataFrame({
            'Superficie': [120],
            'Habitaciones': [3],
            'Antigüedad': [10],
            'Distancia_centro': [5],
            'Baños': [2]
        })

        # Predecir el precio de la vivienda de ejemplo
        precio_estimado = modelo.predecir(vivienda_ejemplo)
        print(f"El precio estimado de la vivienda es: ${precio_estimado:,.2f}")

# Ejemplo de uso
test = TestModeloPrecio()
test.ejecutar()
