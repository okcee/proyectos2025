import matplotlib.pyplot as plt
import numpy as np

# Matplotlib: Marcadores
# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
# print('La listas de valores son:')
# print('La lista "x" es:', x)
# print('La lista "y" es:', y)

# Lista de tipos de marcadores ( https://matplotlib.org/3.1.0/api/markers_api.html )

# Marcadores de los puntos donte se unen las coordenadas del eje x con el eje y
figura = plt.figure() # Creamos la figura
graficos = figura.add_axes([0,0,1,0.88]) # Añadimos los ejes
# marker='o', tipo de marcador
# markersize=5, tamaño del marcador
graficos.plot(x, y , color='chocolate', marker='o', markersize=5)
graficos.set_title('Ejemplo de marcadores en los gráficos', fontsize=14)
plt.show()