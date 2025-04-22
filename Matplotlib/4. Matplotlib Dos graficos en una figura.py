import matplotlib.pyplot as plt
import numpy as np

# Matplotlib: Crear dos gráficos en la misma figura
# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)

# print('La listas de valores son:')
# print('La lista "x" es:', x)

# Como crear dos gráficos en la misma figura
figura = plt.figure() # Creamos la figura
graficos = figura.add_axes([0.1,0.1,0.9,0.8]) # Añadimos los ejes
graficos.plot(x, x**2 , label='Al cuadrado')
graficos.plot(x, x**3 , label='Al cubo')
graficos.legend(loc=0) # Poner la leyenda de los gráficos en la posición óptima de manera automática
graficos.set_title('Dos gráficos en la misma figura', fontsize=14)
plt.show()