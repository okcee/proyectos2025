import pandas as pd
import numpy as np
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







''' Ejercicio de codificación 15

'''