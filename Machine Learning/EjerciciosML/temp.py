# exercise.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class IoTKNNClassifier:
    def __init__(self, n_neighbors=3):
        self.n_neighbors = n_neighbors
        self.model = None
        self.X_train = None
        self.y_train = None

    def fit(self):
        # Generar datos sintéticos
        np.random.seed(42)
        n_devices = 50

        data = {
            'paquetes_por_segundo': np.random.uniform(0, 100, n_devices),
            'bytes_por_paquete': np.random.uniform(50, 1500, n_devices),
            'protocolo': np.random.choice([1, 2, 3], n_devices),
            'seguro': np.random.choice([0, 1], n_devices)
        }

        df = pd.DataFrame(data)

        # Separar características y etiquetas
        X = df[['paquetes_por_segundo', 'bytes_por_paquete', 'protocolo']]
        y = df['seguro']

        # Dividir en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Guardar los datos para predicciones futuras si es necesario
        self.X_train = X_train
        self.y_train = y_train

        # Crear y entrenar el clasificador k-NN
        self.model = KNeighborsClassifier(self.n_neighbors)  # Pasar n_neighbors posicionalmente
        self.model.fit(X_train, y_train)

        # Evaluar precisión (opcional)
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Precisión del modelo: {accuracy:.2f}')

    def predict(self, new_data):
        if self.model is None:
            raise Exception("El modelo no ha sido entrenado. Llama a fit() primero.")
        return self.model.predict(new_data)

# Ejemplo de uso fuera de la clase (esto puede ser opcional o para pruebas internas)
if __name__ == "__main__": # --- Bloque Principal de Ejecución ---
    classifier = IoTKNNClassifier() # 1. Crear una instancia del clasificador
    classifier.fit() # 2. Llamar al método fit()
    # 3. Preparar los datos de un nuevo dispositivo para la predicción.
    nuevo_dispositivo = [[60, 300, 2]]
    columnas = ['paquetes_por_segundo', 'bytes_por_paquete', 'protocolo'] # Nombres de las columnas (deben coincidir con el entrenamiento)
    nuevo_dispositivo_df = pd.DataFrame(nuevo_dispositivo, columns=columnas) # Convertir a DataFrame con nombres de columnas
    prediccion = classifier.predict(nuevo_dispositivo_df) # 4. Realizar la predicción para el nuevo dispositivo usando el modelo entrenado
    print("Predicción:", prediccion) # 5. Mostrar el resultado de la predicción (0 = peligroso, 1 = seguro).
