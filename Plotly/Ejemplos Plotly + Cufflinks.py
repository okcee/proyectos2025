import pandas as pd
import numpy as np
import cufflinks as cf
from matplotlib import pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objects as go

# Configurar Plotly y Cufflinks - visualizaciones interactivas
init_notebook_mode(connected=True) # Configurar notebook
cf.go_offline()

'''
%mathplotlib inline # Para poder visualizar los libros dentro del notebook en jupyter Notebook

En VS Code, cuando utilizas Matplotlib (o librerías basadas en él como Seaborn o Plotly con Cufflinks), los gráficos generalmente se muestran en una ventana de visualización de gráficos separada después de llamar a plt.show() (para Matplotlib y Seaborn) o fig.show()/iplot() (para Plotly).
'''
# Crear un DataFrame aleatorio
dataframe = pd.DataFrame(np.random.randn(100,4), columns=['a', 'b', 'c', 'd']) # Dataframe [100 rows x 4 columns],de 100 filas x 4 columnas
# print(dataframe)

# Sobre el dataframe crearemos el gráfico interactivo mediante Cufflinks
# dataframe.plot()
# plt.show()
# plt.close()

# Crear un gráfico interactivo con Cufflinks
# dataframe.iplot()

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