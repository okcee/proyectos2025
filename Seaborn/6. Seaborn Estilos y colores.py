import seaborn as sns
import matplotlib.pyplot as plt

propinas = sns.load_dataset('tips')
# print(propinas.head())
''' Dataset
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''
# Generamos un gráfico que cuenta el número de ocurrencias de la categoría sex
# Para cambiar el estilo, añadimos el set_style delante de la creación del gráfico
sns.set_style('darkgrid') # Estilo general del plot
sns.countplot(x='sex', data=propinas) # Se crea el gráfico
plt.suptitle("Estilo cambiado")
# plt.show()
plt.close()

# Para que no se vean  las líneas de los ejes
plt.figure(figsize=[12,4])
sns.set_style('white') # Estilo general del plot blanco
sns.countplot(x='sex', data=propinas) # Se crea el gráfico
sns.despine(left=True, bottom=True) # Se eliminan las líneas de los ejes
plt.suptitle("Ocultar líneas")
# plt.show()
plt.close()

# Para cambiar el tamaño de las letras
sns.set_context('notebook', font_scale=1.3) # Estilo de letras y tamaño
plt.figure(figsize=[12,4])
sns.set_style('white') # Estilo general del plot blanco
sns.countplot(x='sex', data=propinas) # Se crea el gráfico
sns.despine(left=True, bottom=True) # Se eliminan las líneas de los ejes
plt.suptitle("Ajustes de las letras")
# plt.show()
plt.close()

# Cambiar los colores
# Paletas d colores ( https://seaborn.pydata.org/tutorial/color_palettes.html )
sns.countplot(x='sex', data=propinas, palette='Set2') # Selección de una paleta de colores
plt.suptitle("Colores cambiados: Paleta")
# plt.show()
plt.close()

# Definir los colores manualmente
# Creamos una variable con los colores
colores = ['lightgreen', 'blue']
colores2 = ['#149fab', '#638a19']
sns.countplot(x='sex', data=propinas, palette=colores2)
plt.suptitle("Colores cambiados: Definidos")
plt.show()
plt.close()