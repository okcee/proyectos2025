import configparser

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

# Leer un archivo de configuración ficticio
config.read_string("""
[seccion_ejemplo]
clave = valor
""")

# Imprimir el contenido de la sección
print(config.sections())  # Debería imprimir: ['seccion_ejemplo']
print(config['seccion_ejemplo']['clave'])  # Debería imprimir: valor