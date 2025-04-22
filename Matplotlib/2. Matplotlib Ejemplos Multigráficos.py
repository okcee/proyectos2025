import matplotlib.pyplot as plt
import numpy as np

# Matplotlib: Multigráficos(filas, columnas)
# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
# print('La listas de valores son:')
# print('La lista "x" es:', x)
# print('La lista "y" es:', y)

# Vamos a contruír un multigráfico de 4 subgráfico, organizado de 2 filas y 2 columnas
figura, graficos = plt.subplots(nrows=2,ncols=2) # Se ordenan como los arrays(listas)
graficos[0][0].plot(x,y,'blue')
graficos[0][1].plot(x,y,'red')
graficos[1][0].plot(x,y,'yellow')
graficos[1][1].plot(x,y,'green')

graficos[0][0].set_title('Azul')
graficos[0][1].set_title('Rojo')
graficos[1][0].set_title('Amarillo')
graficos[1][1].set_title('Verde')

plt.show()
