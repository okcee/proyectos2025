import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from plotly.offline import plot
import plotly.graph_objects as go

# Configurar Plotly y Cufflinks - visualizaciones interactivas
# init_notebook_mode(connected=True) # Configurar notebook
# cf.go_offline()
# Cufflinks está obsoleto
'''
%mathplotlib inline # Para poder visualizar los libros dentro del notebook en jupyter Notebook

En VS Code, cuando utilizas Matplotlib (o librerías basadas en él como Seaborn o Plotly con Cufflinks), los gráficos generalmente se muestran en una ventana de visualización de gráficos separada después de llamar a plt.show() (para Matplotlib y Seaborn) o fig.show()/iplot() (para Plotly).
'''

# Crear un DataFrame aleatorio
dataframe = pd.DataFrame(np.random.randn(100,4), columns=['a', 'b', 'c', 'd']) # Dataframe [100 rows x 4 columns],de 100 filas x 4 columnas
# print(dataframe)

# Crear un gráfico con Plotly
# Definir los trazados (traces) a partir del DataFrame
trace1 = go.Scatter(x=dataframe.index, y=dataframe['a'], mode='lines', name='Columna A')
trace2 = go.Scatter(x=dataframe.index, y=dataframe['b'], mode='lines', name='Columna B')

# Definir el diseño (layout)
layout = go.Layout(title='Gráfico interactivo con Plotly', xaxis=dict(title='Índice'), yaxis=dict(title='Valores'))

# Crear la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Guardar y mostrar el gráfico
plot(fig, filename='plotly_test.html', auto_open=True)

'''
Otros tipo de gráficos:

Tipo Scatter:   dataframe.iplot(kind='scatter', x=a, y=b, mode='marker')
Diagrama de tipo bar:   dataframe.iplot(kind='bar')
Diagrama de tipo bar sumando dos columnas:  dataframe.sum().iplot(kind='bar')
Diagrama de caja:   dataframe.iplot(kind='box')
Diagrama de tipo histograma:    dataframe.iplot(kind='hist', bins=30)
Diagrama de tipo spread sobre dos columnas:     dataframe[['a','b']].iplot(kind='spread')
Diagrama de tipo bubble: dataframe.iplot(kind='bubble', x='a', y='b', size='c')
'''

# Gráfico en 3D, tres dimensiones
dataframe2 = pd.DataFrame({'a':[1,2,3,4], 'b':[30,40,20,10], 'c':[12,16,18,15]})
# print(dataframe2)

fig = go.Figure(data=[go.Surface(z=dataframe2.values)])

# Puedes intentar personalizar los títulos de los ejes aquí si lo deseas
fig.update_layout(scene=dict(
    xaxis_title="Eje a",
    yaxis_title="Eje b",
    zaxis_title="Eje c",
))

plot(fig, filename='superficie_3D.html', auto_open=True)