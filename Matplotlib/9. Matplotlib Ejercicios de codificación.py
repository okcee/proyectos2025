import matplotlib
import matplotlib.pyplot as plt
import numpy as np

'''Ejercicio de codificación 11
Horas de estudio y calificaciones
Crear una función en Python utilizando matplotlib que grafique la relación entre las horas de estudio y las calificaciones obtenidas por los estudiantes, con el objetivo de visualizar la tendencia de cómo las calificaciones aumentan a medida que aumentan las horas de estudio.

Instrucciones:
Crear la función graficar_linea:
Define una función llamada graficar_linea que reciba dos listas:
x: una lista que contenga los valores de las horas de estudio.
y: una lista que contenga las calificaciones obtenidas.
La función debe utilizar la librería matplotlib.pyplot para graficar una línea que conecte los puntos (x, y) en un gráfico de dispersión.
La gráfica debe incluir:
Un título: "Relación entre horas de estudio y calificaciones".
Etiquetas en los ejes:
El eje X debe estar etiquetado como "Horas de Estudio".
El eje Y debe estar etiquetado como "Calificación".
Datos de entrada: A continuación se proporcionan los datos que debes usar para graficar la relación entre las horas de estudio y las calificaciones.
Horas de estudio (x):
[1, 2, 3, 4, 5, 6, 7, 8]
Calificaciones (y):
[55, 60, 65, 70, 75, 80, 85, 90]
Requisitos:
Usa la librería matplotlib para crear la gráfica.
La gráfica debe ser una línea que conecte los puntos (x, y).
Al ejecutar la función, debe aparecer una ventana con la gráfica generada.
Asegúrate de que los ejes X e Y estén correctamente etiquetados y que el gráfico tenga el título especificado.
Prueba:
Llama a la función graficar_linea con los datos proporcionados y asegúrate de que la gráfica se muestre correctamente.
'''

def graficar_linea(x, y):
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title("Relación entre horas de estudio y calificaciones")
    plt.xlabel("Horas de Estudio")
    plt.ylabel("Calificación")

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [55, 60, 65, 70, 75, 80, 85, 90]

graficar_linea(x, y)
plt.show()

'''Ejercicio de codificación 12
Temperaturas semanales
Crear una función que reciba una lista de temperaturas diarias y los días de la semana correspondientes, y genere un gráfico de líneas utilizando Matplotlib. El gráfico debe visualizar las temperaturas a lo largo de la semana.
Requisitos:
Función a crear:
La función debe recibir dos listas:
dias: Una lista de los días de la semana (por ejemplo, ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']).
temperaturas: Una lista de las temperaturas correspondientes a cada día de la semana (por ejemplo, [22, 24, 23, 25, 26, 28, 27]).
Gráfico:
Utilizar Matplotlib para graficar las temperaturas.
El gráfico debe tener los días de la semana en el eje X y las temperaturas en el eje Y.
Configurar el título del gráfico como "Temperaturas Semanales".
El gráfico debe tener etiquetas en los ejes (por ejemplo, "Días" en el eje X y "Temperatura (°C)" en el eje Y).
Personalizar el gráfico cambiando el color de la línea a azul y utilizando un estilo de línea dashed (discontinua).
Opcional:
Añadir una leyenda al gráfico que indique "Temperatura".
Modificar el tamaño del gráfico (por ejemplo, hacerlo más grande).
Ejemplo de Entrada y Salida:
Entrada:
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temperaturas = [22, 24, 23, 25, 26, 28, 27]
Salida:
Un gráfico que muestra las temperaturas a lo largo de la semana, con líneas discontinuas azules y el título "Temperaturas Semanales".
'''

def graficar_temperaturas(dias, temperaturas):
    plt.figure()
    plt.plot(dias, temperaturas, color='blue', linestyle='--', label='Temperatura')
    plt.title("Temperaturas Semanales")
    plt.xlabel("Días")
    plt.ylabel("Temperatura (°C)")
    plt.legend()

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temperaturas = [22, 24, 23, 25, 26, 28, 27]

graficar_temperaturas(dias, temperaturas)
plt.show()