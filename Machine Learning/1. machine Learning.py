# Scikit Learn,paquete de machine learning con muchos algoritmos pre-construídos
# Forma de trabajar
'''
from slearn.linear_model import LinearRegression    # Primero se importa el modelo
modelo = LinearRegresion(normalize=True)    # Inicializar los parámetros del modelo.

Los datos disponibles se dividen en datos de entrenamiento y datos de prueba
Entrenar el modelo con datos de entrenamiento. Ej: "modelo.fit(x_train, y_train)"
Predecir las etiquetas o valores para los datos. Ej: "predicciones = modelo.fit(x_test)"
Datos de prueba. Ej: "train_test_split"
Con la obtención de estos datos, podemos evaluar el modelo de machine learning comparando nuestras predicciones con los valores correctos de los datos de prueba.
'''