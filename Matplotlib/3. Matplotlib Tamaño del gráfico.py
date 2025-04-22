import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np

# Matplotlib: Multigráficos(filas, columnas)
# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
# print('La listas de valores son:')
# print('La lista "x" es:', x)
# print('La lista "y" es:', y)

# Como definir el tamaño de una figura y, de un gráfico dentro de una figura

figura = plt.figure(figsize=(12,6)) # figsize es el ancho y el alto en pulgadas de la figura
grafico = figura.add_axes([0.1,0.1,0.9,0.8]) # separación izquierda, separación derecha, porcentaje sobre uno del ancho y porcentaje sobre uno del alto
grafico.plot(x,y,'r') # Sobre este gráfico vamos a mostrar los valores x e y de color rojo(red)
grafico.set_title('Definiendo tamaños', fontsize=12)
# plt.tight_layout() # Ajusta los márgenes
# plt.subplots_adjust(top=0.8)  # Ajusta el margen superior
# plt.savefig('grafico_Definiendo_tamaños.png') # Crea una imagen formato PNG del gráfico
figura.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.8) # Ajustar márgenes de la figura
plt.show()