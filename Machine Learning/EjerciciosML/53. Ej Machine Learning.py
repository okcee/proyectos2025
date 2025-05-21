''' Predicción del consumo energético - Practicar con numpy para generar datos sintéticos, con regresión lineal para realizar estimaciones de consumo energético y con matplotlib para construir un gráfico con los datos obtenidos

📘 Contexto:
La eficiencia energética es una prioridad en las ciudades modernas. Las compañías eléctricas intentan predecir cuánto se consumirá en función de las condiciones meteorológicas. En este proyecto, desarrollarás un modelo de regresión lineal que permita predecir el consumo de energía en función de la temperatura ambiental.

🎯 Objetivo del proyecto:
Construir un sistema que:
Genere datos sintéticos con numpy representando temperatura (°C) y consumo energético (kWh).
Use regresión lineal (sklearn.linear_model.LinearRegression) para aprender la relación entre ambas variables.
Permita hacer predicciones para nuevas temperaturas.
Visualice los datos y el modelo con matplotlib.

🛠️ Requerimientos:
1. Crear una clase EnergyRecord
Guarda los atributos: temperature y consumption.
Añade un método .to_vector() que devuelva [temperature] como vector de entrada al modelo.
2. Generar los datos con una clase EnergyDataGenerator
Crea datos sintéticos con numpy.random.uniform(-5, 35) para la temperatura.
Calcula el consumo simulando que cuando hace más frío o más calor que 20 °C, el consumo aumenta:
consumo = 100 + (abs(temperatura - 20) * 3) + ruido
Añade un poco de ruido con numpy.random.normal(0, 5).
El método generate() devuelve una lista de objetos EnergyRecord
3. Crear la clase EnergyRegressor
Usa LinearRegression de sklearn para ajustar el modelo.
Métodos necesarios:
fit() para entrenar con una lista de EnergyRecord.
predict(temperature) para predecir consumo dado una temperatura.
get_model() para acceder al modelo (útil para graficar).
4. Implementar una clase EnergyPredictionExample
Que cree los datos, entrene el modelo y prediga para una temperatura nueva (por ejemplo, 30 °C).
También debe mostrar una gráfica:
Un scatter plot de los datos.
Una línea roja representando la recta de regresión.
5. Visualización con matplotlib
Agrega títulos, etiquetas de ejes y leyenda para una mejor comprensión.
Usa .plot() para la línea de predicción del modelo.

✅ Ejemplo de uso
example = EnergyPredictionExample()
example.run()

Salida esperada
🔍 Temperatura: 30 °C
⚡ Predicción de consumo: 120.70 kWh
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class EnergyRecord:
    """
    Guarda los atributos: temperature y consumption.
    """
    def __init__(self, temperature, consumption):
        """
        Inicializa un registro de energía.

        Args:
            temperature (float): La temperatura en °C.
            consumption (float): El consumo energético en kWh.
        """
        self.temperature = temperature
        self.consumption = consumption

    def to_vector(self):
        """
        Devuelve [temperature] como vector de entrada al modelo.
        sklearn espera una matriz 2D para X, así que esto será [temperature].
        """
        return [self.temperature]

class EnergyDataGenerator:
    """
    Genera datos sintéticos de temperatura y consumo energético.
    """
    def __init__(self, num_samples=100):
        """
        Inicializa el generador de datos.

        Args:
            num_samples (int): Número de muestras de datos a generar.
        """
        self.num_samples = num_samples

    def generate(self):
        """
        Genera datos sintéticos.
        - Temperatura: Distribución uniforme entre -5°C y 35°C.
        - Consumo: 100 + (abs(temperatura - 20) * 3) + ruido.
        - Ruido: Distribución normal con media 0 y desviación estándar 5.

        Returns:
            list: Una lista de objetos EnergyRecord.
        """
        # Generar temperaturas
        temperatures = np.random.uniform(-5, 35, self.num_samples)
        
        # Generar ruido
        noise = np.random.normal(0, 5, self.num_samples)
        
        # Calcular consumo
        # El consumo aumenta cuando la temperatura se aleja de 20°C (hacia más frío o más calor)
        consumptions = 100 + (np.abs(temperatures - 20) * 3) + noise
        
        records = []
        for temp, cons in zip(temperatures, consumptions):
            records.append(EnergyRecord(temp, cons))
            
        return records

class EnergyRegressor:
    """
    Ajusta un modelo de regresión lineal y realiza predicciones.
    """
    def __init__(self):
        """
        Inicializa el regresor con un modelo de LinearRegression de sklearn.
        """
        self.model = LinearRegression()

    def fit(self, records):
        """
        Entrena el modelo de regresión lineal.

        Args:
            records (list): Una lista de objetos EnergyRecord para entrenar el modelo.
        """
        # Preparar los datos para sklearn
        # X debe ser una matriz 2D donde cada fila es una muestra y cada columna es una característica
        # y debe ser un vector 1D de los valores objetivo
        X_train = np.array([record.to_vector() for record in records])
        y_train = np.array([record.consumption for record in records])
        
        self.model.fit(X_train, y_train)

    def predict(self, temperature):
        """
        Predice el consumo energético para una temperatura dada.

        Args:
            temperature (float): La temperatura para la cual predecir el consumo.

        Returns:
            float: El consumo energético predicho en kWh.
        """
        # El modelo espera una entrada 2D ([[-5], [0], [30]]), incluso para una sola predicción
        temp_vector = np.array([[temperature]])
        prediction = self.model.predict(temp_vector)
        return prediction[0]

    def get_model(self):
        """
        Devuelve el modelo de regresión lineal entrenado.

        Returns:
            LinearRegression: El objeto del modelo de sklearn.
        """
        return self.model

class EnergyPredictionExample:
    """
    Orquesta la generación de datos, entrenamiento del modelo, predicción y visualización.
    """
    def __init__(self, num_samples=100, temp_to_predict=30.0):
        """
        Inicializa el ejemplo de predicción.

        Args:
            num_samples (int): Número de muestras de datos sintéticos a generar.
            temp_to_predict (float): Temperatura para la cual se realizará una predicción.
        """
        self.num_samples = num_samples
        self.temp_to_predict = temp_to_predict
        self.data_generator = EnergyDataGenerator(num_samples=self.num_samples)
        self.regressor = EnergyRegressor()
        self.records = None

    def run(self):
        """
        Ejecuta el flujo completo: generar datos, entrenar, predecir y visualizar.
        """
        # 1. Generar datos
        self.records = self.data_generator.generate()
        
        # 2. Entrenar el modelo
        self.regressor.fit(self.records)
        
        # 3. Predecir para una nueva temperatura
        predicted_consumption = self.regressor.predict(self.temp_to_predict)
        
        print(f"🔍 Temperatura: {self.temp_to_predict}°C")
        print(f"⚡ Predicción de consumo: {predicted_consumption:.2f} kWh")
        
        # 4. Visualizar los datos y el modelo
        self._plot_results()

    def _plot_results(self):
        """
        Muestra una gráfica con los datos generados y la recta de regresión.
        """
        if not self.records:
            print("No hay datos para graficar. Ejecute run() primero.")
            return

        temperatures = np.array([record.temperature for record in self.records])
        consumptions = np.array([record.consumption for record in self.records])

        plt.figure(figsize=(10, 6))
        
        # Scatter plot de los datos originales
        plt.scatter(temperatures, consumptions, alpha=0.6, label='Datos Sintéticos')
        
        # Línea de regresión
        # Generar puntos para la línea de regresión basados en el rango de temperaturas observadas
        model = self.regressor.get_model()
        x_line = np.linspace(temperatures.min(), temperatures.max(), 100).reshape(-1, 1)
        y_line = model.predict(x_line)
        
        plt.plot(x_line, y_line, color='red', linewidth=2, label='Recta de Regresión Lineal')
        
        # Títulos y etiquetas
        plt.title('Predicción de Consumo Energético vs. Temperatura')
        plt.xlabel('Temperatura (°C)')
        plt.ylabel('Consumo Energético (kWh)')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # Ejemplo de uso
    example = EnergyPredictionExample(num_samples=200, temp_to_predict=30.0)
    example.run()

    # Ejemplo con otra temperatura para probar
    # example_cold = EnergyPredictionExample(num_samples=200, temp_to_predict=-2.0)
    # example_cold.run()

'''
Resuelve en un script python el ejercicio: @51. Ej Machine Learning.py
Crea el código limpio y con comentarios que sea compatible con el entorno de udemy.
No es necesario explicaciones, solo el script para copiar.
'''