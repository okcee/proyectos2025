''' Clasificador de snacks saludables - Practicar con numpy para la generación de datos sintéticos y con arboles de decisión para clasificar si un snak es saludable o no en función de sus características.

Objetivo:
En este ejercicio, aprenderás a crear un clasificador para predecir si un snack es saludable o no, basándote en características nutricionales como las calorías, azúcar, proteínas, grasas y fibra.
Usaremos un árbol de decisión para crear un modelo que prediga si un snack es saludable en función de estos atributos.

Descripción:
Imagina que trabajas en una aplicación de salud que recomienda snacks a los usuarios. Tienes acceso a un conjunto de datos que contiene información sobre varios snacks y su contenido nutricional.
Usaremos estos datos para entrenar un modelo que pueda predecir si un snack es saludable basándose en sus atributos.

Pasos a seguir:
Creación de la clase Snack:
Define una clase Snack que tenga los siguientes atributos: calories, sugar, protein, fat, fiber, y un atributo opcional is_healthy, que será el resultado que queremos predecir (1 si el snack es saludable, 0 si no lo es).
Crea un método to_vector() que convierta un snack en un vector de características (calorías, azúcar, proteínas, grasas, fibra).
Generación de Datos Sintéticos con la clase SnackGenerator:
Crea una clase SnackGenerator que sea capaz de generar un conjunto de datos sintéticos con snacks. Esta clase debe crear entre 50 y 200 snacks con valores aleatorios para las características mencionadas.
La variable is_healthy debe seguir una regla aproximada: un snack es saludable si tiene menos de 200 calorías, menos de 15 gramos de azúcar, menos de 10 gramos de grasa, y al menos 5 gramos de proteína o fibra.
Clasificador de Snacks con Árbol de Decisión:
Crea una clase SnackClassifier que use un árbol de decisión para clasificar los snacks.
Esta clase debe tener dos métodos:
fit(): entrenar el modelo usando un conjunto de snacks y sus etiquetas (is_healthy).
predict(): predecir si un snack específico es saludable o no.

Crear un Ejemplo de Uso:
Crea un objeto de la clase SnackRecommendationExample que entrene el clasificador utilizando el generador de snacks.
Luego, crea un snack de prueba con valores nutricionales conocidos, como 150 calorías, 10 gramos de azúcar, 6 gramos de proteína, 5 gramos de grasa y 3 gramos de fibra.
Usa el clasificador para predecir si este snack es saludable y muestra la predicción.

Requisitos:
Uso de Árbol de Decisión: Para realizar la clasificación, usa la librería sklearn y su DecisionTreeClassifier.
Generación de datos: Usa numpy para generar valores aleatorios.
Impresión de resultados: Imprime la información nutricional del snack de prueba junto con la predicción de si es saludable o no.

Resultado esperado:
Al ejecutar el código, el sistema debe mostrar la información nutricional del snack de prueba y una predicción indicando si es saludable o no.

Ejemplo de uso

# Ejecutar ejemplo
example = SnackRecommendationExample()
example.run()
Salida esperada

🔍 Snack Info:
Calories: 150, Sugar: 10g, Protein: 6g, Fat: 5g, Fiber: 3g
✅ Predicción: Este snack no es saludable.
'''

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import numpy as np


class Snack:
    """
    Clase que representa un snack con sus características nutricionales.
    """

    def __init__(self, calories, sugar, protein, fat, fiber, is_healthy=None):
        self.calories = calories
        self.sugar = sugar
        self.protein = protein
        self.fat = fat
        self.fiber = fiber
        self.is_healthy = is_healthy

    def to_vector(self):
        """
        Convierte las características del snack en un vector.
        """
        return [self.calories, self.sugar, self.protein, self.fat, self.fiber]

    def __str__(self):
        """
        Representación en string del snack.
        """
        return f"Calories: {self.calories}, Sugar: {self.sugar}g, Protein: {self.protein}g, Fat: {self.fat}g, Fiber: {self.fiber}g"


class SnackGenerator:
    """
    Clase para generar datos sintéticos de snacks.
    """

    def __init__(self, num_snacks=None):
        if num_snacks is None:
            # Generar entre 50 y 200 snacks si no se especifica
            self.num_snacks = np.random.randint(50, 201)
        else:
            self.num_snacks = num_snacks

    def generate(self):
        """
        Genera un conjunto de snacks con valores aleatorios.
        """
        snacks = []
        for _ in range(self.num_snacks):
            # Generar valores aleatorios para cada característica
            calories = np.random.randint(50, 400)
            sugar = np.random.randint(0, 30)
            protein = np.random.randint(0, 20)
            fat = np.random.randint(0, 25)
            fiber = np.random.randint(0, 10)

            # Determinar si es saludable según reglas aproximadas
            is_healthy = 1 if (calories < 300 and sugar < 20 and fat < 10 and
                               (protein >= 10 or fiber >= 10)) else 0

            # Crear y añadir el snack a la lista
            snack = Snack(calories, sugar, protein, fat, fiber, is_healthy)
            snacks.append(snack)

        return snacks


class SnackClassifier:
    """
    Clasificador de snacks utilizando árbol de decisión.
    """

    def __init__(self):
        self.model = DecisionTreeClassifier(random_state=42)
        self.is_trained = False

    def fit(self, snacks):
        """
        Entrena el modelo con un conjunto de snacks.
        """
        # Extraer características y etiquetas
        X = [snack.to_vector() for snack in snacks]
        y = [snack.is_healthy for snack in snacks]

        # Dividir en conjunto de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Entrenar el modelo
        self.model.fit(X_train, y_train)
        self.is_trained = True

        # Evaluar el modelo (opcional, para información)
        score = self.model.score(X_test, y_test)
        print(f"📊 Precisión del modelo: {score:.2f}")

    def predict(self, snack):
        """
        Predice si un snack es saludable o no.
        """
        if not self.is_trained:
            raise Exception("El modelo debe ser entrenado antes de hacer predicciones")

        # Obtener el vector de características del snack
        features = [snack.to_vector()]

        # Hacer la predicción
        prediction = self.model.predict(features)[0]

        return prediction


class SnackRecommendationExample:
    """
    Ejemplo de uso del sistema de recomendación de snacks.
    """

    def __init__(self):
        # Inicializar el generador y el clasificador
        self.generator = SnackGenerator()
        self.classifier = SnackClassifier()

    def run(self):
        # Generar snacks
        snacks = self.generator.generate()
        print(f"🍎 Generados {len(snacks)} snacks para entrenamiento")

        # Entrenar el clasificador
        self.classifier.fit(snacks)

        # Crear un snack de prueba
        test_snack = Snack(150, 10, 6, 5, 3)

        # Predecir si es saludable
        prediction = self.classifier.predict(test_snack)

        # Mostrar resultados
        print("\n🔍 Snack Info:")
        print(test_snack)

        if prediction == 1:
            print("✅ Predicción: Este snack es saludable.")
        else:
            print("✅ Predicción: Este snack no es saludable.")


# Ejecutar ejemplo
if __name__ == "__main__":
    example = SnackRecommendationExample()
    example.run()