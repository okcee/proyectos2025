# Random Forest (Bosque Aleatorio)
'''
Random Forest es una combinación de árboles de decisión donde cada árbol selecciona una clase y luego se combinan las decisiones de cada árbol para seleccionar una clase final ganadora.  
Es uno de los algoritmos de aprendizaje de clasificación con mayor precisión.
Funciona eficientemente en bases de datos grandes y puede manejar cientos de variables de entrada.

Ensemble de Árboles de Decisión: Como bien dices, es una técnica de ensemble que combina múltiples árboles de decisión. No es solo un árbol, sino un "bosque" de ellos.
Votación (o Promedio): En problemas de clasificación, cada árbol del bosque "vota" por una clase, y la clase ganadora (la que recibe más votos) es la predicción final del modelo Random Forest. En problemas de regresión, se suele promediar las predicciones de cada árbol.
Alta Precisión: Es reconocido por ser uno de los algoritmos de clasificación más robustos y que, a menudo, logra una alta precisión. Esto se debe a que reduce el sobreajuste (overfitting) que puede ocurrir con árboles de decisión individuales profundos, promediando sus errores y sesgos.
Manejo de Datos Grandes y Muchas Variables: Es eficiente y escalable para trabajar con grandes conjuntos de datos y puede gestionar eficazmente bases de datos con cientos o miles de variables de entrada sin necesidad de una selección de características previa exhaustiva.
'''

import pandas as pd

vino = pd.read_csv("S:\\_proyectos2025\\Machine Learning\\Datasets\\vino.csv")

# print(vino.head())

X = vino.drop('Wine Type', axis=1)
y = vino['Wine Type']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

ramdomforest = RandomForestClassifier(n_estimators=80) # Tenemos que pasar el número de árboles (estimadores) que va a hacer para estimar el resultado
ramdomforest.fit(X_train, y_train)

predicciones = ramdomforest.predict(X_test)
print('Las predicciones son:\n', predicciones) # Predicciones
print('Los valores reales conocidos son: \n', y_test)

# Ahora valoraremos la precisión del modelo
from sklearn.metrics import classification_report

print('Precisión del modelo: \n', classification_report(y_test, predicciones))

