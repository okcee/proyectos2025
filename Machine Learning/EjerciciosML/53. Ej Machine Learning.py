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


'''
Resuelve en un script python el ejercicio: @51. Ej Machine Learning.py
Crea el código limpio y con comentarios que sea compatible con el entorno de udemy.
No es necesario explicaciones, solo el script para copiar.
'''