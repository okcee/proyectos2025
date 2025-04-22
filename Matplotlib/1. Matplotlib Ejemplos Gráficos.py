import matplotlib.pyplot as plt
import numpy as np

# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
# print('La listas de valores son:')
# print('La lista "x" es:', x)
# print('La lista "y" es:', y)

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

plt.title("Gráfico 2: Representar dos gráficos en el mismo espacio")
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

plt.title("Gráfico 3: Representar dos gráficos: uno encima del otro")
plt.show()
plt.close()

# Lo mismo con Programación ortientada a objetos

figura = plt.figure() # Crea un objeto tipo figura.
plt.title("Gráfico 4: Representación de X e Y (su cuadrado) con POO")
grafico4 = figura.add_axes([0.1,0.1,0.9,0.8]) # Crea un gráfico dentro de esta figura. Con el método add_axes añade los ejes. Será una lista de valores con el espacio que dejamos por la izquierda, por la derecha y el ancho y el largo.add()
grafico4.plot(x,y,'green')
grafico4.set_title("Gráfico 4: Representación de X e Y (su cuadrado) con POO")
plt.show()

# Representar dos gráficos con POO

figura = plt.figure()

grafico5 = figura.add_subplot([0.1,0.1,0.9,0.8])
grafico5.plot(x,y,'red')
grafico5.set_title("Figura 5: Comparación ajustes de atributos")


grafico6 = figura.add_subplot([0.2,0.5,0.4,0.4]) # Tamaño: Izq, Dcha. 
grafico6.plot(y,x, 'blue')
grafico6.set_title("Figura 6: Comparación ajustes de atributos")

plt.tight_layout() # Ajusta los dos sub-gráficos
plt.show()
