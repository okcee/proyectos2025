'''
Vamos a ver ahora el procesamiento del lenguaje natural con las siglas PLN.
El procesamiento del lenguaje natural es un campo de las ciencias de la computación, de la inteligencia artificial y de la lingüística, que estudia las interacciones entre las computadoras y el lenguaje humano.
Utiliza mecanismos eficaces para la comunicación entre personas y máquinas por medio del lenguaje natural, es decir, de las lenguas del mundo.
Utiliza programas de ordenador que ejecutan o simulan la comunicación entre los ordenadores y las personas.
'''

# Ejercicio - Detección de spam
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
nltk.download('stopwords')

mensajes = [line.rstrip() for line in open("S:\\_proyectos2025\\Machine Learning\\Datasets\\SMSSpamCollection")]

# print(mensajes[0]) # Salida: ham\ **mensaje en si (ham es el tipo de mensaje, la \ es una tabulación)
# print(mensajes[1])

# print(len(mensajes)) # Comprobamos el número total de mensajes que tiene este archivo (Salida: 5574)

# Creamos un bucle para mostrar los X primeros mensajes
for mensaje in enumerate(mensajes[:5]):
    print(mensaje)

# Para hacer más cómodo trabajar con estos datos, creamos un dataset usando pandas
mensajes_df = pd.read_csv("S:\\_proyectos2025\\Machine Learning\\Datasets\\SMSSpamCollection", sep='\t', names=["etiqueta", "mensaje"])

# print('Mensajes', mensajes_df.head(6))

# Queremos saber la longitud de cada uno de los mensajes y verlo en un gráfico. Para lo cual necesitamos crear una nueva columna con los datos de la longitud
mensajes_df["longitud"] = mensajes_df["mensaje"].apply(len)
print('Mensajes', mensajes_df.head(6))

# Ahora usamos matplotlib para representar la longitud de los mensajes y hacernos una idea de la longitud en función del tipo de mensaje
# Creamos un histograma con el campo de la longitud
mensajes_df["longitud"].plot.hist(bins=100)
# plt.show()
plt.close()
# Estadística de la columna longitud
print('Estadísticas del dataset: \n',mensajes_df["longitud"].describe())

# Saber cual es el mensaje que tiene 910 de longitud
print('El mensaje que tiene 910 caracteres de longitud es: ',mensajes_df[mensajes_df["longitud"] == 910].iloc[0])

# Histograma comparando la longitud de los mensajes según su tipo
mensajes_df.hist(column="longitud", by="etiqueta", bins=100, figsize=(10,5))
# plt.show()
plt.close()

# Procesamiento de texto
# Crearemos una función para procesar distintos textos, quitar los signos de puntuación y las palabras irrelevantes

cadena = 'Mensaje de ejemplo! Nota: Este mensaje tiene signos de puntuación'
# Eliminamos signos de puntuación
# print(string.punctuation) # string.punctuation - Una función con todos los signos de puntuación

sin_puntuación = [c for c in cadena if c not in string.punctuation] # Variable quitados los signos de puntuación
sin_puntuación = ''.join(sin_puntuación) # Lo concatenamos para que sea una cadena de caracteres
# print(sin_puntuación)

# Eliminamos las palabras que no sean clave para nosotros importando la función stopwords (from nltk.corpus import stopwords)
# print(stopwords.words("spanish"))

palabras = sin_puntuación.split()
cadena_limpia = [palabra for palabra in palabras if palabra.lower() not in stopwords.words("spanish")] # Quitamos las palabras que no son importantes
# print('La cadena de caracteres limpia es : \n', cadena_limpia)

# En este próximo paso vamos a crear una función de procesamiento de texto donde vamos a introducir los comandos hechos anteriormente para eliminar los signos de puntuación y las palabras no relevantes

def procesar_texto(cadena):
    sin_puntuación = [c for c in cadena if c not in string.punctuation]
    sin_puntuación = ''.join(sin_puntuación)
    palabras = sin_puntuación.split()
    cadena_limpia = [palabra for palabra in palabras if palabra.lower() not in stopwords.words("spanish")]
    return cadena_limpia

# print(mensajes_df["mensaje"].head(10).apply(procesar_texto))


# Ahora el siguiente paso sería vectorizar
transformador = CountVectorizer(analyzer=procesar_texto).fit(mensajes_df["mensaje"]) # Esta variable tiene un vocabulario de las palabras importantes de cada mensaje
# print(transformador.vocabulary_)

mensaje3 = mensajes_df["mensaje"][3]
print('Mensaje 3 original', mensaje3)

mensaje3_transformado = transformador.transform([mensaje3])
print('Mensaje 3 transformado', mensaje3_transformado)

# Pasamos a organizar las predicciones
# Vamos a  dividir todos nuestros mensajes en mensajes de entrenamiento, mensaje de pruebas, etiquetas de entrenamiento y etiquetas de prueba
m_ent, m_pru, e_ent, e_pru = train_test_split(mensajes_df["mensaje"],mensajes_df["etiqueta"],test_size=0.3)
pipeline = Pipeline([
    ('vectorizar', CountVectorizer(analyzer=procesar_texto)),
    ('transformador', TfidfTransformer()),
    ('clasificar', RandomForestClassifier())
])

pipeline.fit(m_ent, e_ent)

# Realizamos las predicciones
predicciones = pipeline.predict(m_pru)

# Creamos un informe de clasificación para comprarar las etiquetas originales (e_pru) con las predicciones
print(classification_report(e_pru, predicciones))
