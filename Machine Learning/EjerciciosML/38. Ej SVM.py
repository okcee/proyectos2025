''' Clasificador de calidad del aire - Practicar con numpy para generar datos sintéticos y el algoritmo de SVM para clasificar la calidad del aire

Contexto:
Imagina que trabajas en una empresa de tecnología verde. Te piden crear un modelo que, basándose en datos de calidad del aire, prediga si un área es saludable o contaminada para las personas.

Objetivo:
Usando NumPy para generar datos simulados y SVM para clasificar, debes construir un modelo que prediga si un área tiene buena o mala calidad del aire.

Requisitos:
Crear una clase AirSample con los atributos:
pm25 (partículas finas PM2.5 en µg/m³)
pm10 (partículas gruesas PM10 en µg/m³)
o3 (ozono en ppb)
no2 (dióxido de nitrógeno en ppb)
quality (0 = saludable, 1 = contaminado) → solo en entrenamiento.
Crear una clase AirDataGenerator para generar datos sintéticos:
Regla orientativa: si pm25 > 35 o pm10 > 50 o no2 > 40 → contaminado.
Crear una clase AirQualityClassifier para:
Entrenar un modelo SVM usando los datos generados.
Predecir la calidad del aire de una nueva muestra.
Crear una clase AirQualityExample para:
Generar muestras.
Entrenar el clasificador.
Predecir la calidad de una muestra nueva (creada manualmente).
Mostrar el resultado de la predicción.

Ejemplo de uso
example = AirQualityExample()
example.run()
Salida esperada

🌍 Muestra de aire:
PM2.5: 22, PM10: 30, O3: 50, NO2: 35
✅ Predicción de calidad: Saludable ✅
'''

import numpy as np
from sklearn.svm import SVC


# Clase que representa una muestra de aire con características numéricas
class AirSample:
    def __init__(self, pm25, pm10, o3, no2, quality=None):
        self.pm25 = pm25
        self.pm10 = pm10
        self.o3 = o3
        self.no2 = no2
        self.quality = quality  # 0 = saludable, 1 = contaminado

    def to_vector(self):
        return [self.pm25, self.pm10, self.o3, self.no2]

    def __repr__(self):
        return f"AirSample(pm25={self.pm25}, pm10={self.pm10}, o3={self.o3}, no2={self.no2})"


# Clase para generar datos sintéticos de muestras de aire
class AirDataGenerator:
    def __init__(self, num_samples=100):
        self.num_samples = num_samples

    def generate(self):
        samples = []
        for _ in range(self.num_samples):
            pm25 = np.round(np.random.uniform(10, 50), 2)
            pm10 = np.round(np.random.uniform(20, 70), 2)
            o3 = np.round(np.random.uniform(30, 80), 2)
            no2 = np.round(np.random.uniform(10, 60), 2)

            # Regla orientativa para determinar si el área está contaminada
            quality = int(pm25 > 35 or pm10 > 50 or no2 > 40)

            samples.append(AirSample(pm25, pm10, o3, no2, quality))
        return samples


# Clase para entrenar un clasificador usando SVM
class AirQualityClassifier:
    def __init__(self):
        self.model = SVC(kernel='linear', random_state=42)

    def fit(self, samples):
        X = [sample.to_vector() for sample in samples]
        y = [sample.quality for sample in samples]
        self.model.fit(X, y)

    def predict(self, sample):
        return self.model.predict([sample.to_vector()])[0]


# Clase de ejemplo para ejecutar el sistema de clasificación
class AirQualityExample:
    def run(self):
        # Generar 200 muestras aleatorias
        generator = AirDataGenerator(200)
        samples = generator.generate()

        # Entrenar el modelo
        classifier = AirQualityClassifier()
        classifier.fit(samples)

        # Crear una nueva muestra de aire para predecir
        new_sample = AirSample(pm25=22, pm10=30, o3=50, no2=35)

        # Predecir la calidad del aire
        prediction = classifier.predict(new_sample)

        # Mostrar los resultados
        print("🌍 Muestra de aire:")
        print(f"PM2.5: {new_sample.pm25}, PM10: {new_sample.pm10}, O3: {new_sample.o3}, NO2: {new_sample.no2}")
        if prediction == 0:
            print("✅ Predicción de calidad: Saludable ✅")
        else:
            print("❌ Predicción de calidad: Contaminado ❌")


# Ejecutar el ejemplo
if __name__ == "__main__":
    example = AirQualityExample()
    example.run()
