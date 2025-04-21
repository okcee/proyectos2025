import matplotlib.pyplot as plt
import numpy as np

# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
print('La listas de valores son:')
print('La lista "x" es:', x)
print('La lista "y" es:', y)

# Representar las listas mediante un gráfico
plt.plot(x,y, 'red') # define la gráfica  y tiene atributo color rojo para la línea
plt.title("Gráfico 1: Representación de X y su cuadrado") # Ponerle un título
plt.xlabel("Eje x") # Nombre para la primera lista de valores Eje x.
plt.ylabel("Eje y") # Nombre para la segunda lista de valores. Eje y.
plt.show()
plt.close()

# Representar dos gráficos en el mismo espacio
plt.subplot(1,2,1) # Atributos: Número de filas, Número de columnas y Posición
plt.plot(x,y, 'green')
plt.xlabel("Eje x") # Nombre para la primera lista de valores Eje x.
plt.ylabel("Eje y") # Nombre para la segunda lista de valores. Eje y.

plt.subplot(1,2,2)
plt.plot(y,x, 'blue')
plt.xlabel("Eje x") # Nombre para la primera lista de valores Eje x.
plt.ylabel("Eje y") # Nombre para la segunda lista de valores. Eje y.

plt.show()
plt.close()

# Representar dos gráficos: uno encima del otro
plt.subplot(2,1,1) # Atributos: Número de filas, Número de columnas y Posición
plt.plot(x,y, 'pink')
plt.xlabel("Eje x") # Nombre para la primera lista de valores Eje x.
plt.ylabel("Eje y") # Nombre para la segunda lista de valores. Eje y.

plt.subplot(2,1,2)
plt.plot(y,x, 'violet')
plt.xlabel("Eje x") # Nombre para la primera lista de valores Eje x.
plt.ylabel("Eje y") # Nombre para la segunda lista de valores. Eje y.

plt.show()
plt.close()

# 