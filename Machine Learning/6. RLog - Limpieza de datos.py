''' REGRESIÓN LOGÍSTICA: Limpieza de datos + Entrenamiento del Modelo
Vamos a hacer una limpieza del dataset titanic.
Modificaremos estos valores nulos, para cambiar el valor nulo por el valor medio de la edad según la clase en la que está.
Para lo cuál calcularemos el valor medio de la edadpor cada clase y se la vamos a poner en aquellas filas donde no tenga ningún valor.
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px

from sklearn.model_selection import train_test_split # Dividir dataset en características y valor objetivo
from sklearn.linear_model import LogisticRegression # Modulo de regresión logística para entrenar un modelo
from sklearn.metrics import classification_report # importar las métricas
from sklearn.metrics import confusion_matrix # Importa la matriz de confusión
from sklearn.preprocessing import StandardScaler # Importar el escalador

entrenamiento = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/train.csv")
# print(entrenamiento.head())
# print(entrenamiento.columns) # Ver las columnas del dataset

# Para saber si en un dataset, una columa tiene valores nulos, podemos crear un mapa de calor (heatmap). En este, con el método "isnull()", los datos nulos se mostrarán en color blanco respecto al los no nulos, que serán en color negro
sns.heatmap(entrenamiento.isnull())
# plt.show()
plt.close()
# Vemos con el heatmap que hay valores nulos en las columnas "Age" y "Cabin"

# Vamos a comenzar a hacer la limpieza de datos
# 1. Vamos a calcular mediante un diagrama de cajs cuál es la edad media por cada una de las categorías (primera, segunda y tercera clase)
sns.boxplot(x='Pclass', y='Age', hue='Pclass', data=entrenamiento, palette='Set1', legend=False)
# plt.show()
plt.close()

# 2. Haremos una función para ir rellenando los valores nuelos con estos
def edad_media(columnas):
    edad = columnas.iloc[0]
    clase = columnas.iloc[1]
    # Verificamos si el valor para esa fila es nulo, y si es nulo lo cambiamos por el valor de la media aproximada
    if pd.isnull(edad):
        if clase == 1:
            return 38
        elif clase == 2:
            return 30
        else:
            return 25
    else:
        return edad

# 3. En función de la edad media la tenemos que aplicar a cada uno de los valores de la columna edad
entrenamiento['Age'] = entrenamiento[['Age', 'Pclass']].apply(edad_media, axis=1) # Modificamos el dataset igualándola al dataset con dos columnas aplicandole, sobre las columnas (axis=1), la función que creamos anteriormente def edad_media(columnas)

# 4. Comprobamos la columna edad: 'Age'
sns.heatmap(entrenamiento.isnull())
# plt.show()
plt.close()
# Resultado dado por bueno

# 5. Pasamos a la columna 'Cabin' y , podemos ver que la mayoría de los datos de esta columna son nulos. Entonces decidimos borrar esta columna
entrenamiento.drop('Cabin', axis=1, inplace=True)

# 6. Verificamos cómo a quedado nuestro dataset
sns.heatmap(entrenamiento.isnull())
# plt.show()
plt.close()
print("Estado del dataset actual tras la limpieza de las columnas Age y Cabin")
print(entrenamiento.head(10))

# 7. Vamos a borrar las columnas que no utilizaremos en los análisis: 'Name', 'Ticket', 'Passengerld' 
entrenamiento.drop(['Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)
plt.show()
plt.close()
print("Estado del dataset actual tras la nueva limpieza  eliminando las columnas")
print(entrenamiento.head(10))

# 8. Mediante la función get.dummies vamos a covertir la columna 'Sex' de alfanumérica (male, female) a numérica. Por ejemplo: el hombre adoptará el valor de 1 y la mujer la de 0
print("\nColumna 'Sex' ANTES de get_dummies:")
print(entrenamiento['Sex'].head())
sexo_dummy = pd.get_dummies(entrenamiento['Sex'], drop_first=True, dtype=int) # dtype=int para tener 0s y 1s enteros
print("\nVariable dummy creada ('male'):")
print(sexo_dummy.head())
# Eliminar la columna original 'Sex' del DataFrame
entrenamiento.drop('Sex', axis=1, inplace=True)
entrenamiento = pd.concat([entrenamiento, sexo_dummy], axis=1) # Añadimos la nueva columna sexo_dummy a el dataset entrenamiento
print("\nDataFrame DESPUÉS de aplicar get_dummies y concatenar:")
print(entrenamiento.head(10))
# Verificar las columnas finales
print("\nColumnas actuales del DataFrame:")
print(entrenamiento.columns)

# 9. El puerto de embarque, vamos a convertirla de una columna con 3 valores alfanuméricos a 2 columnas con valor numérico binario
puerto = pd.get_dummies(entrenamiento['Embarked'])
print("\nValores iniciales de la columna Embarked:")
print(puerto.head())
puerto = pd.get_dummies(entrenamiento['Embarked'], drop_first=True, dtype=int)
entrenamiento = pd.concat([entrenamiento, puerto], axis=1)
print("\nValores actuales de la columna Embarked:")
print(puerto.head())
entrenamiento.drop('Embarked', axis=1, inplace=True)
print("\nValores finales sin la columna Embarked:")
print(entrenamiento.head())

''' REGRESIÓN LOGÍSTICA: Entrenamiento del Modelo
Crearemos las características y el valor objetivo. Valoraremos la predicción de la probabilidad de su sobrevive o no el pasajero en función del resto de características
'''
# 1. Dividimos y decidimos nuestro valor objetibo, la Y, el valor que vamos a predecir, la columna de 'Survived'
Y = entrenamiento['Survived']

# 2. Seleccionar las características, X, para lo cual, o bien seleccionamos todas las columnas menos 'Survived' o también podemos borrar la columna 'Survived' a nuestro Dataset
X = entrenamiento.drop('Survived', axis=1)
print(X.head())

# 3. Dividimos el dataset en dos conjuntos de datos, uno para entrenamiento (train) y el otro para hacer las pruebas (test)
# Recordar que test_site, elioge el porcentaje 0.3 (30%) de datos del conjunto que será empleado para pruebas, quedando el resto para entrenamiento. A su vez, ramdom_state, planta una semilla para que coja de forma aleatoria los valores dentro del dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=45)
print("\nCaracterísticas de entrenamiento:")
print(X_train)
print("\nCaracterísticas de prueba:")
print(X_test)

# 4. Creamos un modelo
modelo = LogisticRegression()
# Esta gran diferencia en las escalas de los datos de la características X, puede hacer que el algoritmo de optimización tarde mucho más en encontrar el punto óptimo, o que incluso no lo encuentre dentro del límite de iteraciones por defecto. Principalmente hay dos soluciones:
# Aumentar el número de iteraciones: modelo = LogisticRegression(max_iter=1000) # Se puede aumentar el número de iteraciones 
# Escalar los datos (Recomendado): Esta es generalmente la mejor práctica. Consiste en transformar tus características para que todas tengan una escala similar

# 5. Entrenamos el modelo con los datos de entrenamiento
modelo.fit(X_train, Y_train)

# 6. Hacer predicciones
predicciones = modelo.predict(X_test)
print("\nPredicciones:")
print(predicciones)

# 7. Se puede comparar con los datos reales
print("\nDatos reales de la columna 'Survived': ")
print(Y_test.head(20))

# 8. Evaluamos la precisión del modelo, a ver si es suficiente para nosotros, mediante las métricas
print("\nPrecisión: métricas")
print(classification_report(Y_test, predicciones))

# 9. Evaluamos la precisión del modelo, mediante la matriz de confusión, para ver positivos correctos, negativos correctos, falsos positivos y falsos negativos
print("\nPrecisión: matriz de confusión")
print(confusion_matrix(Y_test, predicciones))

''' Optimizar datos de las características para aumentar la predicción
Escalar los datos (Recomendado): Esta es generalmente la mejor práctica. Consiste en transformar tus características para que todas tengan una escala similar (por ejemplo, media 0 y desviación estándar 1, o todas entre 0 y 1). Esto ayuda enormemente a que los algoritmos de optimización converjan más rápido y de forma más estable. Se usa StandardScaler o MinMaxScaler de sklearn.preprocessing.
Importante: El escalador se debe "ajustar" (fit) solo con los datos de entrenamiento (X_train) para evitar fuga de datos (data leakage) del conjunto de prueba al de entrenamiento. Luego, se usa ese mismo escalador ajustado para transformar tanto X_train como X_test.
'''
# *** NUEVO: Escalar los datos ***
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # Ajustar y transformar en X_train
X_test_scaled = scaler.transform(X_test)     # Solo transformar en X_test

print("\nCaracterísticas de entrenamiento escaladas (primeras filas):")
print(X_train_scaled[:5]) # Mostrar algunas filas escaladas
print("\nCaracterísticas de prueba escaladas (primeras filas):")
print(X_test_scaled[:5])  # Mostrar algunas filas escaladas

# 4. Creamos un modelo
# Ahora puedes usar el max_iter por defecto o uno menor si quieres
modelo2 = LogisticRegression(random_state=45) # Añadir random_state para reproducibilidad

# 5. Entrenamos el modelo con los datos de entrenamiento ESCALADOS
modelo2.fit(X_train_scaled, Y_train) # Usar X_train_scaled

# 6. Hacer predicciones usando X_train_scaled
predicciones2 = modelo2.predict(X_test_scaled)
print("\nPredicciones con datos escalados:")
print(predicciones2)

# 7. Se puede comparar con los datos reales
print("\nDatos reales de la columna 'Survived': ")
print(Y_test.head(20))

# 8. Evaluamos la precisión del modelo, a ver si es suficiente para nosotros, mediante las métricas
print("\nPrecisión con datos escalados: métricas")
print(classification_report(Y_test, predicciones2))

# 9. Evaluamos la precisión del modelo, mediante la matriz de confusión, para ver positivos correctos, negativos correctos, falsos positivos y falsos negativos
print("\nPrecisión con datos escalados: matriz de confusión")
print(confusion_matrix(Y_test, predicciones2))


''' ¿Cómo se evalúa qué modelo es mejor si los resultados no son muy distintos?

Métricas Detalladas (classification_report): No te fijes solo en la accuracy general. Compara:
- Precision: Para cada clase (0 - No sobrevivió, 1 - Sobrevivió), ¿qué proporción de las predicciones para esa clase fueron correctas?
- Recall (Sensibilidad): Para cada clase real, ¿qué proporción fue correctamente identificada por el modelo?
- F1-Score: Es la media armónica de Precision y Recall. Es una buena métrica general, especialmente si hay desbalance entre clases (aunque en Titanic no es extremo).
- Support: El número de muestras reales de cada clase en el conjunto de test (Y_test).
- Compara los valores de Precision, Recall y F1-Score para la clase 0 y la clase 1 entre predicciones y predicciones2. Un modelo puede ser ligeramente mejor prediciendo supervivientes (clase 1) a costa de predecir peor los no supervivientes (clase 0), o viceversa. El modelo "mejor" dependerá de qué tipo de error te importa más evitar.

Matriz de Confusión (confusion_matrix):
[[TN, FP],      (Verdaderos Negativos, Falsos Positivos)
 [FN, TP]]      (Falsos Negativos, Verdaderos Positivos)
Busca si el segundo modelo (predicciones2) consigue:
Más Verdaderos Positivos (TP) y Verdaderos Negativos (TN).
Menos Falsos Positivos (FP) y Falsos Negativos (FN).

Convergencia del Modelo: ¡Este es un punto clave en tu caso!

El primer modelo (modelo) te dio una ConvergenceWarning. Esto significa que el algoritmo de optimización no terminó de encontrar la "mejor" solución posible dentro del número de pasos permitidos. El resultado que obtienes es el que tenía hasta ese momento.
El segundo modelo (modelo2), entrenado con datos escalados, probablemente no dio esa advertencia (puedes verificar la salida de la consola al ejecutar modelo2.fit). El escalado ayuda al algoritmo a converger más rápido y de forma más estable.
Conclusión: Aunque las métricas finales sean muy parecidas, el modelo entrenado con datos escalados (modelo2) es técnicamente más fiable y preferible, porque sí alcanzó la convergencia. Se considera que encontró una solución óptima (o muy cercana a ella) según los criterios del algoritmo. El primer modelo se quedó "a medias"
'''