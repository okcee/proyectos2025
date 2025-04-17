import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pandas: Crear gráficos directamente desde un dataframe
# Necesario intalar matplotlib: ( pip install matplotlib )
# El comando plt.show() , muestra un gráfico después de generarlo

dataframe = pd.DataFrame(np.random.randint(200, size=(50,4)), columns=['a','b','c','d'])
print('El dataframe es:')
print(dataframe, '\n')

# Vamos a utilizar este dataframe para crear los gráficos
# Método hist()
# Gráfico de la columna "a"
print('Histograma de los valores de la columna "a"')
dataframe['a'].hist() # Histograma de los valores de la columna a
plt.title("Histograma Columna 'a'") # Añadir título (opcional)
plt.xlabel("Valor")               # Añadir etiqueta eje X (opcional)
plt.ylabel("Frecuencia")          # Añadir etiqueta eje Y (opcional)
plt.show()                        # Método para que matplotlib muestre los gráficos generados anteriormente

# Gráfico de la columna "b", podemos cambiar el número de columnas con el método bins (30 bins = 30 columnas)
print('Histograma de los valores de la columna "b"')
dataframe['b'].hist(bins=30) # Histograma de los valores de la columna a
plt.title("Histograma Columna 'b' (30 bins)")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Método plot.hist()
print('Histograma de los valores de la columna "a"')
dataframe['a'].plot.hist()
plt.title("Histograma Columna 'a' (plot.hist)")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de tipo área, método plot.area()
print('Gráfico de área con los valores de las columna "a", "b", "c" y "d"')
dataframe.plot.area(alpha=0.5) # alpha=0.5 para hacer más transparentes los colores del gráfico
plt.title("Gráfico de área")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de barras, método plot.areabar()
print('Gráfico de barras con los valores de las columna "a", "b", "c" y "d"')
dataframe.plot.bar(stacked=True) # stacked=True Acumula los valores para que no se vean las barras apretujadas
plt.title("Gráfico de barras")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de tipo scatter, método plot.scatter()
print('Gráfico de área con los valores de las columna "a", "b" y "c"')
dataframe.plot.scatter(x='a', y='b', c='c', cmap='coolwarm') # cmap='coolwarm' Añade una paleta de colores para diferenciar mejor los puntos a, b o c
plt.title("Gráfico de área")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Diagrama de caja
print('Diagrama de caja con los valores de las columna "a", "b", "c" y "d"')
dataframe.plot.box() # stacked=True Acumula los valores para que no se vean las barras apretujadas
plt.title("Diagrama de caja")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de tipo hexadecimal, método plot.hexbin()
print('Gráfico de área con los valores de las columna "a" y "b"')
dataframe.plot.hexbin(x='a', y='b', gridsize=12) # gridsize=12 Tamaño de la rejilla
plt.title("Gráfico de área")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico KDE, método .plot.kde() o .plot.density()
print('Gráfico KDE con los valores de las columna "a", "b", "c" y "d"')
dataframe.plot.kde() # stacked=True Acumula los valores para que no se vean las barras apretujadas
plt.title("Gráfico KDE")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
