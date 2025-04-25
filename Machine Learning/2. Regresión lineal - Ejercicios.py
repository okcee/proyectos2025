'''
La regresión lineal es un algoritmo de aprendizaje supervisado, para datos estructurados.
la regresión lineal es una aproximación para modelar la relación entre una variable escalar dependiente "y" y una o más variables explicativas "x".
La idea es dibujar una recta que indicará la tendencia del conjuntoi de datos.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/Housing.csv")

print(casas.head())