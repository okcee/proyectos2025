from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

propinas = sns.load_dataset('tips') # Cargamos un dataset que viene con la librería para hacer pruebas
print("Los primeros 10 elementos del dataset son: ")
print(propinas.head(10))
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
6        8.77  2.00    Male     No  Sun  Dinner     2
7       26.88  3.12    Male     No  Sun  Dinner     4
8       15.04  1.96    Male     No  Sun  Dinner     2
9       14.78  3.23    Male     No  Sun  Dinner     2
'''

# Seaborn: Gráficos para columnas de tipo categorías
# barplot
sns.barplot(x='sex', y='total_bill', data=propinas)
plt.title("Gráfico de género (masculino o Femenino) en función de las facturas")
plt.show()

# countplot
sns.countplot(x='sex', data=propinas)
plt.title("Gráfico de cantidad de personas según género (masculino o Femenino)")
plt.show()

# boxplot
sns.boxplot(x='day', y='total_bill', data=propinas)
plt.title("Diagrama de caja según día")
plt.show() # Caja según día
sns.boxplot(x='day', y='total_bill', data=propinas, hue='smoker') # Se le añade otro atributo más
plt.title("Diagrama de caja según día y en comparando los no fumadores con los fumadores")
plt.show()

# violinplot
sns.violinplot(x='day', y='total_bill', data=propinas)
plt.title("Diagrama tipo violín factura según el día")
plt.show()
sns.violinplot(x='day', y='total_bill', data=propinas, hue='smoker', split=True) # Se le añade otro atributo más y se juntan
plt.title("Diagrama tipo violín según día y comparando los no fumadores con los fumadores juntado")
plt.show()

# stripplot
sns.violinplot(x='day', y='total_bill', data=propinas)
plt.title("Diagrama tipo strip de puntos de facturación según día")
plt.show()
sns.violinplot(x='day', y='total_bill', data=propinas, hue='sex')
plt.title("Diagrama tipo strip de puntos de facturación según día comparado por sexo")
plt.show()

# swarmplot Gráfico de puntos, pero distribuídos para que no se solapen
sns.swarmplot(x='day', y='total_bill', data=propinas)
plt.title("Diagrama tipo swarm de puntos de facturación según día")
plt.show()
sns.swarmplot(x='day', y='total_bill', data=propinas, hue='sex')
plt.title("Diagrama tipo swarm de puntos de facturación según día comparado por sexo")
plt.show()

# Juntar dos gráficos en una figura
sns.violinplot(x='day', y='total_bill', data=propinas)
sns.swarmplot(x='day', y='total_bill', data=propinas)
plt.title("Dos diagramas juntos")
plt.show()