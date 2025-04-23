# Prueba Plotly

import plotly.offline as py
import plotly.graph_objs as go

py.init_notebook_mode(connected=True)

# Datos de ejemplo
data = [go.Scatter(x=[1, 2, 3, 4, 5], y=[6, 5, 7, 2, 8])]

# Layout de ejemplo (opcional)
layout = go.Layout(title='Gráfico de prueba con Plotly')

# Crear la figura
fig = go.Figure(data=data, layout=layout)

# Guardar la figura como un archivo HTML
py.plot(fig, filename='plotly_test.html', auto_open=True)

# Mostrar la figura (debería abrirse en el navegador)
# py.iplot(fig)