
import pandas as pd
import numpy as np
import cufflinks as cf

from matplotlib import pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Plotly y Cufflinks - visualizaciones interactivas

init_notebook_mode(connected=True) # Configurar notebook
cf.go_offline()

'''
%mathplotlib inline # Para poder visualizar los libros dentro del notebook en jupyter Notebook

En VS Code, cuando utilizas Matplotlib (o librerías basadas en él como Seaborn o Plotly con Cufflinks), los gráficos generalmente se muestran en una ventana de visualización de gráficos separada después de llamar a plt.show() (para Matplotlib y Seaborn) o fig.show()/iplot() (para Plotly).
'''

dataframe = pd.DataFrame(np.random.randn(100,4), columns=['a', 'b', 'c', 'd']) # Dataframe [100 rows x 4 columns],de 100 filas x 4 columnas
# print(dataframe)

# Sobre el dataframe crearemos los gráficos
dataframe.plot()
# plt.show()
plt.close()

dataframe.iplot(color='gold')
plt.show()
plt.close()