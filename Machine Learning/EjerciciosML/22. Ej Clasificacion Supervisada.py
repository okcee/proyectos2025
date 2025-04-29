''' Ejercicio de codificación 22 - Recomendador de canciones inteligente

🧠 Contexto
Estás desarrollando un sistema para una plataforma musical que quiere ofrecer recomendaciones automáticas basadas en características cuantitativas de las canciones, como su energía o duración.
Utilizarás el algoritmo K-Nearest Neighbors (KNN) de la biblioteca scikit-learn para encontrar las canciones más similares a una canción objetivo.

🎯 Objetivo del ejercicio
Implementar un sistema de recomendación de canciones en Python, usando el modelo de K Vecinos Más Cercanos de scikit-learn.
El sistema debe permitir recomendar canciones similares a partir de características musicales numéricas.

📌 Requisitos
🧩 1. Clase Song
Crea una clase Song que represente una canción, con los siguientes atributos:
title (str): título de la canción.
artist (str): artista o grupo musical.
energy (float): energía de la canción (0.4 a 1.0).
danceability (float): cuán bailable es la canción (0.4 a 1.0).
duration (int): duración en segundos (180 a 300).
popularity (int): nivel de popularidad (50 a 100).
La clase debe incluir:
Un método to_vector() que devuelva una lista con los valores [energy, danceability, duration, popularity].
Un método __str__() que permita imprimir la canción en formato "Song Title by Artist".
🤖 2. Clase SongRecommender
Crea una clase SongRecommender que use el algoritmo de KNN de scikit-learn:
El constructor debe aceptar un parámetro k (número de vecinos a considerar).
El método fit(song_list) debe:
Convertir la lista de canciones en una matriz de características numéricas.
Ajustar el modelo NearestNeighbors con estas características.
El método recommend(target_song) debe:
Obtener los k vecinos más cercanos a la canción objetivo.
Devolver la lista de canciones recomendadas (sin incluir la propia canción objetivo si aparece).
🔁 3. Clase SongGenerator
Crea una clase SongGenerator con:
Un parámetro num_songs (por defecto 30).
Un método generate() que genere canciones aleatorias con numpy, usando nombres como "Song1", "Song2", etc., y artistas "Artist1", "Artist2", etc.
🧪 4. Clase SongRecommendationExample
Crea una clase de ejemplo que:
Genere una lista de canciones con SongGenerator.
Defina una canción personalizada como objetivo (target_song).
Cree una instancia de SongRecommender, la entrene con las canciones y obtenga recomendaciones.
Imprima por pantalla las canciones recomendadas.
Ejemplo de salida:
example = SongRecommendationExample()
example.run()
Salida esperada

🎵 Recomendaciones para 'Mi Canción':
 - Song29 by Artist4
 - Song11 by Artist1
 - Song25 by Artist5

💡 Recomendaciones para completar el ejercicio
Usa numpy para generar valores aleatorios.
Recuerda importar NearestNeighbors desde sklearn.neighbors.
Asegúrate de convertir los objetos Song a vectores antes de ajustar o predecir con el modelo.
No incluyas la canción objetivo entre las recomendaciones (verifica si es necesario).

Objetivo del aprendizaje: Practicar con numpy para la generación de datos sintéticos y con el algoritmo de k vecinos más cercanos para realizar predicciones de canciones.
'''

import numpy as np
from sklearn.neighbors import NearestNeighbors

# 🧩 1. Clase Song: Crea una clase Song que represente una canción
class Song:
    """Representa una canción con sus características musicales."""
    def __init__ (self, title, artist, energy, danceability, duration, popularity):
        # Atributos
        self.title = title
        self.artist = artist
        self.energy = energy
        self.danceability = danceability
        self.duration = duration
        self.popularity = popularity
    # Un método to_vector() que devuelva una lista con los valores [energy, danceability, duration, popularity]
    def to_vector(self):
        """Devuelve las características numéricas como una lista."""
        return [self.energy, self.danceability, self.duration, self.popularity]
    # Un método __str__() que permita imprimir la canción en formato "Song Title by Artist"
    def __str__(self):
        """Representación en formato 'Song Title by Artist'."""
        return f"Song {self.title} by {self.artist}"

# 🤖 2. Clase SongRecommender: Crea una clase SongRecommender que use el algoritmo de KNN de scikit-learn
class SongRecommender:
    """Recomienda canciones usando K-Nearest Neighbors."""
    def __init__(self, k): # El constructor debe aceptar un parámetro k
        """Inicializa el recomendador con k vecinos."""
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k debe ser un entero positivo.")
        self.k = k
        self.model = NearestNeighbors(n_neighbors=self.k, algorithm='auto') # Inicializa el modelo NearestNeighbors aquí, especificando el número de vecinos (k) y el algoritmo a usar (por defecto 'auto' que suele ser eficiente, si no se definiría con el parámetro opcional 'algorithm')
        '''La clase NearestNeighbors tiene varios parámetros que puedes especificar, como n_neighbors (el número de vecinos k), metric (la forma de medir la distancia), y algorithm (el método interno para encontrar los vecinos).'''
        self.song_list = [] # Lista para guardar las canciones originales
        self.song_vectors = None # Array NumPy para guardar los vectores de características de la matriz NumPy
    def fit(self, song_list): # Convertir la lista de canciones en una matriz de características numéricas. Ajustar el modelo NearestNeighbors con estas características.
        """Entrena el modelo KNN con una lista de canciones."""
        if not song_list:
            print("Advertencia: La lista de canciones para entrenar está vacía.") # Validación
            self.song_list = []
            self.song_vectors = np.empty((0, 4)) # Array vacío con 4 columnas
            return

        # Convierte la lista de objetos Song a una matriz NumPy
        # Se usa list comprehension y np.array (Cumple recomendación)
        self.song_vectors = np.array([song.to_vector() for song in song_list])
        # Ajusta el modelo NearestNeighbors con los vectores
        self.model.fit(self.song_vectors)

        self.song_list = song_list
        # Convierte cada objeto Song en su vector de características usando to_vector() y crea un array NumPy con todos estos vectores. Cada fila es una canción
        self.song_vectors = np.array([song.to_vector() for song in song_list]) # np.array(...) Esta es la función de NumPy que toma la lista de listas generada por la comprensión y la convierte en un array de NumPy
        # Entrena (ajusta) el modelo KNN con los vectores de características. El modelo aprende la estructura espacial de los datos para poder encontrar vecinos rápidamente.
        self.model.fit(self.song_vectors)
    def recommend(self, target_song):
        """
        Encuentra y devuelve las k canciones más similares a target_song.
        Excluye la propia target_song de las recomendaciones.
        Args:
            target_song (Song): La canción para la cual buscar recomendaciones.
        Returns:
            list[Song]: Una lista de las k canciones recomendadas (excluyendo target_song si está presente).
            Devuelve menos de k si no hay suficientes canciones únicas.
        """
        if not self.song_list:
            print("El modelo no ha sido entrenado o la lista de canciones está vacía. No se pueden generar recomendaciones.")
            return []
        # 1. Preparar el vector de la canción objetivo: convierte la canción objetivo a vector NumPy 2D (1 fila):
        #    - Llama a target_song.to_vector() para obtener sus características numéricas.
        #    - np.array(...) convierte esa lista en un array NumPy.
        #    - .reshape(1, -1) lo transforma en un array 2D con una sola fila y
        #      tantas columnas como características tenga. Esto es necesario porque
        #      los métodos de scikit-learn esperan una matriz de muestras (aunque sea una sola).
        target_vector = np.array(target_song.to_vector()).reshape(1, -1)

        # 2. Encontrar los vecinos más cercanos:
        # Encuentra los k+1 vecinos más cercanos (incluyendo potencialmente a sí misma)
        # Pedimos k+1 por si la propia canción objetivo es el vecino más cercano (distancia 0)
        # Así aseguramos tener k recomendaciones *distintas* si es posible.
        num_neighbors_to_find = min(self.k + 1, len(self.song_list)) # No pedir más vecinos que canciones hay
        distances, indices = self.model.kneighbors(target_vector, n_neighbors=num_neighbors_to_find)
        # El método .kneighbors() devuelve dos cosas: indices: Las posiciones (índices) de las canciones más cercanas en la lista original y distances: Los valores numéricos de las distancias calculadas entre la target_song y cada una de esas canciones vecinas encontradas. Una distancia menor significa que la canción vecina es más similar a la canción objetivo, según las características usadas.

        # 3. Obtener las canciones recomendadas a partir de los índices:
        recommended_songs = []
        # Itera sobre los índices de los vecinos encontrados
        for i in indices[0]:
            neighbor_song = self.song_list[i]
            # Excluye la canción objetivo (comparación de identidad de objeto)
            # (Cumple recomendación)
            if neighbor_song is not target_song:
                recommended_songs.append(neighbor_song)
            # Si ya hemos encontrado k recomendaciones distintas, paramos
            if len(recommended_songs) == self.k:
                break
        return recommended_songs

# 🔁 3. Clase SongGenerator
class SongGenerator: # Crea una clase SongGenerato con un parámetro num_songs (por defecto 30).
    """Genera una lista de objetos Song aleatorios."""
    def __init__(self, num_songs=30):
        """Inicializa el generador con el número de canciones."""
        self.num_songs = num_songs
    def generate(self): # Un método generate() que genere canciones aleatorias con numpy
        """Genera y devuelve la lista de canciones aleatorias."""
        songs = []
        if self.num_songs <= 0:
            return songs
        
        for i in range(1, self.num_songs + 1):
            # Nombres y artistas genéricos como se pide
            title = f"Song{i}" # usando nombres como "Song1", "Song2"
            artist = f"Artist{i}" # artistas "Artist1", "Artist2" ## Si quisiesemos menos artistas que canciones: artist = f"Artist{np.random.randint(1, self.num_songs // 2 + 1)}"
            # Genera características aleatorias usando numpy (Cumple recomendación)
            energy = np.random.uniform(0.4, 1.0) # Atributos de las canciones...
            danceability = np.random.uniform(0.4, 1.0)
            duration = np.random.randint(180, 301)
            popularity = np.random.randint(50, 101)
            # Crea el objeto Song y lo añade a la lista de Python
            songs.append(Song(title, artist, energy, danceability, duration, popularity)) # Añade un objeto de la clase Song (que contiene los datos de una canción generada) a la lista vacía llamada songs, utilizando el método .append() propio de las listas de Python, que sirve para añadir un elemento al final de la lista existente
        return songs

# 🧪 4. Clase SongRecommendationExample
class SongRecommendationExample: # Clase de ejemplo
    """Clase de ejemplo para demostrar el sistema de recomendación."""
    def __init__(self, k_neighbors=5, num_generated_songs=30):
        # Genera la lista de canciones base
        self.song_generator = SongGenerator(num_songs=num_generated_songs)
        self.songs = self.song_generator.generate()
        # Define una canción objetivo personalizada (como en el ejemplo de salida)
        # Usamos valores dentro de los rangos esperados
        self.target_song = Song(title="Mi Canción", artist="Mi Artista",
                                energy=0.75, danceability=0.85,
                                duration=215, popularity=88)
        # IMPORTANTE: Añadir la canción objetivo a la lista total de canciones
        # para que el modelo la conozca si queremos poder excluirla correctamente
        # por identidad y para que las distancias se calculen respecto a todo el catálogo.
        self.songs.append(self.target_song)
        # Crea y entrena el recomendador
        self.recommender = SongRecommender(k=k_neighbors)
        self.recommender.fit(self.songs) # Entrena con la lista que incluye la target_song

    def run(self):
        """Ejecuta el proceso de recomendación e imprime los resultados."""
        print(f"🎵 Recomendaciones para '{self.target_song.title}':") # Ajustado para usar solo el título
        # Obtiene las recomendaciones para la canción objetivo
        recommended_songs = self.recommender.recommend(self.target_song)
        # Imprime las canciones recomendadas
        if recommended_songs:
            for song in recommended_songs:
                # Usa el método __str__ de Song para el formato "Title by Artist"
                print(f" - {song}")
        else:
            print("   No se encontraron recomendaciones.")

# --------------------------------------------------
# Bloque de ejecución principal
# --------------------------------------------------
if __name__ == "__main__":
    # Crea una instancia del ejemplo y la ejecuta
    example = SongRecommendationExample(k_neighbors=3, num_generated_songs=50) # k=3 para coincidir con el número de items en la salida de ejemplo
    example.run()

'''
El método .reshape() se utiliza comúnmente en la librería NumPy de Python para cambiar la forma (dimensiones) de un array sin cambiar sus datos.

La sintaxis básica es:
array_original.reshape(nueva_forma, order='C')

Aquí te desglosamos los elementos:
- array_original: Es el array de NumPy (o un objeto que se puede convertir en uno, como el .values de un DataFrame/Series de Pandas) al que quieres cambiar la forma.
- .reshape(): El nombre del método.
- nueva_forma: Este es el argumento principal y obligatorio. Especifica la nueva forma (dimensiones) que quieres que tenga el array. Puede ser:
    - Un entero: Para convertir el array en un array 1D (aplanarlo).
    - Una tupla de enteros: Donde cada entero representa el tamaño de una dimensión. Por ejemplo, (filas, columnas) para un array 2D, (profundidad, filas, columnas) para un array 3D, etc.
    - Uno de los elementos de la tupla de nueva_forma puede ser -1. Si usas -1, NumPy calculará automáticamente el tamaño de esa dimensión basándose en el tamaño total del array y los tamaños de las otras dimensiones que has especificado. Solo puede haber un -1 en la tupla. La condición es que el número total de elementos en la nueva_forma (calculando el -1) debe ser igual al número total de elementos en el array_original.
    - order: Este argumento es opcional y especifica el orden en que se leen los elementos del array original para colocarlos en el nuevo array.
        - 'C' (por defecto): Lee/escribe elementos usando el orden de indexación estilo C (orden por filas o "row-major").
        - 'F': Lee/escribe elementos usando el orden de indexación estilo Fortran (orden por columnas o "column-major").
        - 'A': Lee/escribe en orden Fortran si el array original está en Fortran-contiguous, de lo contrario usa orden C.
'''