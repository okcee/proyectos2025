'''
Vamos a ver ahora el procesamiento del lenguaje natural con las siglas PLN.
El procesamiento del lenguaje natural es un campo de las ciencias de la computación, de la inteligencia artificial y de la lingüística, que estudia las interacciones entre las computadoras y el lenguaje humano.
Utiliza mecanismos eficaces para la comunicación entre personas y máquinas por medio del lenguaje natural, es decir, de las lenguas del mundo.
Utiliza programas de ordenador que ejecutan o simulan la comunicación entre los ordenadores y las personas.
'''

# Ejercicio - Detección de spam
import nltk

mensajes = [line.rstrip() for line in open("S:\\_proyectos2025\\Machine Learning\\Datasets\\SMSSpamCollection")]
