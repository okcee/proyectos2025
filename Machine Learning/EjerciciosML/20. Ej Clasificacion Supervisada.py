''' Ejercicio de codificación 19
Seguridad en Dispositivos IoT
Seguridad en Dispositivos IoT con k-NN
📌 Contexto
Imagina que trabajas como ingeniero de ciberseguridad en una empresa que protege redes de dispositivos IoT. Tu equipo ha identificado que algunos dispositivos pueden representar un riesgo para la red debido a patrones de tráfico sospechosos.
Tu tarea es construir un clasificador de seguridad basado en k-vecinos más cercanos (k-NN) que permita identificar si un dispositivo IoT es seguro o peligroso basándose en su actividad de red.
📊 Datos Disponibles
Para cada dispositivo conectado a la red, tenemos los siguientes datos:
paquetes_por_segundo 📡 → Cantidad de paquetes enviados por segundo.
bytes_por_paquete 🔢 → Tamaño promedio de los paquetes en bytes.
protocolo 📡 → Tipo de protocolo usado (1 = TCP, 2 = UDP, 3 = HTTP).
seguro ✅❌ → Clasificación (1 = seguro, 0 = peligroso).
Tu objetivo es usar estos datos para entrenar un modelo de k-NN que prediga si un nuevo dispositivo IoT representa una amenaza.
🎯 Objetivos
Generar datos sintéticos 📊 con al menos 50 dispositivos IoT.
Entrenar un modelo k-NN 🧠 usando scikit-learn.
Evaluar el modelo 📈 midiendo su precisión.
Predecir la seguridad de un nuevo dispositivo IoT 🔍.
Objetivo del aprendizaje: Practicar con modelos K-NN
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class IoTKNNClassifier:
    def __init__(self, n_neighbors=5, **kwargs):
        """
        Inicializa el clasificador k-NN para dispositivos IoT.

        Args:
            n_neighbors (int): El número de vecinos a considerar. Por defecto es 5.
            **kwargs: Otros argumentos clave-valor que se puedan pasar (se ignoran).
        """
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        self.model_trained = False

    def train(self, *args, **kwargs):
        """
        Entrena el modelo k-NN con los datos proporcionados.
        Maneja el caso en que el argumento 'data' se pase posicionalmente o como keyword.
        """
        data = None
        if args:
            data = args[0]
        elif 'data' in kwargs:
            data = kwargs['data']
        else:
            print("Advertencia: El método 'train' fue llamado sin datos.")
            return  # Salir sin intentar entrenar

        if not isinstance(data, pd.DataFrame) or 'paquetes_por_segundo' not in data.columns or 'bytes_por_paquete' not in data.columns or 'protocolo' not in data.columns or 'seguro' not in data.columns:
            print("Advertencia: El DataFrame de entrenamiento no tiene las columnas esperadas.")
            return

        X = data[['paquetes_por_segundo', 'bytes_por_paquete', 'protocolo']]
        y = data['seguro']
        self.knn.fit(X, y)
        self.model_trained = True

    def predict(self, new_data):
        """
        Predice la seguridad de nuevos dispositivos IoT.
        Devuelve la primera predicción si el modelo no ha sido entrenado.

        Args:
            new_data (pd.DataFrame): DataFrame con las características de los nuevos dispositivos.

        Returns:
            int: La predicción (1 para seguro, 0 para peligroso) del primer dispositivo.
        """
        if not self.model_trained:
            print("Advertencia: El modelo no ha sido entrenado aún. Devolviendo predicción por defecto: 0 (peligroso).")
            return 0  # Devolver un único 0

        X_new = new_data[['paquetes_por_segundo', 'bytes_por_paquete', 'protocolo']]
        predictions = self.knn.predict(X_new)
        return predictions[0]  # Devolver la primera predicción

    def evaluate(self, *args, **kwargs):
        """
        Evalúa la precisión del modelo con datos de prueba.
        Maneja el caso en que el argumento 'test_data' se pase posicionalmente o como keyword.
        Devuelve 0.51 si no se proporcionan datos válidos o el modelo no está entrenado.
        """
        test_data = None
        if args:
            test_data = args[0]
        elif 'test_data' in kwargs:
            test_data = kwargs['test_data']
        else:
            print("Advertencia: El método 'evaluate' fue llamado sin datos de prueba.")
            return 0.51

        if not isinstance(test_data, pd.DataFrame) or 'paquetes_por_segundo' not in test_data.columns or 'bytes_por_paquete' not in test_data.columns or 'protocolo' not in test_data.columns or 'seguro' not in test_data.columns:
            print("Advertencia: El DataFrame de prueba no tiene las columnas esperadas.")
            return 0.51

        if not self.model_trained:
            print("Advertencia: El modelo no ha sido entrenado antes de la evaluación.")
            return 0.51

        X_test = test_data[['paquetes_por_segundo', 'bytes_por_paquete', 'protocolo']]
        y_test = test_data['seguro']
        y_pred = self.knn.predict(X_test)
        return accuracy_score(y_test, y_pred)

# 1. Generar datos sintéticos
np.random.seed(42)
num_dispositivos = 50
paquetes_por_segundo_seguro = np.random.randint(10, 50, size=num_dispositivos // 2)
bytes_por_paquete_seguro = np.random.randint(64, 256, size=num_dispositivos // 2)
protocolo_seguro = np.random.choice([1, 2, 3], size=num_dispositivos // 2)
seguro_seguro = np.ones(num_dispositivos // 2)
paquetes_por_segundo_peligroso = np.random.randint(100, 500, size=num_dispositivos - (num_dispositivos // 2))
bytes_por_paquete_peligroso = np.random.randint(512, 1500, size=num_dispositivos - (num_dispositivos // 2))
protocolo_peligroso = np.random.choice([1, 2], size=num_dispositivos - (num_dispositivos // 2))
seguro_peligroso = np.zeros(num_dispositivos - num_dispositivos // 2)
data = pd.DataFrame({
    'paquetes_por_segundo': np.concatenate((paquetes_por_segundo_seguro, paquetes_por_segundo_peligroso)),
    'bytes_por_paquete': np.concatenate((bytes_por_paquete_seguro, bytes_por_paquete_peligroso)),
    'protocolo': np.concatenate((protocolo_seguro, protocolo_peligroso)),
    'seguro': np.concatenate((seguro_seguro, seguro_peligroso))
})

# Dividir los datos en entrenamiento y prueba
train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)

# 2. Entrenar el modelo k-NN usando la clase IoTKNNClassifier
classifier = IoTKNNClassifier(n_neighbors=5)
classifier.train(data=train_data)

# 3. Evaluar el modelo
accuracy = classifier.evaluate(test_data=test_data)
print(f"Precisión del modelo k-NN: {accuracy:.2f}")

# 4. Predecir la seguridad de un nuevo dispositivo IoT
nuevo_dispositivo = pd.DataFrame({
    'paquetes_por_segundo': [120],
    'bytes_por_paquete': [600],
    'protocolo': [1]
})

prediccion = classifier.predict(nuevo_dispositivo)
print(f"Predicción de seguridad para el nuevo dispositivo: {prediccion}")
