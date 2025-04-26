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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

