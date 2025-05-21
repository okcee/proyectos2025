''' Agrupar perfiles de sueño - Practicar con numpy para generar datos, con el algoritmo de k-medias para agrupar perfiles de sueño, con pandas y matplotlib para graficar los resultados obtenidos.

🎯 Objetivo del ejercicio:
Analizar perfiles de sueño simulados de distintas personas para agruparlos según sus patrones de descanso utilizando el algoritmo de k-medias (K-Means).
El objetivo es encontrar tipos de durmientes (como los que duermen mucho, los que se despiertan frecuentemente, etc.) a partir de sus datos personales.

🧠 Contexto:
Un equipo de investigadores del sueño quiere estudiar cómo duermen diferentes personas durante varias noches.
Para ello, han registrado características clave como:
Duración del sueño (en horas)
Latencia: cuántos minutos tarda la persona en dormirse
Cantidad de despertares por noche
Variabilidad: cuánto varía la hora a la que se acuesta cada día
Tu tarea es agrupar estos perfiles en 3 tipos de durmientes usando K-Means, y visualizar los resultados de manera clara y útil.

📊 Datos simulados:
Los datos serán generados aleatoriamente con estas distribuciones:

🧱 Estructura sugerida del código:
Clases utilizadas:
SleepProfile
Representa un perfil individual de sueño, con atributos como duración del sueño, latencia, despertares y variabilidad.
Método to_vector() convierte estos atributos en un vector numérico para el algoritmo.
SleepDatasetGenerator
Genera n perfiles de sueño aleatorios con características estadísticas realistas.
Usa distribución normal y de Poisson para crear variedad en los datos.
SleepClusterer
Se encarga de escalar los datos y aplicar el algoritmo K-Means para agrupar los perfiles en k grupos.
Usa StandardScaler para normalizar.
Devuelve las etiquetas de grupo y los datos escalados.
SleepAnalysisExample
Es la clase que integra todo: genera los datos, entrena el modelo, agrupa y visualiza los resultados en un gráfico.
También imprime los centroides de cada grupo interpretados en la escala original.

📈 ¿Qué deberías mostrar al final?
Los centroides de los grupos, interpretando lo que caracteriza a cada uno.
Un gráfico de dispersión donde se vea la agrupación de perfiles por:
Eje X: Duración del sueño
Eje Y: Variabilidad de hora de dormir
Comentarios sobre posibles tipos de durmientes: ¿hay un grupo de "insomnes"? ¿otro de "buenos durmientes"?

🧪 Ejemplo de uso
example = SleepAnalysisExample()
example.run()

Salida esperada
📌 Centroides de los grupos:
Grupo 0: Duración=6.30h, Latencia=19.3min, Despertares=1.2, Variabilidad=39.6min
Grupo 1: Duración=6.79h, Latencia=18.9min, Despertares=3.4, Variabilidad=26.5min
Grupo 2: Duración=7.98h, Latencia=18.6min, Despertares=1.0, Variabilidad=22.3min
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class SleepProfile:
    def __init__(self, duration, latency, wakeups, variability):
        self.duration = duration
        self.latency = latency
        self.wakeups = wakeups
        self.variability = variability

    def to_vector(self):
        return [self.duration, self.latency, self.wakeups, self.variability]

class SleepDatasetGenerator:
    def __init__(self, n=300):
        self.n = n

    def generate(self):
        np.random.seed(0)
        durations = np.random.normal(7, 1.2, self.n)
        latencies = np.abs(np.random.normal(20, 10, self.n))
        wakeups = np.random.poisson(1.5, self.n)
        variabilities = np.abs(np.random.normal(30, 15, self.n))

        profiles = []
        for d, l, w, v in zip(durations, latencies, wakeups, variabilities):
            profiles.append(SleepProfile(d, l, w, v))
        return profiles

class SleepClusterer:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        self.scaler = StandardScaler()

    def fit(self, profiles):
        X = np.array([p.to_vector() for p in profiles])
        X_scaled = self.scaler.fit_transform(X)
        self.kmeans.fit(X_scaled)
        self.labels = self.kmeans.labels_
        return X_scaled, self.labels

    def get_cluster_centers(self):
        return self.scaler.inverse_transform(self.kmeans.cluster_centers_)

class SleepAnalysisExample:
    def run(self):
        generator = SleepDatasetGenerator()
        profiles = generator.generate()

        clusterer = SleepClusterer(n_clusters=3)
        X_scaled, labels = clusterer.fit(profiles)

        df = pd.DataFrame([p.to_vector() for p in profiles],
                          columns=["Duración", "Latencia", "Despertares", "Variabilidad"])
        df["Grupo"] = labels
        df["Grupo"] = df["Grupo"].astype(int)  # <-- Aquí está la solución

        print("📌 Centroides de los grupos:")
        centers = clusterer.get_cluster_centers()
        for i, c in enumerate(centers):
            print(f"Grupo {i}: Duración={c[0]:.2f}h, Latencia={c[1]:.1f}min, Despertares={c[2]:.1f}, Variabilidad={c[3]:.1f}min")

        colores = ['blue', 'green', 'orange']
        plt.figure(figsize=(8, 6))
        for i in range(clusterer.n_clusters):
            subset = df[df["Grupo"] == i]
            plt.scatter(subset["Duración"], subset["Variabilidad"],
                        c=colores[i], label=f"Grupo {i}", alpha=0.6)

        plt.xlabel("Duración del sueño (horas)")
        plt.ylabel("Variabilidad en horario de dormir (minutos)")
        plt.title("💤 Agrupación de perfiles de sueño (K-Means)")
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    example = SleepAnalysisExample()
    example.run()
