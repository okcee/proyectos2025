''' REGRESIÓN LOGÍSTICA: Limpieza de datos
Vamos a hacer una limpieza del dataset titanic.
Modificaremos estos valores nulos, para cambiar el valor nulo por el valor medio de la edad según la clase en la que está.
Para lo cuál calcularemos el valor medio de la edadpor cada clase y se la vamos a poner en aquellas filas donde no tenga ningún valor.
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

# Vamos a comenzar a hacer la limpieza de datos
# 1. Vamos a calcular mediante un diagrama de cajs cuál es la edad media por cada una de las categorías (primera, segunda y tercera clase)
sns.boxplot(x='Pclass', y='Age', data=entrenamiento, palette='Set1')
# plt.show()
plt.close()

# 2. Haremos una función para ir rellenando los valores nuelos con estos
def edad_media(columnas):
    edad = columnas[0]
    clase = columnas[1]
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
