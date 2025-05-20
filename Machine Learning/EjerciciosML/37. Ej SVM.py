''' Detectar jugadores con potencial profesional - Practicar con el algoritmo de máquinas de vector de soporte SVM

🎮 Ejercicio: ¿Quién será un jugador profesional? - Clasificación con SVM

🧠 Contexto:
Imagina que trabajas en una plataforma de eSports y tu equipo está desarrollando un sistema de scouting para detectar jugadores con potencial profesional en base a sus estadísticas de juego.
Tu tarea es construir un modelo de clasificación usando SVM (Support Vector Machine) que, dada la información de un jugador, prediga si tiene el perfil de jugador profesional (1) o no (0).

📋 Objetivo del ejercicio
Implementar un clasificador que:
Use datos simulados de jugadores (partidas ganadas, horas jugadas, precisión, velocidad de reacción, estrategia).
Entrene un modelo de SVM con scikit-learn.
Clasifique a nuevos jugadores como "pro" o "casual".
Evalúe el modelo con métricas de precisión.

📁 Datos de entrada:
Cada jugador se representa con las siguientes características (todas normalizadas entre 0 y 1):

🧪 Ejemplo de datos
simulator = GameSimulator()
simulator.run()
Salida esperada
Jugador profesional:
Precisión del modelo: 1.00

🛠️ Tareas a realizar:
Implementa la clase ProPlayerClassifier con los métodos:
train(X, y) para entrenar el modelo.
predict(player_stats) para predecir si un jugador es profesional.
Usa sklearn.svm.SVC como modelo base.
Prueba el modelo con al menos 2 predicciones distintas.
Evalúa el rendimiento con accuracy_score.
'''

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class GameSimulator:
    def __init__(self, n_players=200):
        self.n_players = n_players

    def run(self):
        np.random.seed(42)
        partidas_ganadas = np.random.rand(self.n_players)
        horas_jugadas = np.random.rand(self.n_players)
        precision = np.random.rand(self.n_players)
        reaccion = np.random.rand(self.n_players)
        estrategia = np.random.rand(self.n_players)

        etiquetas = (
            (partidas_ganadas > 0.7) &
            (horas_jugadas > 0.6) &
            (precision > 0.7) &
            (reaccion > 0.6) &
            (estrategia > 0.6)
        ).astype(int)

        X = np.column_stack([partidas_ganadas, horas_jugadas, precision, reaccion, estrategia])
        y = etiquetas
        return X, y


class ProPlayerClassifier:
    def __init__(self):
        self.model = SVC(kernel='rbf', C=1.0, gamma='scale')

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, player_stats):
        prediction = self.model.predict([player_stats])
        return int(prediction[0])

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return accuracy_score(y_test, y_pred)
