import pandas as pd

# Pandas: Tratar ficheros Excel, formato CSV
# Es necesario installar openpyxl ( pip install openpyxl ). Biblioteca especializada para leer formato XLSX
# pwd => Comando en la terminal Bash para ver la carpeta en la que estamos
# ls => Comando en la terminal Bash para listar los archivos de la carpeta en la que estamos

# Leer el fichero Excel desde un dataframe
dataframe = pd.read_excel('Ejemplo_excel.xlsx')
print('El contenido del dataframe generado con el archivo Excel es:')
print(dataframe, '\n')

# Añadir una nueva columna
dataframe['e'] = [20, 21, 22, 23]
print('El dataframe con la columna "e" añadida es:')
print(dataframe, '\n')

# Para guardar esto en otro fichero de excel
dataframe.to_excel('salida_excel.xlsx', sheet_name='Hoja1') # sheet_name es el atributo para definir el nombre de la hoja del archivo excel
