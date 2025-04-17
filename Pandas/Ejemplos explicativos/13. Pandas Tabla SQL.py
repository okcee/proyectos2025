import numpy as np
import pandas as pd

from sqlalchemy import create_engine

# Pandas: Tabla SQL
# Necesitamos instalar sqlalchemy ( pip install sqlalchemy )

diccionario = {'A':[1,2,3], 'B':[4,5,6]}
dataframe = pd.DataFrame(diccionario)
print('El contenido del dataframe es:')
print(dataframe, '\n')

# Ahora vamos a grabar el contenido de este dataframe dentro de una base de datos, en este caso, dentro de una tabla nueva
# Lo haremos en un motor de sql en memoria que vamos a crear de la siguiente forma
engine = create_engine('sqlite:///:memory:') # Creado en memoria un motor de base de datos

dataframe.to_sql('tabla', engine, index=False) # Grabamos el dataframe dentro de una tabla nueva

# Comprobamos la salida de lo hecho
# Leemos los datos sql
datos_leidos_db = pd.read_sql('tabla', con=engine)

print('Los datos de la tabla sql son:')
print(datos_leidos_db, '\n')
