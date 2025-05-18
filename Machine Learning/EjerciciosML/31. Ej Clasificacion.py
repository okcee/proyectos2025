''' Clasificador de jugadores de baloncesto - Practicar con numpy para generar datos, arboles de decision para realizar clasificaciones de jugadores, y pandas con matplotlib para graficar los resultados obtenidos.

Objetivo del ejercicio:
Tu misión es construir un modelo inteligente que clasifique a jugadores de baloncesto según su rendimiento en tres categorías: "Bajo", "Medio" y "Alto", utilizando para ello sus características físicas y estadísticas de juego.
Usarás el algoritmo de árboles de decisión junto con NumPy, pandas, matplotlib y scikit-learn.

🎯 Contexto del problema
Un equipo de baloncesto ficticio está evaluando a nuevos jugadores y necesita una herramienta que, a partir de la altura, el peso y el promedio de puntos por partido, determine automáticamente el nivel de rendimiento del jugador.
Esta herramienta será clave para seleccionar a los mejores candidatos.

🧱 Estructura sugerida de la solución
1. BasketballPlayer
Una clase que representa a cada jugador. Sus atributos son:
height (int): altura en centímetros.
weight (int): peso en kilogramos.
avg_points (float): promedio de puntos por partido.
performance (str): nivel de rendimiento, con valores "Bajo", "Medio" o "Alto".
Método útil:
to_vector(): devuelve [height, weight, avg_points] para ser usado por el modelo.
2. BasketballDataGenerator
Una clase que genera datos sintéticos simulando jugadores reales.
Método clave:
generate(): devuelve una lista de objetos BasketballPlayer. La clasificación se basa en el promedio de puntos:
Menos de 8 puntos → "Bajo"
Entre 8 y 15 puntos → "Medio"
Más de 15 puntos → "Alto"
3. BasketballPerformanceClassifier
Encapsula el modelo de árbol de decisión. Métodos clave:
fit(players): entrena el modelo con una lista de jugadores.
predict(height, weight, avg_points): predice el rendimiento de un nuevo jugador.
evaluate(players): imprime la matriz de confusión y el informe de clasificación sobre un conjunto de prueba.
4. BasketballPredictionExample
Contiene el flujo principal:
Generar datos.
Dividirlos en entrenamiento y prueba.
Entrenar y evaluar el clasificador.
Hacer una predicción para un nuevo jugador (por ejemplo: altura = 198 cm, peso = 92 kg, puntos = 17).
Visualizar los jugadores usando matplotlib, diferenciando el rendimiento por colores.

📊 Visualización esperada
Un gráfico de dispersión donde cada punto representa un jugador.
El eje X muestra la altura y el eje Y el promedio de puntos.
El color indica el rendimiento:
🔴 Bajo
🟠 Medio
🟢 Alto

✅ Requisitos técnicos
Usa NumPy para generar datos aleatorios.
Usa pandas para crear el DataFrame de visualización.
Usa DecisionTreeClassifier de sklearn.tree.
Representa visualmente los datos con matplotlib.

🧪 Ejemplo de uso

example = BasketballPredictionExample()
example.run()

Salida esperada

Confusion Matrix:
[[10  0  0]
 [ 0 23  0]
 [ 0  0 27]]
 
Classification Report:
              precision    recall  f1-score   support
 
        Alto       1.00      1.00      1.00        10
        Bajo       1.00      1.00      1.00        23
       Medio       1.00      1.00      1.00        27
 
    accuracy                           1.00        60
   macro avg       1.00      1.00      1.00        60
weighted avg       1.00      1.00      1.00        60
 
 
🎯 Predicción personalizada → Altura: 198 cm, Peso: 92 kg, Prom. puntos: 17
   → Categoría predicha: Alto
'''

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class BasketballPlayer:
    def __init__(self, height, weight, avg_points, performance):
        self.height = height          # Altura en centímetros
        self.weight = weight          # Peso en kilogramos
        self.avg_points = avg_points  # Promedio de puntos por partido
        self.performance = performance  # Rendimiento: Bajo, Medio o Alto

    def to_vector(self):
        return [self.height, self.weight, self.avg_points]

class BasketballDataGenerator:
    def __init__(self, num_samples=200):
        self.num_samples = num_samples

    def generate(self):
        heights = np.random.normal(190, 10, self.num_samples)    # Altura media de 190 cm
        weights = np.random.normal(85, 10, self.num_samples)     # Peso medio de 85 kg
        points = np.random.normal(10, 5, self.num_samples)       # Puntos por partido, media 10

        data = []
        for h, w, p in zip(heights, weights, points):
            if p < 8:
                perf = "Bajo"
            elif p < 15:
                perf = "Medio"
            else:
                perf = "Alto"
            data.append(BasketballPlayer(h, w, max(0, p), perf))  # Evita puntos negativos

        return data

class BasketballPerformanceClassifier:
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def fit(self, players):
        X = [p.to_vector() for p in players]
        y = [p.performance for p in players]
        self.model.fit(X, y)

    def predict(self, height, weight, avg_points):
        return self.model.predict([[height, weight, avg_points]])[0]

    def evaluate(self, players):
        X = [p.to_vector() for p in players]
        y = [p.performance for p in players]
        y_pred = self.model.predict(X)

        print("Confusion Matrix:")
        print(confusion_matrix(y, y_pred))
        print("\nClassification Report:")
        print(classification_report(y, y_pred))

class BasketballPredictionExample:
    def run(self):
        generator = BasketballDataGenerator()
        data = generator.generate()

        train_data, test_data = train_test_split(data, test_size=0.3, random_state=1)

        classifier = BasketballPerformanceClassifier()
        classifier.fit(train_data)
        classifier.evaluate(test_data)

        # Ejemplo de predicción personalizada
        height, weight, points = 198, 92, 17
        prediction = classifier.predict(height, weight, points)
        print(f"\n🎯 Predicción personalizada → Altura: {height} cm, Peso: {weight} kg, Prom. puntos: {points}")
        print(f"   → Categoría predicha: {prediction}")

        # Visualización con Matplotlib
        df = pd.DataFrame({
            "Altura": [p.height for p in data],
            "Prom. Puntos": [p.avg_points for p in data],
            "Rendimiento": [p.performance for p in data]
        })

        colores = {
            "Bajo": "red",
            "Medio": "orange",
            "Alto": "green"
        }

        plt.figure(figsize=(8, 6))
        for nivel, color in colores.items():
            subset = df[df["Rendimiento"] == nivel]
            plt.scatter(subset["Altura"], subset["Prom. Puntos"], label=nivel, c=color, alpha=0.6)

        plt.xlabel("Altura (cm)")
        plt.ylabel("Promedio de puntos por partido")
        plt.title("🏀 Clasificación de jugadores de baloncesto por rendimiento")
        plt.grid(True)
        plt.legend(title="Rendimiento")
        plt.show()

# Ejecución final
example = BasketballPredictionExample()
example.run()

