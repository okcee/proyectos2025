import matplotlib.pyplot as plt
import numpy as np

# Matplotlib: Ajustar color del Gráfico
# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
# print('La listas de valores son:')
# print('La lista "x" es:', x)
# print('La lista "y" es:', y)

# Color del Gráfico (Paleta de colores en: https://matplotlib.org/users/colors.html)
# Los Códigos hexadecimales RGB son también válidos ( https://htmlcolorcodes.com/es/ )
figura = plt.figure() # Creamos la figura
graficos = figura.add_axes([0,0,1,1]) # Añadimos los ejes
graficos.plot(x, y, color='tomato') # Se puede omitir color= y poner directamente 'tomato'
plt.show()

figura = plt.figure()
graficos = figura.add_axes([0,0,1,1])
graficos.plot(2*x, y, '#3e7a4e')
plt.show()