''' REGRESIÓN LOGÍSTICA
La regresión logistica es un tipo de análisis de regresión, utilizado para predecir el resultado de una variable categórica (una variable que puede adoptar un número limmitado de categorías) en función de otras variables independientes.
Es útil para moldear la probabilidad de que un evento pueda ocurrir en función de otros factores.
Es un método de clasificación, por ejemplo, para clasificar los correos según sean válidos o no, para clasificar a las personas que solicitan un prestamo según lo puedan pagar o no, o para clasificar a las personas según tengan o no una enfermedad concreta.
Estos ejemplos son ejemplos de clasificaciones binarias, es las que sólo hay dos categorías (sí o no)(categoria 1 o categoría 2)
La función de regresión logística recoge cualquier valor (eje X) y devolverá siempre un valor entre 0 y 1 (eje Y). Si el resultado es >=0.5, la salida será 1, si el resultado es < 0.5, la salida será 0.
Una matriz de confusión sirve para evaluar nuestro modelo de regresión logística. Evaluamos cuales son los positivos correctos (PC), negativos correctos (NC), falsos positivos (FP) que es el error tipo 1 y, falsos negativos (FN) que es el error tipo 2.
La precisión sirve para saber la probabilidad de acierto en la predicción.
    Precisión = Positivos correctos (PC) + Negativos correctos (NC) / Total
La tasa de error sirve para saber la probabilidad de error en la predicción.
    Tasa de error = Falsos positivos (FP) + Falsos Negativos (FN) / Total
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

entrenamiento = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/train.csv")
# print(entrenamiento.head())
# print(entrenamiento.columns) # Ver las columnas del dataset

# Para saber si en un dataset, una columa tiene valores nulos, podemos crear un mapa de calor (heatmap). En este, con el método "isnull()", los datos nulos se mostrarán en color blanco respecto al los no nulos, que serán en color negro
sns.heatmap(entrenamiento.isnull())
# plt.show()
plt.close()
# Vemos con el heatmap que hay valores nulos en las columnas "Age" y "Cabin"

# Podemos contar el número total de supervivientes, mediante seaborn (sns)
sns.countplot(x='Survived', data=entrenamiento, palette='bright')
# plt.show()
plt.close()

# Podemos dividir este contador de supervivientes y añadirle una nueva variable
sns.countplot(x='Survived', data=entrenamiento, hue='Sex', palette='bright')
# plt.show()
plt.close()

# Podemos hacer una distribución por edades, mediante Seaborn
sns.displot(entrenamiento['Age'].dropna(), kde=False, bins=30) # .dropna() (Borra los valores nulos). kde=False, que no ponga la línea curva del histograma. bins=30 selecciona el número de columnas
# plt.show()
plt.close()
# Podemos hacer una distribución por edades, directamente desde el dataframe
print(entrenamiento['Age'].plot.hist(bins=30))
# plt.show()
plt.close()

# Podemos saber el número de familiares que tenía cada pasajero mediante el dataset
print(entrenamiento['SibSp'].plot.hist(bins=30))
# plt.show()
plt.close()

# Podemos sacar el número de familiares que tenía cada pasajero mediante Seaborn
sns.countplot(x='SibSp', data=entrenamiento, palette='viridis')
plt.title('Número de Hermanos/Cónyuges a Bordo')
# plt.show()
plt.close()

# Podemos sacarlo de manera más interactiva (usando plotly.express) import plotly.express as px



# Suponiendo que 'entrenamiento' es tu DataFrame
# entrenamiento = pd.read_csv("S:/_proyectos2025/Machine Learning/Datasets/train.csv") # Si no está cargado

# 1. Calcula las frecuencias (igual que antes)
sibsp_counts = entrenamiento['SibSp'].value_counts().reset_index()
sibsp_counts.columns = ['SibSp', 'count'] # Renombrar columnas para px.bar

# 2. Crea el gráfico de barras interactivo con plotly.express (Colores: https://plotly.com/python/builtin-colorscales/)
fig = px.bar(sibsp_counts,
             x='SibSp',
             y='count',
             title='Número de Hermanos/Cónyuges a Bordo',
             labels={'SibSp': 'Número de Hermanos/Cónyuges', 'count': 'Cantidad de Pasajeros'},
             color='SibSp', # Map the 'SibSp' column to color
             color_continuous_scale='Viridis' # Use the Viridis continuous color scale
            )

# 3. Muestra el gráfico (se abrirá en el navegador o se mostrará en el entorno como Jupyter)
fig.show()

# Ya no necesitas plt.close() para figuras de Plotly




# --- LIMPIEZA DE DATOS ---
# El siguiente paso es tratar los datos nulos para poder entrenar el modelo.
# Una opción es eliminar las filas con datos nulos, pero perderíamos información.
# Otra opción es imputar los valores nulos, es decir, rellenarlos con algún valor estimado.

# Para la columna 'Age', podemos imputar la edad media de todos los pasajeros.
# O mejor aún, la edad media según la clase ('Pclass') en la que viajaban.

plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass', y='Age', data=entrenamiento, palette='winter')
plt.title('Edad media por Clase')
# plt.show()
plt.close()

# Calculamos la edad media por clase
edad_media_por_clase = entrenamiento.groupby('Pclass')['Age'].mean()
print("\nEdad media por clase:")
print(edad_media_por_clase)

# Creamos una función para imputar la edad basada en la clase
def imputar_edad(columnas):
    Edad = columnas[0]
    Clase = columnas[1]

    if pd.isnull(Edad):
        if Clase == 1:
            return edad_media_por_clase[1] # Edad media de la clase 1
        elif Clase == 2:
            return edad_media_por_clase[2] # Edad media de la clase 2
        else:
            return edad_media_por_clase[3] # Edad media de la clase 3
    else:
        return Edad

# Aplicamos la función a la columna 'Age'
entrenamiento['Age'] = entrenamiento[['Age', 'Pclass']].apply(imputar_edad, axis=1)

# Verificamos que ya no hay nulos en 'Age' con el heatmap
sns.heatmap(entrenamiento.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title('Mapa de calor después de imputar Edad')
# plt.show()
plt.close()

# La columna 'Cabin' tiene demasiados valores nulos. Lo más sencillo es eliminarla.
entrenamiento.drop('Cabin', axis=1, inplace=True)

# Verificamos de nuevo el heatmap
sns.heatmap(entrenamiento.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title('Mapa de calor después de eliminar Cabin')
# plt.show()
plt.close()

# Puede que queden algunos valores nulos en otras columnas (ej. 'Embarked').
# Como son pocos, podemos eliminar esas filas directamente.
entrenamiento.dropna(inplace=True)

# --- CONVERSIÓN DE VARIABLES CATEGÓRICAS ---
# El modelo de regresión logística necesita variables numéricas.
# Debemos convertir las variables categóricas (como 'Sex', 'Embarked') en variables dummy.
# Las variables dummy son variables binarias (0 o 1) que representan las categorías.

# Vemos las columnas de tipo 'object' (categóricas)
print("\nColumnas antes de convertir a dummies:")
print(entrenamiento.info())

sexo = pd.get_dummies(entrenamiento['Sex'], drop_first=True) # drop_first=True para evitar multicolinealidad (quita la primera categoría, ej. 'female')
embarque = pd.get_dummies(entrenamiento['Embarked'], drop_first=True) # Quita la categoría 'C'

# Eliminamos las columnas originales 'Sex', 'Embarked', 'Name', 'Ticket' que no usaremos o ya hemos convertido
entrenamiento.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)

# Concatenamos las nuevas variables dummy al DataFrame
entrenamiento = pd.concat([entrenamiento, sexo, embarque], axis=1)

print("\nPrimeras filas después de procesar:")
print(entrenamiento.head())

print("\nColumnas después de convertir a dummies:")
print(entrenamiento.info()) # Ahora todas las columnas deberían ser numéricas

# --- CONSTRUCCIÓN DEL MODELO DE REGRESIÓN LOGÍSTICA ---
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Separamos las características (X) de la variable objetivo (y)
X = entrenamiento.drop('Survived', axis=1) # Todas las columnas excepto 'Survived'
y = entrenamiento['Survived'] # La columna 'Survived'

# Dividimos los datos en conjunto de entrenamiento y conjunto de prueba
# test_size=0.3 significa que el 30% de los datos serán para prueba
# random_state es una semilla para que la división sea reproducible
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Creamos y entrenamos el modelo de Regresión Logística
modelo_logistico = LogisticRegression(max_iter=1000) # Aumentamos max_iter si no converge
modelo_logistico.fit(X_train, y_train)

# Realizamos predicciones sobre el conjunto de prueba
predicciones = modelo_logistico.predict(X_test)

# --- EVALUACIÓN DEL MODELO ---

# Matriz de Confusión
print("\nMatriz de Confusión:")
matriz_confusion = confusion_matrix(y_test, predicciones)
print(matriz_confusion)

# Visualización de la Matriz de Confusión
sns.heatmap(matriz_confusion, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicción')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusión')
# plt.show()
plt.close()

# Reporte de Clasificación (Precisión, Recall, F1-Score)
print("\nReporte de Clasificación:")
reporte = classification_report(y_test, predicciones)
print(reporte)

# Calculamos la precisión manualmente (Accuracy)
# Precisión = (Verdaderos Positivos + Verdaderos Negativos) / Total
# TP = matriz_confusion[1, 1]
# TN = matriz_confusion[0, 0]
# FP = matriz_confusion[0, 1]
# FN = matriz_confusion[1, 0]
# precision_manual = (TP + TN) / (TP + TN + FP + FN)
# print(f"\nPrecisión calculada manualmente: {precision_manual:.4f}")

# La precisión también la da el reporte de clasificación (accuracy)
# o podemos usar la función score del modelo
precision_modelo = modelo_logistico.score(X_test, y_test)
print(f"\nPrecisión del modelo (Accuracy): {precision_modelo:.4f}")

# Tasa de error = (Falsos Positivos + Falsos Negativos) / Total
# tasa_error_manual = (FP + FN) / (TP + TN + FP + FN)
# print(f"Tasa de error calculada manualmente: {tasa_error_manual:.4f}")
print(f"Tasa de error del modelo: {1 - precision_modelo:.4f}")

