import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

''' Ejercicio de codificación 16
Clasificación Binaria
Supongamos que tienes un conjunto de datos que contiene información sobre pacientes y deseas predecir si un paciente tiene una enfermedad (1) o no (0) en función de algunas características médicas, como la edad y los niveles de colesterol.
Tu tarea es desarrollar una función llamada regresion_logistica que tome estos datos como entrada y ajuste un modelo de regresión logística para la clasificación binaria.
def regresion_logistica(datos):
# Ejemplo de uso con datos de pacientes
data = {
    'Edad': [50, 35, 65, 28, 60],
    'Colesterol': [180, 150, 210, 130, 190],
    'Enfermedad': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
modelo_regresion_logistica = regresion_logistica(df)
# Estimaciones de clasificación binaria para nuevos datos
nuevos_datos = pd.DataFrame({'Edad': [45, 55], 'Colesterol': [170, 200]})
estimaciones_clasificacion = modelo_regresion_logistica.predict(nuevos_datos)
print("Estimaciones de Clasificación:")
print(estimaciones_clasificacion)
Resultados:
Estimaciones de Clasificación:
[1 1]
'''
def regresion_logistica(datos):
    # 1. Definir las columnas de características (X) y la columna objetivo (Y)
    features = ['Edad', 'Colesterol']
    target = 'Enfermedad'
    # 2. Seleccionar X e Y del DataFrame de entrada 'datos
    X = datos[features]
    Y = datos[target]
    # 3. Crear una instancia del modelo de Regresión
    modelo = LogisticRegression()
    # 4. Entrenar (ajustar) el modelo
    modelo.fit(X, Y)
    # 5. Devolver el modelo entrenado
    return modelo

# Ejemplo de uso con datos de pacientes
data = {
    'Edad': [50, 35, 65, 28, 60],
    'Colesterol': [180, 150, 210, 130, 190],
    'Enfermedad': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
modelo_regresion_logistica = regresion_logistica(df)

# Estimaciones de clasificación binaria para nuevos datos
nuevos_datos = pd.DataFrame({'Edad': [45, 55], 'Colesterol': [170, 200]})
estimaciones_clasificacion = modelo_regresion_logistica.predict(nuevos_datos)
print("Estimaciones de Clasificación:")
print(estimaciones_clasificacion)
# Salida:
# Estimaciones de Clasificación:
# [1 1]

''' Ejercicio de codificación 17
Predecir futuro de una app
¿Tendrá éxito tu app?
📱 Contexto
Eres parte de un equipo de análisis de una startup que lanza apps móviles. Se te ha asignado la tarea de construir un modelo que pueda predecir si una app será exitosa o no en función de sus métricas iniciales.
La empresa ha recopilado datos de otras apps anteriores, tanto exitosas como fallidas, y quiere automatizar este análisis con Machine Learning.
🎯 Objetivo
Crea un sistema en Python que permita:
Representar los datos de una app.
Preparar un conjunto de datos a partir de múltiples apps.
Entrenar un modelo de regresión logística con scikit-learn.
Predecir si una app será exitosa.
De forma opcional, mostrar la probabilidad de éxito.
🧱 Estructura del proyecto
Debes implementar las siguientes clases:
📦 App
Representa una app móvil con las siguientes características:
app_name: nombre de la app.
monthly_users: número de usuarios mensuales.
avg_session_length: duración media de las sesiones (en minutos).
retention_rate: tasa de retención entre 0 y 1.
social_shares: número de veces que se ha compartido en redes sociales.
success: valor opcional (1 = éxito, 0 = fracaso).
Método:
to_features(self): devuelve una lista de características numéricas.
📊 AppDataset
Representa un conjunto de datos de apps. Debe incluir:
Lista de objetos App.
Métodos:
get_feature_matrix(self): devuelve una matriz de características.
get_target_vector(self): devuelve un vector de etiquetas (success).
🤖 SuccessPredictor
Encargado de entrenar y usar el modelo de regresión logística.
Métodos:
train(dataset): entrena el modelo usando un AppDataset.
predict(app): devuelve 1 o 0 para predecir si la app será exitosa.
predict_proba(app): (opcional) devuelve la probabilidad de éxito como número decimal entre 0 y 1.
💡 Sugerencia: puedes usar StandardScaler para mejorar la precisión del modelo escalando los datos.
Ejemplo de uso:
# Datos de entrenamiento
apps = [
    App("FastChat", 10000, 12.5, 0.65, 1500, 1),
    App("FitTrack", 500, 5.0, 0.2, 50, 0),
    App("GameHub", 15000, 25.0, 0.75, 3000, 1),
    App("BudgetBuddy", 800, 6.5, 0.3, 80, 0),
    App("EduFlash", 12000, 18.0, 0.7, 2200, 1),
    App("NoteKeeper", 600, 4.0, 0.15, 30, 0)
]
dataset = AppDataset(apps)
predictor = SuccessPredictor()
predictor.train(dataset)
# Nueva app a evaluar
new_app = App("StudyBoost", 20000, 15.0, 0.5, 700)
predicted_success = predictor.predict(new_app)
prob = predictor.predict_proba(new_app)
print(f"¿Será exitosa la app {new_app.app_name}? {'Sí' if predicted_success else 'No'}")
print(f"Probabilidad estimada de éxito: {prob:.2f}")
'''
class App:
    def __init__ (self, app_name, monthly_users, avg_session_length, retention_rate, social_shares, success=None):
        self.app_name = app_name
        self.monthly_users = monthly_users
        self.avg_session_length = avg_session_length
        self.retention_rate = retention_rate
        self.social_shares = social_shares
        self.success = success
    def to_features(self):
        return [self.monthly_users, self.avg_session_length, self.retention_rate, self.social_shares]

class AppDataset:
    def __init__ (self, apps_list):
        self.apps_list = apps_list
    def get_feature_matrix(self):
        return [app.to_features() for app in self.apps_list]
    def get_target_vector(self):
        return [app.success for app in self.apps_list if app.success is not None] # Asegurarse de que solo se incluyen apps con valor de 'success' conocido

class SuccessPredictor:
    def __init__ (self):
        self.model = LogisticRegression()
        self.escalador = StandardScaler() # Añadido: Inicializa el StandardScaler. Objeto para escalar los datos
        self.escalador_ajustado = False # Añadido: Flag para saber si el escalador ya aprendió la escala
    def train(self, dataset: AppDataset):
        X = dataset.get_feature_matrix()
        Y = dataset.get_target_vector()
        X_scaled = self.escalador.fit_transform(X) # Ajustar el escalador a los datos de entrenamiento Y transformarlos
        self.escalador_ajustado = True # Marcar que el escalador está listo
        self.model.fit(X_scaled, Y)
    def predict(self, app: App):
        """
        Predice la clase (0 o 1) para una nueva app.
        Escala las características de la app usando el escalador ya ajustado.
        """
        if not self.escalador_ajustado:
            raise RuntimeError("El predictor debe ser entrenado ('train') antes de hacer predicciones.")
        # 1. Obtener características de la app
        caracteristicas_app = app.to_features()
        datos_para_predecir = [caracteristicas_app] # Formato 2D requerido
        # 2. Escalar las características
        datos_escalados = self.escalador.transform(datos_para_predecir)
        # 3. Hacer predicción con datos escalados
        predicciones = self.model.predict(datos_escalados)
        valor_predicho = predicciones[0]
        return int(valor_predicho)
    def predict_proba(self, app: App):
        """
        Predice la probabilidad de éxito (clase 1) para una nueva app.
        Escala las características de la app usando el escalador ya ajustado.
        """
        if not self.escalador_ajustado:
             raise RuntimeError("El predictor debe ser entrenado ('train') antes de predecir probabilidades.")
        # 1. Obtener características de la app
        caracteristicas_app = app.to_features()
        datos_para_predecir = [caracteristicas_app] # Formato 2D
        # --- CORRECCIÓN: Escalar los datos de la nueva app ---
        # 2. Usar transform() para aplicar la escala aprendida en train
        datos_escalados = self.escalador.transform(datos_para_predecir)
        # 3. Predecir probabilidades usando los datos ESCALADOS
        probabilidades = self.model.predict_proba(datos_escalados)
        # ------------------------------------------------------
        # predict_proba devuelve [[prob_clase_0, prob_clase_1]]
        probabilidad_exitosa = probabilidades[0][1]
        return float(probabilidad_exitosa)

# Datos de entrenamiento
apps = [
    App("FastChat", 10000, 12.5, 0.65, 1500, 1),
    App("FitTrack", 500, 5.0, 0.2, 50, 0),
    App("GameHub", 15000, 25.0, 0.75, 3000, 1),
    App("BudgetBuddy", 800, 6.5, 0.3, 80, 0),
    App("EduFlash", 12000, 18.0, 0.7, 2200, 1),
    App("NoteKeeper", 600, 4.0, 0.15, 30, 0)
]
 
dataset = AppDataset(apps)
predictor = SuccessPredictor()
predictor.train(dataset)
 
# Nueva app a evaluar
new_app = App("StudyBoost", 20000, 15.0, 0.5, 700)
predicted_success = predictor.predict(new_app)
prob = predictor.predict_proba(new_app)
 
print(f"¿Será exitosa la app {new_app.app_name}? {'Sí' if predicted_success else 'No'}")
print(f"Probabilidad estimada de éxito: {prob:.2f}")

''' Ejercicio de codificación 18
Predecir resultados en partidas multijugador
🧠 Objetivo
En este ejercicio, aplicarás tus conocimientos de regresión logística para construir un modelo capaz de predecir si un jugador ganó o perdió una partida, a partir de sus estadísticas individuales.
📋 Descripción del problema
Tienes que construir un modelo predictivo que, a partir de las estadísticas de un jugador en una partida, determine si ganó o no. Para ello, deberás:
Crear datos sintéticos que representen partidas ficticias de jugadores.
Entrenar un modelo de regresión logística con esos datos.
Implementar una función que prediga el resultado (ganar o no) para un nuevo jugador.

📦 Paso 1: Definir una clase para representar una partida
Crea una clase PlayerMatchData con los siguientes atributos:
kills: número de enemigos eliminados
deaths: número de veces que el jugador ha muerto
assists: asistencias realizadas
damage_dealt: daño total infligido
damage_received: daño total recibido
healing_done: curación realizada
objective_time: tiempo (en segundos) que el jugador estuvo capturando objetivos
won: 1 si el jugador ganó la partida, 0 si perdió
Incluye un método .to_dict() que devuelva los datos como un diccionario (sin la variable won, opcionalmente).

📦 Paso 2: Generar datos sintéticos con NumPy
Crea una función llamada generate_synthetic_data que genere un conjunto de datos de entrenamiento simulando partidas de videojuegos. Para ello:
Utiliza la librería numpy para generar los valores numéricos.
Cada instancia representará el desempeño de un jugador en una partida.
La función debe devolver una lista de objetos PlayerMatchData (ya definida previamente).
Implementa la siguiente lógica para cada jugador:
Reglas para los datos:
kills: número de enemigos eliminados, generado con una distribución de Poisson con media 5.
kills = np.random.poisson(5)
deaths: número de veces que el jugador ha muerto, distribución de Poisson con media 3.
assists: asistencias realizadas, distribución de Poisson con media 2.
damage_dealt: daño infligido, calculado como kills * 300 + ruido aleatorio normal.
damage_received = deaths * 400 + np.random.normal(0, 100)
damage_received: daño recibido, como deaths * 400 + ruido aleatorio normal.
healing_done: cantidad de curación, valor aleatorio entero entre 0 y 300.
objective_time: tiempo (en segundos) controlando objetivos, valor aleatorio entre 0 y 120.
won: el jugador se considera que ganó la partida si hizo más daño del que recibió y tuvo más kills que muertes.
🧠 Tu función debe seguir esta estructura:
import numpy as np
def generate_synthetic_data(n=100):
    data = []
    for _ in range(n):
        # Genera cada variable siguiendo las instrucciones dadas
        # Crea un objeto PlayerMatchData con estos valores
        # Añádelo a la lista de datos
    return data

🧪 Paso 3: Crear y entrenar el modelo
Crea una clase VictoryPredictor que entrene un modelo de regresión logística con los datos sintéticos. Esta clase debe tener:
Un método train(data) para entrenar el modelo.
Un método predict(player: PlayerMatchData) que devuelva 1 si predice victoria, 0 si derrota.

📌 Ejemplo de uso
# Crear datos de entrenamiento
training_data = generate_synthetic_data(150)
# Entrenar modelo
predictor = VictoryPredictor()
predictor.train(training_data)
# Crear jugador de prueba
test_player = PlayerMatchData(8, 2, 3, 2400, 800, 120, 90, None)
# Predecir si ganará
prediction = predictor.predict(test_player)
print(f"¿El jugador ganará? {'Sí' if prediction == 1 else 'No'}")
Salida esperada
¿El jugador ganará? Sí
'''
class PlayerMatchData:
    def __init__ (self, kills, deaths, assists, damage_dealt, damage_received, healing_done, objective_time, won=None):
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.damage_dealt = damage_dealt
        self.damage_received = damage_received
        self.healing_done = healing_done
        self.objective_time = objective_time
        self.won = won
    def to_dict(self):
        data_dict = {
            'kills': self.kills,
            'deaths': self.deaths,
            'assists': self.assists,
            'damage_dealt': self.damage_dealt,
            'damage_received': self.damage_received,
            'healing_done': self.healing_done,
            'objective_time': self.objective_time
        }
        return data_dict

def generate_synthetic_data(n=100):
    data = []
    for _ in range(n):
        kills = np.random.poisson(5)
        deaths = np.random.poisson(3)
        assists = np.random.poisson(2)
        damage_dealt = kills * 300 + np.random.normal(0, 100)
        damage_received = deaths * 400 + np.random.normal(0, 100)
        healing_done = np.random.randint(0, 301)
        objective_time = np.random.randint(0, 121)
        won = 1 if damage_dealt > damage_received and kills > deaths else 0
        