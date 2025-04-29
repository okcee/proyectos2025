import pandas as pd
from typing import List

from sklearn.linear_model import LinearRegression

''' Ejercicio de codificación 13
Regresión Lineal con Datos de Ventas
Supongamos que tienes un conjunto de datos que contiene información sobre las ventas de una tienda y la cantidad de dinero que se gastó en publicidad en diferentes medios (por ejemplo, televisión, radio y periódico).
Tu tarea es desarrollar una función llamada regresion_ventas que tome estos datos como entrada y ajuste un modelo de regresión lineal para predecir las futuras ventas en función de la inversión en publicidad.
def regresion_ventas(datos):
# Ejemplo de uso con datos reales
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8],
    'Periodico': [69.2, 45.1, 69.3, 58.5, 58.4],
    'Ventas': [22.1, 10.4, 9.3, 18.5, 12.9]
}
df = pd.DataFrame(data)
modelo_regresion = regresion_ventas(df)
# Estimaciones de ventas para nuevos datos de inversión en publicidad
nuevos_datos = pd.DataFrame({'TV': [200, 60, 30], 'Radio': [40, 20, 10], 'Periodico': [50, 10, 5]})
estimaciones_ventas = modelo_regresion.predict(nuevos_datos)
print("Estimaciones de Ventas:")
print(estimaciones_ventas)
Resultado:
Estimaciones de Ventas:
[21.54261464  8.48121675  4.16961329]
'''
def regresion_ventas(datos: pd.DataFrame) -> LinearRegression:
    # 1. Definir las columnas de características (X) y la columna objetivo (Y)
    features = ['TV', 'Radio', 'Periodico']
    target = 'Ventas'
    # 2. Seleccionar X e Y del DataFrame de entrada 'datos'
    X = datos[features]
    Y = datos[target]

    # 3. Crear una instancia del modelo de Regresión Lineal
    modelo = LinearRegression()

    # 4. Entrenar (ajustar) el modelo con los datos proporcionados (X, Y)
    modelo.fit(X, Y)

    # 5. Devolver el modelo entrenado
    return modelo

# --- Ejemplo de uso (fuera de la función) ---
# Datos de ejemplo proporcionados en el enunciado
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8],
    'Periodico': [69.2, 45.1, 69.3, 58.5, 58.4],
    'Ventas': [22.1, 10.4, 9.3, 18.5, 12.9]
}
df_entrada = pd.DataFrame(data) # Usamos un nombre diferente para evitar confusión con el df interno erróneo

# Llamar a la función para obtener el modelo entrenado
# Le pasamos el DataFrame con los datos de ejemplo
modelo_entrenado = regresion_ventas(df_entrada)

# Ahora usamos el modelo devuelto por la función para hacer predicciones
nuevos_datos = pd.DataFrame({'TV': [200, 60, 30], 'Radio': [40, 20, 10], 'Periodico': [50, 10, 5]})
estimaciones_ventas = modelo_entrenado.predict(nuevos_datos)

print("Modelo Entrenado:", modelo_entrenado) # Muestra el objeto del modelo
print("\nEstimaciones de Ventas para nuevos datos:")
print(estimaciones_ventas)

# --------------------------------------- #
''' Ejercicio de codificación 14
Predecir el rendimiento de un jugador
📝 Enunciado del ejercicio
Imagina que formas parte del equipo de desarrollo de un videojuego multijugador competitivo. El equipo de analítica necesita predecir cuántas victorias podría lograr un nuevo jugador, basándose únicamente en su estilo de juego.
Como científico de datos, tu misión es crear un modelo de regresión lineal que pueda predecir las victorias de un jugador en función de su rendimiento medio en partidas anteriores.
Para organizar bien tu solución y facilitar su reutilización en el futuro, deberás construirla utilizando tres clases bien definidas.
👨‍💻 Lo que debes hacer
1. Crea la clase Player
Esta clase representa a un jugador. Debe contener:
name: nombre del jugador
avg_session_time: duración promedio de sus sesiones de juego (en minutos)
avg_actions_per_min: acciones por minuto que realiza
avg_kills_per_session: número promedio de eliminaciones por sesión
victories: número de victorias (opcional, ya que puede usarse para predicción)
Debe incluir un método to_features(self) que devuelva una lista con los valores de entrada para el modelo.
2. Crea la clase PlayerDataset
Esta clase representa una colección de jugadores. Debe tener:
Un constructor que reciba una lista de objetos Player
Un método get_feature_matrix() que devuelva una lista de listas con los valores de entrada (X)
Un método get_target_vector() que devuelva una lista con los valores objetivo (y, las victorias)
3. Crea la clase VictoryPredictor
Encargada de entrenar y usar el modelo de regresión. Debe contener:
Un atributo con el modelo (LinearRegression)
Un método train(dataset: PlayerDataset) para entrenar el modelo con los datos del dataset
Un método predict(player: Player) que devuelva el número de victorias predichas para ese jugador
🧪 Ejemplo de uso
players = [
    Player("Alice", 40, 50, 6, 20),
    Player("Bob", 30, 35, 4, 10),
    Player("Charlie", 50, 60, 7, 25),
    Player("Diana", 20, 25, 2, 5),
    Player("Eve", 60, 70, 8, 30)
]
dataset = PlayerDataset(players)
predictor = VictoryPredictor()
predictor.train(dataset)
test_player = Player("TestPlayer", 45, 55, 5)
predicted = predictor.predict(test_player)
print(f"Victorias predichas para {test_player.name}: {predicted:.2f}")
🧪 Salida esperada
Victorias predichas para TestPlayer: 22.50
'''
class Player:
    def __init__ (self, name, avg_session_time, avg_actions_per_min, avg_kills_per_session, victories=None): # Datos de entrada, Victories=True porque no es obligatorio conocerlo como dato de entrada
        self.name = name
        self.avg_session_time = avg_session_time
        self.avg_actions_per_min = avg_actions_per_min
        self.avg_kills_per_session = avg_kills_per_session
        self.victories = victories
    
    def to_features(self): # Devuelve los datos de los jugadores que se van a usar en la predicción de victorias
        return [self.avg_session_time, self.avg_actions_per_min, self.avg_kills_per_session]

class PlayerDataset:
    def __init__ (self, players_list):
        self.players_list = players_list
    def get_feature_matrix(self):
        return [player.to_features() for player in self.players_list] # Devuelve una lista[], dónde itera cada objeto "player" dentro de "self.players_list" y, llama al método "to_features()" para obtener las características del mismo y agregar a la lista los valores de cada jugador a lista definidas en el método.
    def get_target_vector(self):
        return [player.victories for player in self.players_list] # Devuelve una lista[], dónde itera cada objeto "player" dentro de "self.players_list" y, llama al atributo "victories" para obtener las características del mismo y agregar a la lista los valores de cada jugador a lista definidas en el método.

class VictoryPredictor:
    def __init__ (self):
        self.model = LinearRegression()
    def train(self, dataset: PlayerDataset):
        X = dataset.get_feature_matrix()
        Y = dataset.get_target_vector()
        self.model.fit(X, Y) # Entrenar con todos los datos X, Y
        # El método train modifica el estado interno (entrena self.model), no necesita devolver nada.
    def predict(self, player: Player):
        caracteristicas_jugador = player.to_features()
        datos_para_predecir = [caracteristicas_jugador]
        predicciones = self.model.predict(datos_para_predecir) # Para sacar el valor objetivo de cada una de ellas
        valor_predicho = predicciones[0]
        return valor_predicho

players = [
    Player("Alice", 40, 50, 6, 20),
    Player("Bob", 30, 35, 4, 10),
    Player("Charlie", 50, 60, 7, 25),
    Player("Diana", 20, 25, 2, 5),
    Player("Eve", 60, 70, 8, 30)
]

dataset = PlayerDataset(players)
predictor = VictoryPredictor()
predictor.train(dataset)

test_player = Player("TestPlayer", 45, 55, 5)
predicted = predictor.predict(test_player)
print(f"Victorias predichas para {test_player.name}: {predicted:.2f}")

# --------------------------------------- #
''' Ejercicio de codificación 15
Predecir ingresos de una aplicación
📘 Enunciado del ejercicio:
Eres parte de un equipo de analistas de datos en una empresa tecnológica que desarrolla aplicaciones móviles. Te han proporcionado un pequeño conjunto de datos con información sobre diferentes apps que ya están publicadas, y tu tarea es crear un modelo de regresión lineal para predecir los ingresos estimados de una nueva app.
📊 Datos disponibles por app:
app_name: Nombre de la app
downloads: Número de descargas (en miles)
rating: Valoración media de los usuarios (de 1 a 5)
size_mb: Tamaño de la app (en MB)
reviews: Número de valoraciones escritas
revenue: Ingresos generados (en miles de dólares) → variable a predecir
📌 Tareas que debes realizar:
Crea una clase App que represente cada app con sus atributos.
Crea una clase RevenuePredictor que:
Reciba una lista de objetos App.
Extraiga las características relevantes para entrenar un modelo.
Entrene un modelo de regresión lineal para predecir los ingresos (revenue).
Permita predecir los ingresos de una nueva app con datos similares.
Entrena el modelo con los datos proporcionados (puedes usar una lista de ejemplo en el código).
Prueba el modelo prediciendo los ingresos estimados de una nueva app ficticia.
🧪 Ejemplo de uso
# Datos simulados de entrenamiento
training_apps = [
    App("TaskPro", 200, 4.2, 45.0, 1800, 120.0),
    App("MindSpark", 150, 4.5, 60.0, 2100, 135.0),
    App("WorkFlow", 300, 4.1, 55.0, 2500, 160.0),
    App("ZenTime", 120, 4.8, 40.0, 1700, 140.0),
    App("FocusApp", 180, 4.3, 52.0, 1900, 130.0),
    App("BoostApp", 220, 4.0, 48.0, 2300, 145.0),
]
# Creamos y entrenamos el predictor
predictor = RevenuePredictor()
predictor.fit(training_apps)
# Nueva app para predecir
new_app = App("FocusMaster", 250, 4.5, 50.0, 3000)
predicted_revenue = predictor.predict(new_app)
print(f"Ingresos estimados para {new_app.name}: ${predicted_revenue:.2f}K")
Salida esperada
Ingresos estimados para FocusMaster: $207.59K
'''

# 1. Crea una clase App que represente cada app con sus atributos
class App:
    def __init__ (self, app_name, download, rating, size_mb, reviews, revenue=None):
        self.app_name= app_name
        self.download = download
        self.rating = rating
        self.size_mb = size_mb
        self.reviews = reviews
        self.revenue = revenue
# 2. Crea una clase RevenuePredictor que:
class RevenuePredictor:
    # 2.1. Reciba una lista de objetos App.
    def __init__ (self): # Inicia el modelo de predicción
        self.model = LinearRegression()
        self.feature_names = ['download', 'rating', 'size_mb', 'reviews']
    def fit(self, training_apps: List[App]): # El método fit recibe la lista de apps para entrenar
        # 2.2. Extraiga las características relevantes para entrenar un modelo.
        # Extraer características (X)
        X_train = []
        for app in training_apps:
            # Seleccionamos los atributos numéricos relevantes para la predicción
            features = [
                app.download,
                app.rating,
                app.size_mb,
                app.reviews
            ]
            X_train.append(features)
        # Extraer objetivo (Y)
        Y_train = [app.revenue for app in training_apps] # Creamos una lista simple con los ingresos de cada app
        # 2.3. Entrene un modelo de regresión lineal para predecir los ingresos (revenue)
        # self.model ya fue inicializado en __init__, ahora entrenamos el modelo
        self.model.fit(X_train, Y_train) # El método fit modifica el estado interno (entrena self.model), no necesita devolver nada explícitamente.
    def predict(self, app_to_predict: App):
        # 2.4. Permita predecir los ingresos de una nueva app con datos similares.
        # Extraer las características de la nueva app en el mismo orden
        features = [
            app_to_predict.download,
            app_to_predict.rating,
            app_to_predict.size_mb,
            app_to_predict.reviews
        ]
        # Scikit-learn espera una entrada 2D (matriz), incluso para una sola predicción
        X_new = [features]
        predicted_revenue = self.model.predict(X_new) # Realizar la predicción
        return predicted_revenue[0]

# 3. Entrena el modelo con los datos proporcionados (puedes usar una lista de ejemplo en el código)
# Datos simulados de entrenamiento
training_apps = [
    App("TaskPro", 200, 4.2, 45.0, 1800, 120.0),
    App("MindSpark", 150, 4.5, 60.0, 2100, 135.0),
    App("WorkFlow", 300, 4.1, 55.0, 2500, 160.0),
    App("ZenTime", 120, 4.8, 40.0, 1700, 140.0),
    App("FocusApp", 180, 4.3, 52.0, 1900, 130.0),
    App("BoostApp", 220, 4.0, 48.0, 2300, 145.0),
]

# Creamos y entrenamos el predictor
predictor = RevenuePredictor()
predictor.fit(training_apps) # Pasamos la lista de apps aquí

# 4. Prueba el modelo prediciendo los ingresos estimados de una nueva app ficticia.
# Nueva app para predecir (sin revenue)
new_app = App("FocusMaster", 250, 4.5, 50.0, 3000) # No necesita revenue
predicted_revenue = predictor.predict(new_app)

print(f"Ingresos estimados para {new_app.app_name}: ${predicted_revenue:.2f}K")