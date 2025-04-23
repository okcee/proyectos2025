# El siguiente código genera un gráfico interactivo y lo guarda como un archivo HTML. Luego, abre automáticamente el archivo en tu navegador predeterminado (Brave).

import pandas as pd
import numpy as np
import cufflinks as cf
from plotly.offline import plot
import plotly.graph_objects as go

# Configurar Plotly y Cufflinks para trabajar offline
cf.go_offline()

# Crear un DataFrame aleatorio
dataframe = pd.DataFrame(np.random.randn(100, 4), columns=['a', 'b', 'c', 'd'])

# Crear trazados (traces) para Plotly
trace1 = go.Scatter(x=dataframe.index, y=dataframe['a'], mode='lines', name='Columna A')
trace2 = go.Scatter(x=dataframe.index, y=dataframe['b'], mode='lines', name='Columna B')

# Definir el diseño (layout)
layout = go.Layout(
    title='Gráfico interactivo con Plotly',
    xaxis=dict(title='Índice'),
    yaxis=dict(title='Valores')
)

# Crear la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Guardar el gráfico como un archivo HTML y abrirlo en el navegador predeterminado
# Por defecto, se guardará en el mismo directorio donde se encuentra tu script Python
plot(fig, filename='grafico_interactivo.html', auto_open=True)
# Se puede especificar la ruta donde guardar el archivo "S:\_proyectos2025\Plotly\grafico_interactivo.html"
# plot(fig, filename='C:/ruta/completa/grafico_interactivo.html', auto_open=True)

'''
3. Explicación del código
cf.go_offline() : Configura Cufflinks y Plotly para trabajar en modo offline.
go.Scatter : Crea los trazados (líneas) para el gráfico.
go.Layout : Define el diseño del gráfico (título, etiquetas de ejes, etc.).
plot(fig, filename='grafico_interactivo.html', auto_open=True) :
Guarda el gráfico en un archivo HTML (grafico_interactivo.html).
Abre automáticamente el archivo en tu navegador predeterminado (en este caso, Brave).
'''
'''
Explicación del código
cf.go_offline() : Configura Cufflinks y Plotly para trabajar en modo offline.
go.Scatter : Crea los trazados (líneas) para el gráfico.
go.Layout : Define el diseño del gráfico (título, etiquetas de ejes, etc.).
plot(fig, filename='grafico_interactivo.html', auto_open=True) :
Guarda el gráfico en un archivo HTML (grafico_interactivo.html).
Abre automáticamente el archivo en tu navegador predeterminado (en este caso, Brave).
'''
'''
¿Dónde se guarda el archivo HTML?
El archivo grafico_interactivo.html se guardará en el mismo directorio donde se encuentra tu script Python. Si quieres guardarlo en una ubicación específica, puedes proporcionar la ruta completa al parámetro filename. Por ejemplo:
plot(fig, filename='C:/ruta/completa/grafico_interactivo.html', auto_open=True)
'''
'''
Abrir el archivo manualmente (opcional)
Si por alguna razón el archivo no se abre automáticamente en Brave, puedes abrirlo manualmente:
Navega al directorio donde se guardó el archivo HTML.
Haz doble clic en el archivo grafico_interactivo.html.
El archivo se abrirá en tu navegador predeterminado (Brave).
'''
'''
Resultado esperado
Cuando ejecutes el script en VS Code:
Se generará un archivo HTML llamado grafico_interactivo.html.
El archivo se abrirá automáticamente en Brave, mostrando el gráfico interactivo.
Podrás interactuar con el gráfico (hacer zoom, moverlo, ocultar/mostrar trazados, etc.).
'''