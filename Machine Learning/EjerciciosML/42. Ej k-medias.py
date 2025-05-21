''' Agrupar viajeros según sus preferencias - Practicar con numpy para crear datos sintéticos de ejemplo y con el algoritmo de k-medias para agrupar viajeros según sus preferencias de viaje.

Imagina que trabajas en una agencia de viajes internacional que recibe cientos de perfiles de viajeros. Cada viajero indica cuánto le gustan diferentes tipos de destinos: playa, montaña, ciudad y campo.

Tu misión es:
🔹 Crear una clase Traveler para representar un viajero, con atributos como:
beach
mountain
city
countryside
🔹 Crear una clase TravelerGenerator que pueda generar automáticamente viajeros con gustos aleatorios (usando numpy).
🔹 Crear una clase TravelerClusterer que use K-Means Clustering (sklearn) para agrupar a los viajeros en 3 grupos principales según sus preferencias.
🔹 Permitir probar con un viajero nuevo: dado un viajero personalizado, deberás predecir a qué grupo pertenecería.
🔹 Crear una clase TravelerClusteringExample que integre todo:
Genere los datos de entrenamiento.
Entrene el modelo de agrupamiento.
Cree un viajero nuevo.
Prediga a qué grupo pertenece ese viajero y muestre los resultados.

🛠 Requisitos mínimos:
Traveler: clase que almacena las preferencias.
TravelerGenerator: clase que genera viajeros de manera aleatoria.
TravelerClusterer: clase que entrena el modelo K-Means y predice el grupo de nuevos viajeros.
TravelerClusteringExample: clase que coordina todo el flujo y ejecuta el ejemplo completo.

🎯 Pistas para completar la misión:
Usa numpy.random.uniform(0, 10) para generar los gustos aleatorios.
Usa sklearn.cluster.KMeans(n_clusters=3) para entrenar el modelo.
Representa cada viajero como un vector de 4 números (uno por tipo de preferencia).
Al final del ejemplo, imprime en pantalla el grupo asignado al nuevo viajero.

✅ Ejemplo de uso
# Ejecutar ejemplo
example = TravelerClusteringExample()
example.run()

Salida esperada
🏝️🏔️🏙️🌄 Cluster Centers (Preferencias promedio):
Cluster 0: Playa=4.79, Montaña=5.16, Ciudad=7.79, Campo=7.82
Cluster 1: Playa=5.11, Montaña=5.54, Ciudad=6.60, Campo=1.66
Cluster 2: Playa=4.69, Montaña=5.23, Ciudad=1.46, Campo=6.16
Interpretación aproximada:
- Cluster con alta Playa y Ciudad: Viajero urbano y costero.
- Cluster con alta Montaña y Campo: Amante de la naturaleza.
- Cluster equilibrado: Viajero versátil o aventurero.
🔍 Nuevo viajero con preferencias:
Playa: 9, Montaña: 2, Ciudad: 8, Campo: 1
📌 El nuevo viajero pertenece al grupo 1.
'''

import numpy as np
from sklearn.cluster import KMeans

# 1. Clase Traveler
class Traveler:
    def __init__(self, beach, mountain, city, countryside):
        self.beach = beach
        self.mountain = mountain
        self.city = city
        self.countryside = countryside

    def to_vector(self):
        return [self.beach, self.mountain, self.city, self.countryside]

# 2. Clase TravelerGenerator
class TravelerGenerator:
    def __init__(self, num_travelers=100):
        self.num_travelers = num_travelers

    def generate(self):
        travelers = []
        for _ in range(self.num_travelers):
            beach = np.round(np.random.uniform(0, 10), 2)
            mountain = np.round(np.random.uniform(0, 10), 2)
            city = np.round(np.random.uniform(0, 10), 2)
            countryside = np.round(np.random.uniform(0, 10), 2)

            traveler = Traveler(beach, mountain, city, countryside)
            travelers.append(traveler)
        return travelers

# 3. Clase TravelerClusterer
class TravelerClusterer:
    def __init__(self, n_clusters=3):
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.cluster_centers = None

    def fit(self, travelers):
        X = [t.to_vector() for t in travelers]
        self.model.fit(X)
        self.cluster_centers = self.model.cluster_centers_

    def predict(self, traveler):
        return self.model.predict([traveler.to_vector()])[0]

    def get_cluster_centers(self):
        return self.cluster_centers

# 4. Clase TravelerClusteringExample
class TravelerClusteringExample:
    def run(self):
        # 1. Generar datos
        generator = TravelerGenerator(100)
        travelers = generator.generate()

        # 2. Entrenar el modelo
        clusterer = TravelerClusterer(n_clusters=3)
        clusterer.fit(travelers)

        # 3. Obtener y mostrar los centros de los clústeres
        centers = clusterer.get_cluster_centers()
        print("🏝️🏔️🏙️🌄 Centros de los Clústeres (Preferencias promedio):")
        for i, center in enumerate(centers):
            print(f"Cluster {i}: Playa={center[0]:.2f}, Montaña={center[1]:.2f}, Ciudad={center[2]:.2f}, Campo={center[3]:.2f}")

        # 4. Crear un viajero nuevo
        new_traveler = Traveler(beach=8.5, mountain=2.0, city=9.0, countryside=1.5)

        # 5. Predecir su grupo
        group = clusterer.predict(new_traveler)

        # 6. Mostrar resultados
        print("🧳 Nuevo viajero:")
        print(f"Beach: {new_traveler.beach}, Mountain: {new_traveler.mountain}, City: {new_traveler.city}, Countryside: {new_traveler.countryside}")
        print(f"📍 Pertenece al grupo: {group}")

# 5. Ejecutar el ejemplo
if __name__ == "__main__":
    example = TravelerClusteringExample()
    example.run()
