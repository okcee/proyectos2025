import matplotlib.pyplot as plt
import numpy as np

# Matplotlib:Línea del gráfico (Ajustar grosor, transparencia y tipo)
# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
# print('La listas de valores son:')
# print('La lista "x" es:', x)
# print('La lista "y" es:', y)

# El ANCHO de la línea (linewidth)
figura = plt.figure()
grafico = figura.add_axes([0,0,1,1])
grafico.plot(x,y,color='aqua',linewidth=5) # linewidth=5 El ANCHO de la línea
plt.show()
# La TRANSPARENCIA de la línea (alpha)
figura = plt.figure()
grafico = figura.add_axes([0,0,1,1])
grafico.plot(x,y,color='aquamarine',linewidth=5, alpha=0.4) # alpha= La TRANSPARENCIA de la línea (+Transparente < 0.5 < -Transparente) alpha=0.5 es el valor intermedio
plt.show()
# El TIPO de línea (linestyle)
figura = plt.figure()
grafico = figura.add_axes([0,0,1,0.9])
grafico.plot(x,y,color='black',linewidth=5, alpha=1, linestyle=':')
grafico.set_title("linestyle=':'", fontsize=15)
plt.show()

figura = plt.figure()
grafico = figura.add_axes([0,0,1,0.9])
grafico.plot(x,y,color='brown',linewidth=5, alpha=0.8, linestyle='-.')
grafico.set_title("linestyle='-.'", fontsize=15)
plt.show()

figura = plt.figure()
grafico = figura.add_axes([0,0,1,0.9])
grafico.plot(x,y,color='chartreuse',linewidth=5, alpha=0.8, linestyle='--')
grafico.set_title("linestyle='--'", fontsize=15)
plt.show()

figura = plt.figure()
grafico = figura.add_axes([0,0,1,0.9])
grafico.plot(x,y,color='beige',linewidth=10, alpha=0.8, linestyle='-') # Colores beige y azure muy claros
grafico.set_title("linestyle='-'", fontsize=15)
plt.show()