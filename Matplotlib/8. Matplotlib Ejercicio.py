''' Ejercicio 1
Crear una variable "x" que tenga 10 valores equidistantes entre los valores 0 y 20
Crear una variable "y" que tenga los valores de la función "x al cuadrado + 5"
Crear un gráfico de color rojo con ancho de 5 y estilo de puntos "...."
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, num=10)
y = (x**2)+5

figura = plt.figure()
grafico = figura.add_axes([0,0,1,0.9])
grafico.plot(x,y,color='red',linewidth=5, linestyle=':')
grafico.set_title("Ejercicio 1 de gráficos Matplotlib", fontsize=14)
plt.show()