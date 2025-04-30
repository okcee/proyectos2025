''' Árboles de decisión en Machine Learning
Un árbol de decisión es un modelo de predicción utilizado en diversos ámbitos que van desde la inteligencia artificial hasta la economía
Dado un conjunto de datos, se fabrican diagramas de construcciones lógicas, que sirven para representar y categorizar una serie de condiciones que ocurren de forma sucesiva, para resolución de un problema
'''

# Árboles de decisión - método de clasificación de machine learning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vinos = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/vino.csv")
# print(vinos.head())
# print(vinos.columns)


