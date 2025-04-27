import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from matplotlib import pyplot as plt

casas = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/Housing.csv")
# print(casas.head()) # Visualizar primeros elementos
# print(casas.columns) # Lista con los nombres exactos de cada columnas


''' Estimar el precio futuro
Ahora tenemos que dividir los datos del dataset en eje X y eje Y.
X serían las características, que serían todas las columnas numéricas
y serían la variable objetivo (precio)
'''
X = casas[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']] # D
print(X.columns)
Y = casas['Price'] # El dato objetivo

''' Ahora vamos a dividir los datos en:
    - Datos de entrenamiento (_train)
    - Datos de pruebas (_test)
'''
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42) # test_size= Porcentaje del dataset
lrm = LinearRegression() # Creamos una variable que será una instancia de LinearRegression()
lrm.fit(X_train, Y_train) # Método fit para entrenamiento

''' Proceso de entrenamiento realizado:
. RL - Proceso Machine Learning.py"
Index(  ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms', 'Area Population'],
        dtype='object'  )
'''
''' Ahora evaluamos si el modelo del entrenamiento es correcto
El modelo ha tenido que ser capaz de pasar las características de las casa y sacar el precio objetivo de cada una de ellas
'''
predicciones = lrm.predict(X_test) # Para sacar el valor objetivo de cada una de ellas
print(predicciones)

# Cómo acceder a esas filas para comparar la predicción de tu modelo y evaluar el rendimiento mediante su índice
indice_a_comparar = 1501 # Elige el índice de la fila que quieres comparar (ej. la fila con índice original 1501)
if indice_a_comparar in Y_test.index: # 1. Verifica si ese índice realmente terminó en el conjunto de prueba
    X_fila_especifica = X_test.loc[[indice_a_comparar]] # 2. Obtén los datos de características (X) para esa fila específica usando .loc y doble corchete [[]]

    prediccion_especifica = lrm.predict(X_fila_especifica) # 3. Realiza la predicción SOLO para esa fila
    # predict() devuelve un array, incluso para una fila, así que accedemos al primer (y único) elemento [0]
    valor_predicho = prediccion_especifica[0] # predict() devuelve un array, incluso para una fila, así que accedemos al primer (y único) elemento [0]

    valor_real = Y_test.loc[indice_a_comparar] # 4. Obtén el valor real (Y) para esa misma fila usando .loc
    # 5. Imprime y compara los valores
    print(f"--- Comparación para la fila con índice original: {indice_a_comparar} ---")
    print(f"Valor Predicho por el modelo: {valor_predicho:.2f}") # :.2f formatea a 2 decimales
    print(f"Valor Real del dataset:      {valor_real:.2f}")
    print(f"Diferencia:                  {abs(valor_real - valor_predicho):.2f}")
else:
    print(f"El índice {indice_a_comparar} no se encuentra en el conjunto de prueba (Y_test).")

# Ahora para valorar la diferencia entre todos los datos entrenados y compararlos con los reales, prodemos utilizar un gráfico tipo scatter
plt.scatter(Y_test, predicciones) # Le pasamos los precios reales y las predicciones
# plt.show()
plt.close()
# Aquí observamos los datos, teniendo en cuenta que los datos reales son la diagonal, cuánto más se acerquen los puntos (predicción de los datos de entrenamiento), el modelo será más bueno

# Valorarlo haciendo un histograma, donde le pasaríamos los precios reales y se los restaríamos de las predicciones
sns.displot((Y_test - predicciones))
# plt.show()
plt.close()

''' Hay una serie de métricas para evaluar numéricamente el modelo (3 tipos)
MAE (Mean Absolute Error) - Media del valor absoluto de los errores
MSE (Mean Squared Error) - Media de los errores al cuadrado
RSME () - Raíz cuadrada de la media de los errores al cuadrado
Los valores obtenidos de cada modelo de entrenamiento se compararian con los obtenidos en otros entrenamientos
'''
# MAE
print(metrics.mean_absolute_error(Y_test, predicciones)) # Da 81135.57, cuánto menor sea este valor, mejor es el modelo

# MSE
print(metrics.mean_squared_error(Y_test, predicciones)) # Da 10068422551.40, cuánto menor sea este valor, mejor es el modelo. Al elevar los errores al cuadrado, el MSE penaliza los errores grandes mucho más que los errores pequeños.

# RSME
print(np.sqrt(metrics.mean_squared_error(Y_test, predicciones))) # 100341.53, cuánto mayor sea el número, más cerca o más correcto es el modelo de predicción