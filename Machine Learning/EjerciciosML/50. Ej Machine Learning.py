''' Detectar correo electrónico spam - Practicar con algoritmos de machine learning

Clasificación de Emails: ¿Spam o No Spam?

Contexto: Tienes un conjunto de datos que contiene información sobre emails. Cada email tiene un conjunto de características, como la longitud del mensaje, la frecuencia de ciertas palabras clave, la cantidad de enlaces, y otros aspectos relevantes. El objetivo es construir un modelo de clasificación para predecir si un email es Spam o No Spam.

Objetivo: Tu tarea es implementar un modelo de clasificación que, dada la información de un email (características como la longitud del mensaje y la frecuencia de palabras clave), sea capaz de predecir si el email es Spam (1) o No Spam (0).

Funciones a Implementar:
Generar datos de emails:
Función: generar_datos_emails(num_muestras)
Esta función debe generar un conjunto de datos ficticios con num_muestras emails.
Cada email tendrá las siguientes características:
longitud_mensaje: Un número aleatorio que representa la longitud del email en caracteres (entre 50 y 500).
frecuencia_palabra_clave: Un número aleatorio que representa la frecuencia de una palabra clave relacionada con spam (entre 0 y 1).
cantidad_enlaces: Un número aleatorio que representa la cantidad de enlaces en el email (entre 0 y 10).
Cada email será etiquetado como Spam (1) o No Spam (0).

Entrenar el modelo SVM:
Función: entrenar_modelo_svm(datos, etiquetas)
Esta función debe tomar un conjunto de datos con características de emails y sus etiquetas, y entrenar un modelo de clasificación.
La salida debe ser el modelo entrenado.

Realizar predicciones:
Función: predecir_email(modelo, longitud_mensaje, frecuencia_palabra_clave, cantidad_enlaces)
Esta función debe tomar un modelo entrenado y las características de un nuevo email, y devolver si el email es Spam o No Spam.
La salida debe ser una cadena de texto que indique si el email es Spam o No Spam.

Instrucciones:
Generar Datos: Para empezar, debes generar un conjunto de datos con emails etiquetados (Spam o No Spam).
Entrenar el Modelo: Entrenar el modelo de clasificación basado en las características del email.
Predicciones: Utiliza el modelo entrenado para predecir si un email es Spam o No Spam según sus características.
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# Función para generar datos de correos electrónicos
def generar_datos_emails(num_muestras):
    np.random.seed(42)

    X = []  # Características: [longitud_mensaje, frecuencia_palabra_clave, cantidad_enlaces]
    y = []  # Etiquetas: 1 (Spam) o 0 (No Spam)

    for _ in range(num_muestras):
        longitud_mensaje = np.random.randint(50, 501)  # Longitud del mensaje entre 50 y 500 caracteres
        frecuencia_palabra_clave = np.random.uniform(0, 1)  # Frecuencia de palabra clave entre 0 y 1
        cantidad_enlaces = np.random.randint(0, 11)  # Cantidad de enlaces entre 0 y 10

        # Etiqueta: 1 (Spam) si tiene más de 2 enlaces y la frecuencia de palabra clave es mayor que 0.5
        if cantidad_enlaces > 2 and frecuencia_palabra_clave > 0.5:
            y.append(1)  # Spam
        else:
            y.append(0)  # No Spam

        X.append([longitud_mensaje, frecuencia_palabra_clave, cantidad_enlaces])  # Añadir características

    return np.array(X), np.array(y)


# Función para entrenar un modelo SVM
def entrenar_modelo_svm(X, y):
    # Dividir los datos en conjunto de entrenamiento y prueba (70% entrenamiento, 30% prueba)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Usar el clasificador SVM (máquinas de soporte vectorial)
    modelo = SVC(kernel='linear')  # Usamos el kernel lineal
    modelo.fit(X_train, y_train)  # Entrenar el modelo

    # Evaluar el modelo en el conjunto de prueba
    y_pred = modelo.predict(X_test)
    precision = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {precision * 100:.2f}%")

    return modelo


# Función para predecir si un email es Spam o No Spam
def predecir_email(modelo, longitud_mensaje, frecuencia_palabra_clave, cantidad_enlaces):
    # Realizar una predicción para un nuevo email
    prediccion = modelo.predict([[longitud_mensaje, frecuencia_palabra_clave, cantidad_enlaces]])

    # Devolver el mensaje adecuado según la predicción
    if prediccion == 1:
        return 'El email es Spam.'
    else:
        return 'El email no es Spam.'


# Ejemplo de flujo completo
# Generar un conjunto de datos de emails
num_muestras = 1000  # Puedes ajustar este número para generar más o menos datos
X, y = generar_datos_emails(num_muestras)

# Entrenar el modelo SVM
modelo = entrenar_modelo_svm(X, y)

# Realizar una predicción para un nuevo email
longitud_mensaje = 300  # Ejemplo: el email tiene 300 caracteres
frecuencia_palabra_clave = 0.7  # Ejemplo: la frecuencia de la palabra clave es 0.7
cantidad_enlaces = 5  # Ejemplo: el email tiene 5 enlaces

mensaje_prediccion = predecir_email(modelo, longitud_mensaje, frecuencia_palabra_clave, cantidad_enlaces)

# Mostrar el mensaje de predicción
print(mensaje_prediccion)
