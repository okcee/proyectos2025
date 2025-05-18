''' Recomendador de plataforma - Practicar con los arboles de decisión en python
🎯 Título:
"¿Web, móvil o escritorio? – Recomendador de plataforma"

📘 Enunciado:
Imagina que trabajas en una consultora tecnológica que ayuda a startups y pequeñas empresas a decidir qué tipo de plataforma es la más adecuada para sus aplicaciones: web, móvil o escritorio.
Tu tarea será entrenar un modelo de aprendizaje automático que, dado un conjunto de características de un proyecto, sea capaz de predecir automáticamente la plataforma recomendada.

💾 Datos de entrada (proyectos)
Cada proyecto tiene las siguientes características:

🎯 Objetivo
Tu modelo deberá predecir el valor de recommended_platform para un nuevo proyecto a partir de sus características.

🛠️ Requisitos del ejercicio
Crear una clase Project para representar cada proyecto.
Crear una clase ProjectDataset que contenga una lista de proyectos y permita extraer los datos necesarios para el modelo.
Crear una clase PlatformRecommender que entrene un modelo basado en árboles de decisión (DecisionTreeClassifier) y permita hacer predicciones.

🧪 Ejemplo de uso
projects = [
    Project("AppGlobal", 5, 25.0, 6, True, False, "global", "web"),
    Project("IntranetCorp", 10, 40.0, 12, False, True, "empresa", "desktop"),
    Project("LocalDelivery", 3, 20.0, 4, True, True, "local", "mobile"),
    Project("CloudDashboard", 6, 50.0, 8, True, False, "empresa", "web"),
    Project("OfflineTool", 4, 15.0, 6, False, True, "local", "desktop"),
    Project("SocialBuzz", 2, 10.0, 3, True, False, "global", "mobile"),
]
new_project = Project("AIChatApp", 4, 30.0, 5, True, False, "global")
dataset = ProjectDataset(projects)
recommender = PlatformRecommender()
recommender.train(dataset)
prediction = recommender.predict(new_project)
print(f"Plataforma recomendada: {prediction}")

🧪 Salida esperada
Plataforma recomendada: mobile

✅ Requisitos adicionales
Puedes usar LabelEncoder para transformar variables categóricas (target_users).
Asegúrate de convertir los booleanos (realtime_required, needs_offline) en enteros (0 o 1) antes de entrenar el modelo.
Evalúa tu modelo con diferentes ejemplos para ver cómo se comporta.
'''

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

import numpy as np


# Clase para representar un proyecto
class Project:
    def __init__(self, project_name, team_size, budget, duration_months,
                 realtime_required, needs_offline, target_users, recommended_platform=None):
        self.project_name = project_name
        self.team_size = team_size
        self.budget = budget
        self.duration_months = duration_months
        self.realtime_required = int(realtime_required)
        self.needs_offline = int(needs_offline)
        self.target_users = target_users
        self.recommended_platform = recommended_platform


# Clase para gestionar un conjunto de proyectos y preparar los datos
class ProjectDataset:
    def __init__(self, projects):
        self.projects = projects
        self.label_encoder = LabelEncoder()
        self._fit_label_encoder()

    def _fit_label_encoder(self):
        target_users_list = [p.target_users for p in self.projects]
        self.label_encoder.fit(target_users_list)

    def get_features_and_labels(self):
        features = []
        labels = []
        for p in self.projects:
            features.append([
                p.team_size,
                p.budget,
                p.duration_months,
                p.realtime_required,
                p.needs_offline,
                self.label_encoder.transform([p.target_users])[0]
            ])
            labels.append(p.recommended_platform)
        return np.array(features), np.array(labels)

    def encode_project(self, project):
        return np.array([[
            project.team_size,
            project.budget,
            project.duration_months,
            project.realtime_required,
            project.needs_offline,
            self.label_encoder.transform([project.target_users])[0]
        ]])


# Clase que entrena y realiza predicciones
class PlatformRecommender:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.dataset = None

    def train(self, dataset):
        self.dataset = dataset
        X, y = dataset.get_features_and_labels()
        self.model.fit(X, y)

    def predict(self, project):
        if not self.dataset:
            raise ValueError("El modelo no ha sido entrenado todavía.")
        X_new = self.dataset.encode_project(project)
        return self.model.predict(X_new)[0]
