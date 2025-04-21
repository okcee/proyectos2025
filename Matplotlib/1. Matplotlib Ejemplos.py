import matplotlib.pyplot as plt
import numpy as np

# Hacemos una lista de valores mediante numpy con el método lonspace
x = np.linspace(2,9,10)
y = x**2
print('La listas de valores son:')
print('La lista "x" es:', x)
print('La lista "y" es:', y)

# Representar las listas mediante un gráfico

plt.plot(x,y)
