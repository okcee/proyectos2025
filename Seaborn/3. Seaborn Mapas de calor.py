from matplotlib import pyplot as plt
import seaborn as sns

vuelos = sns.load_dataset('flights') # Cargamos un dataset que viene con la librería para hacer pruebas
print("Los primeros 10 elementos del dataset son: ")
print(vuelos.head(10))
''' Dataset
   year month  passengers
0  1949   Jan         112
1  1949   Feb         118
2  1949   Mar         132
3  1949   Apr         129
4  1949   May         121
5  1949   Jun         135
6  1949   Jul         148
7  1949   Aug         148
8  1949   Sep         136
9  1949   Oct         119
'''

# Seaborn: Mapas de calor (Heatmaps)
# Para crear un heatmap tenemos que tener la tabla en formato matrix
# Lo haremos mediante la función pivot_table

vuelos_matrix = vuelos.pivot_table(index='month', columns='year', values='passengers')
print(vuelos_matrix)

# Creamos el mapa de calor
heatmap = sns.heatmap(vuelos_matrix)
heatmap.set_title("Gráfico de calor pasajeros por mes y año")
plt.show()
# Añadimos atributo color "cmap": Opciones: viridis, plasma, inferno, magma, coolwarm
heatmap = sns.heatmap(vuelos_matrix, cmap='viridis')
heatmap.set_title("Gráfico de calor pasajeros por mes y año color 2")
plt.show()
# Añadimos atributos para las líneas que separan los cuadrados
# linecolor= color de las líneas de separación de los cuadrados
# linewidths= ancho de las líneas de separación de los cuadrados
heatmap = sns.heatmap(vuelos_matrix, cmap='coolwarm', linecolor='white', linewidths=2)
heatmap.set_title("Gráfico de calor pasajeros por mes y año con líneas diferenciadas")
plt.show()