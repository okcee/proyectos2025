''' Ejercicio de codificación 19 - Recomendador de Personajes
🎮 "Recomendador de Personajes: ¿Qué tipo de personaje deberías elegir?"

📘 Enunciado
En este ejercicio trabajarás como desarrollador de sistemas inteligentes para un nuevo videojuego tipo RPG online. El juego permite a los jugadores crear personajes y elegir entre distintos roles o clases (por ejemplo: guerrero, mago, arquero, curandero…).
Tu tarea es construir un modelo de recomendación que, dado un perfil de jugador (nivel, estilo de combate, número de partidas jugadas, etc.), recomiende qué tipo de personaje debería usar, basándose en datos históricos de otros jugadores similares.

🧩 Requerimientos
Crea una clase Player que represente a un jugador con los siguientes atributos:
name: nombre del jugador.
level: nivel del jugador (1 a 100).
aggressiveness: valor entre 0 y 1 que representa su estilo ofensivo.
cooperation: valor entre 0 y 1 que representa cuánto coopera con el equipo.
exploration: valor entre 0 y 1 que representa cuánto le gusta explorar el mapa.
preferred_class: clase de personaje que suele elegir (solo en los datos de entrenamiento).
Implementa un método .to_features() en la clase para convertir al jugador en una lista de características numéricas (sin la clase preferida).
Crea una clase PlayerDataset que contenga una lista de jugadores y proporcione:
get_X() → lista de listas de características.
get_y() → lista de clases preferidas.
Crea una clase ClassRecommender que use KNN para:
Entrenar el modelo a partir de un PlayerDataset.
Predecir la mejor clase para un nuevo jugador (predict(player)).
Obtener los k jugadores más parecidos (get_nearest_neighbors(player)).
(Opcional) Permite probar diferentes valores de k y evaluar la precisión del modelo con cross_val_score.

🧪 Ejemplo de uso
# Datos de entrenamiento
players = [
    Player("Alice", 20, 0.8, 0.2, 0.1, "Warrior"),
    Player("Bob", 45, 0.4, 0.8, 0.2, "Healer"),
    Player("Cleo", 33, 0.6, 0.4, 0.6, "Archer"),
    Player("Dan", 60, 0.3, 0.9, 0.3, "Healer"),
    Player("Eli", 50, 0.7, 0.2, 0.9, "Mage"),
    Player("Fay", 25, 0.9, 0.1, 0.2, "Warrior"),
]
# Nuevo jugador
new_player = Player("TestPlayer", 40, 0.6, 0.3, 0.8)
# Entrenamiento y predicción
dataset = PlayerDataset(players)
recommender = ClassRecommender(n_neighbors=3)
recommender.train(dataset)
# Resultado
recommended_class = recommender.predict(new_player)
neighbors_indices = recommender.get_nearest_neighbors(new_player)
print(f"Clase recomendada para {new_player.name}: {recommended_class}")
print("Jugadores similares:")
for i in neighbors_indices:
    print(f"- {players[i].name} ({players[i].preferred_class})")

🧪 Salida esperada
Clase recomendada para TestPlayer: Archer
Jugadores similares:
- Bob (Healer)
- Cleo (Archer)
- Eli (Mage)

Objetivo del aprendizaje: Practicar con el algoritmo de k vecinos más cercanos
'''

# --- Importaciones ---
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from typing import List, Optional # Para type hints
from collections import Counter # Importar Counter aquí

# --- Clase Player ---
class Player:
    """Representa a un jugador con sus atributos y clase preferida (opcional)."""
    def __init__(self, name: str, level: int, aggressiveness: float,
                 cooperation: float, exploration: float, preferred_class: Optional[str] = None):
        self.name = name
        self.level = level
        self.aggressiveness = aggressiveness
        self.cooperation = cooperation
        self.exploration = exploration
        self.preferred_class = preferred_class

    def to_features(self) -> List[float]:
        """Convierte los atributos del jugador en una lista de características numéricas."""
        return [
            float(self.level),
            self.aggressiveness,
            self.cooperation,
            self.exploration
        ]

    def __repr__(self) -> str:
        """Representación en string del objeto Player."""
        return (f"Player(name='{self.name}', level={self.level}, agg={self.aggressiveness}, "
                f"coop={self.cooperation}, exp={self.exploration}, "
                f"class='{self.preferred_class or 'N/A'}')")

# --- Clase PlayerDataset ---
class PlayerDataset:
    """Contiene una lista de jugadores y proporciona métodos para obtener X e y."""
    def __init__(self, players: List[Player]):
        if not players:
            raise ValueError("La lista de jugadores no puede estar vacía.")
        self.players = players

    def get_X(self) -> List[List[float]]:
        """Devuelve una lista de listas de características para todos los jugadores."""
        return [player.to_features() for player in self.players]

    def get_y(self) -> List[str]:
        """Devuelve una lista de las clases preferidas de todos los jugadores."""
        if any(player.preferred_class is None for player in self.players):
             raise ValueError("Todos los jugadores en el dataset de entrenamiento deben tener una 'preferred_class'.")
        return [player.preferred_class for player in self.players]

# --- Clase ClassRecommender ---
# --- Clase ClassRecommender ---
class ClassRecommender:
    """Recomienda clases de personajes usando K-Nearest Neighbors."""
    def __init__(self, n_neighbors: int = 3):
        if n_neighbors <= 0:
            raise ValueError("n_neighbors debe ser un entero positivo.")
        self.n_neighbors = n_neighbors
        # Inicializar knn aquí, pero se puede re-instanciar en train si k se ajusta
        self.knn = KNeighborsClassifier(n_neighbors=self.n_neighbors)
        self._is_fitted = False
        self._feature_names = ['level', 'aggressiveness', 'cooperation', 'exploration']

    def train(self, dataset: PlayerDataset):
        """Entrena el modelo KNN con los datos del PlayerDataset."""
        if not isinstance(dataset, PlayerDataset):
            raise TypeError("El argumento 'dataset' debe ser una instancia de PlayerDataset.")

        try:
            X = dataset.get_X()
            y = dataset.get_y()
        except ValueError as e:
             # Re-lanzar el error si get_y falla (jugador sin clase)
             raise ValueError(f"Error al obtener datos del dataset para entrenamiento: {e}")

        if not X:
             raise ValueError("No se pueden extraer características del dataset (lista X vacía).")

        # Ajustar k si es mayor que el número de muestras ANTES de entrenar
        effective_k = self.n_neighbors
        current_knn_k = self.knn.n_neighbors # Guardar k actual por si no cambia

        if effective_k > len(X):
            print(f"Advertencia: n_neighbors ({effective_k}) es mayor que el número de muestras de entrenamiento ({len(X)}). "
                  f"Ajustando n_neighbors a {len(X)}.")
            effective_k = len(X)
            # Solo re-instanciar si k realmente cambia
            if effective_k != current_knn_k:
                 self.knn = KNeighborsClassifier(n_neighbors=effective_k)
        # Asegurarse de que si k no se ajustó, el knn tenga el k original
        elif effective_k != current_knn_k:
             self.knn = KNeighborsClassifier(n_neighbors=effective_k)


        self.knn.fit(X, y)
        self._is_fitted = True
        # Usar self.knn.n_neighbors que refleja el valor real usado
        print(f"Recomendador entrenado con {len(X)} jugadores y k={self.knn.n_neighbors}.")


    def predict(self, player: Player) -> str: # Cambiado Optional[str] a str porque ahora lanza excepción
        """Predice la clase más adecuada para un nuevo jugador."""
        # --- CORRECCIÓN: Lanzar excepción si no está entrenado ---
        if not self._is_fitted:
            raise RuntimeError("El modelo debe ser entrenado ('train') antes de hacer predicciones.")
        # ------------------------------------------------------
        if not isinstance(player, Player):
            raise TypeError("El argumento 'player' debe ser una instancia de Player.")

        player_features = player.to_features()
        player_features_2d = [player_features]

        prediction = self.knn.predict(player_features_2d)
        return prediction[0]

    def get_nearest_neighbors(self, player: Player) -> np.ndarray: # Cambiado Optional[...] a np.ndarray
        """
        Encuentra los índices de los k jugadores más similares en el dataset de entrenamiento.
        """
        # --- CORRECCIÓN: Lanzar excepción si no está entrenado ---
        if not self._is_fitted:
            raise RuntimeError("El modelo debe ser entrenado ('train') antes de buscar vecinos.")
        # ------------------------------------------------------
        if not isinstance(player, Player):
            raise TypeError("El argumento 'player' debe ser una instancia de Player.")

        player_features = player.to_features()
        player_features_2d = [player_features]

        distances, indices = self.knn.kneighbors(player_features_2d)
        return indices[0]

    def evaluate_accuracy(self, dataset: PlayerDataset, cv: int = 3) -> float: # Cambiado Optional[float] a float
        """
        (Opcional) Evalúa la precisión del modelo usando validación cruzada.
        Args:
            dataset (PlayerDataset): El dataset (puede ser el mismo de entrenamiento o uno nuevo).
            cv (int): Número de folds para la validación cruzada.
        Returns:
            float: La precisión media de la validación cruzada.
        Raises:
            RuntimeError: Si el modelo no ha sido entrenado.
            TypeError: Si dataset no es PlayerDataset.
            ValueError: Si los datos no son adecuados para la validación cruzada solicitada.
        """
        # --- CORRECCIÓN: Lanzar excepción si no está entrenado ---
        if not self._is_fitted:
            raise RuntimeError("El modelo debe ser entrenado ('train') antes de evaluar.")
        # ------------------------------------------------------
        if not isinstance(dataset, PlayerDataset):
            raise TypeError("El argumento 'dataset' debe ser una instancia de PlayerDataset.")

        # Obtener los datos PRIMERO
        try:
            X = dataset.get_X()
            y = dataset.get_y()
        except ValueError as e:
             raise ValueError(f"Error al obtener datos del dataset para evaluación: {e}")

        # Validar si hay suficientes datos totales
        if not X or len(X) < 2:
             # Lanzar ValueError si no hay suficientes datos para CV
             raise ValueError(f"No hay suficientes muestras ({len(X)}) para realizar validación cruzada (se requieren al menos 2).")

        # Validar y ajustar 'cv' basado en el total de muestras
        effective_cv = cv
        if len(X) < effective_cv:
            print(f"Advertencia: No hay suficientes muestras ({len(X)}) para cv={effective_cv}. Reduciendo cv a {len(X)}.")
            effective_cv = len(X)

        if effective_cv < 2:
             # Lanzar ValueError si cv efectivo es menor que 2
             raise ValueError(f"El número de splits para validación cruzada debe ser al menos 2, pero se obtuvo {effective_cv}.")

        # Validar 'cv' para estratificación
        min_class_count = min(Counter(y).values())

        if effective_cv > min_class_count:
            # Lanzar ValueError si cv es mayor que la clase mínima (error estándar de CV estratificada)
            raise ValueError(f"El número de splits (cv={effective_cv}) no puede ser mayor que el número de miembros en cada clase (mínimo: {min_class_count}).")

        # Realizar la validación cruzada
        try:
            scores = cross_val_score(self.knn, X, y, cv=effective_cv, scoring='accuracy')
            print(f"Precisión en validación cruzada ({effective_cv} folds): {scores}")
            return np.mean(scores)
        except ValueError as e:
            # Re-lanzar el error si cross_val_score falla por otras razones
            raise ValueError(f"Error durante cross_val_score: {e}")

# --- Resto del código (Clase Player, PlayerDataset, Ejemplo de uso) sin cambios ---
# ... (pegar el resto del código aquí) ...

# --- Ejemplo de uso (modificado para manejar excepciones si ocurren) ---
print("--- Iniciando Ejemplo de Recomendador de Personajes ---")

# Datos de entrenamiento
players = [
    Player("Alice", 20, 0.8, 0.2, 0.1, "Warrior"),
    Player("Bob", 45, 0.4, 0.8, 0.2, "Healer"),
    Player("Cleo", 33, 0.6, 0.4, 0.6, "Archer"),
    Player("Dan", 60, 0.3, 0.9, 0.3, "Healer"),
    Player("Eli", 50, 0.7, 0.2, 0.9, "Mage"),
    Player("Fay", 25, 0.9, 0.1, 0.2, "Warrior"),
]
print(f"\nJugadores de entrenamiento ({len(players)}):")

new_player = Player("TestPlayer", 40, 0.6, 0.3, 0.8)
print(f"\nNuevo jugador: {new_player}")

try:
    dataset = PlayerDataset(players)
    recommender = ClassRecommender(n_neighbors=3)

    # --- Prueba de excepción (descomentar para probar) ---
    # try:
    #     recommender.predict(new_player)
    # except RuntimeError as e:
    #     print(f"\nPrueba de excepción (predict antes de train): OK - {e}")
    # ----------------------------------------------------

    recommender.train(dataset)

    recommended_class = recommender.predict(new_player)
    print(f"\nClase recomendada para {new_player.name}: {recommended_class}")

    neighbors_indices = recommender.get_nearest_neighbors(new_player)
    if neighbors_indices is not None: # Aunque ahora no debería ser None si no hay excepción
        print("\nJugadores similares (vecinos más cercanos):")
        for i in neighbors_indices:
            neighbor_player = dataset.players[i]
            print(f"- {neighbor_player.name} (Nivel: {neighbor_player.level}, Clase: {neighbor_player.preferred_class})")

    print("\n--- Evaluación Opcional ---")
    # Esta parte ahora lanzará ValueError con los datos de ejemplo
    try:
        mean_accuracy = recommender.evaluate_accuracy(dataset, cv=3)
        print(f"Precisión media estimada (cross-validation): {mean_accuracy:.4f}")
    except ValueError as e:
        print(f"No se pudo calcular la precisión media por validación cruzada: {e}") # Imprimir el error esperado

except ValueError as e:
    print(f"\nError durante la configuración o entrenamiento: {e}")
except TypeError as e:
    print(f"\nError de tipo durante la configuración o entrenamiento: {e}")
except RuntimeError as e:
    print(f"\nError de ejecución (probablemente modelo no entrenado): {e}")


print("\n--- Fin del Ejemplo ---")
