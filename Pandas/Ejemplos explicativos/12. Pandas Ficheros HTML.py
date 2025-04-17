import pandas as pd

# Pandas: Ficheros HTML
# Necesitamos instalar lxml ( pip install lxml )
# Vamos a obtener los datos de una tabla de un enlace web para un dataframe, para poder trabajar con ellos

pagina_web = 'https://es.wikipedia.org/wiki/Anexo:Comunidades_y_ciudades_aut%C3%B3nomas_de_Espa%C3%B1a'

datos = pd.read_html(pagina_web) # Función para leer los datos de una página web
print(type(datos))

print(datos[0]) # visualizamos datos

dataframe = datos[0] # Pasamos los datos a un dataframe

print('Visualizamos los 10 primeros datos de la tabala')
print(dataframe.head(10), '\n')
