from matplotlib import pyplot as plt
import seaborn as sns

propinas = sns.load_dataset('tips')
# propinas.head()
# print(propinas.head())
''' Dataset
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''

# Seaborn: Gráficos de regresión (Regression Plots)
# Gráfico lm
sns.lmplot(x='total_bill', y='tip', data=propinas)
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()
# Misma gráfica con un atributo más, que distingue los datos según el género
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex')
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()
# Misma gráfica con marcadores distintos
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex', markers=['o','v'])
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()
# Modificar el tamaño de los marcadores
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex', markers=['o','v'], scatter_kws={'s':80})
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()

# Gráfico lm, separándolo por columnas
sns.lmplot(x='total_bill', y='tip', data=propinas, col='sex')
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()
sns.lmplot(x='total_bill', y='tip', data=propinas, col='day')
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()
sns.lmplot(x='total_bill', y='tip', data=propinas, col='day', hue='sex')
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()

# Gráfico lm, separándolo por filas
sns.lmplot(x='total_bill', y='tip', data=propinas, row='sex')
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()
sns.lmplot(x='total_bill', y='tip', data=propinas, row='day')
plt.suptitle("Gráfico de regresión", y=0.9)
# plt.show()
plt.close()

# Cambiar el aspecto al gráfico. aspect= ancho, height= tamaño general
sns.lmplot(x='total_bill', y='tip', data=propinas, aspect=2, height=10)
plt.suptitle("Gráfico de regresión")
plt.show()
plt.close()