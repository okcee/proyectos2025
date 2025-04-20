# Clase Conexion. Gestiona las conexiones con la base de datos MySQl

import configparser
from mysql.connector import pooling
from mysql.connector import Error
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) # Obtener la ruta absoluta del directorio donde se encuentra este script (conexion.py)
config_path = os.path.join(script_dir, '.config.ini') # Construir la ruta completa al archivo .config.ini

config = configparser.ConfigParser()

class Conexion:
    _pool = None

    try:
        archivos_leidos = config.read(config_path)
        if not archivos_leidos:
            # Si config.read no encontró o no pudo leer el archivo, lanza un error
            raise FileNotFoundError(f"No se pudo encontrar o leer el archivo de configuración en: {config_path}")

        if 'database' not in config:
            # Este error ahora significa que el archivo se leyó, pero no tiene la sección [database]
            raise ValueError(f"La sección [database] no se encuentra en {config_path}")

        db_config = {
            "host": config['database']['host'],
            "user": config['database']['user'],
            "password": config['database']['password'],
            "database": config['database']['database'],
            "db_port": config['database']['db_port'],
            "pool_size": config['database']['pool_size'],
            "pool_name": config['database']['pool_name']
        }

        host = db_config["host"]
        user = db_config["user"]
        password = db_config["password"]
        database = db_config["database"]
        port = int(db_config["db_port"])
        pool_size = int(db_config["pool_size"])
        pool_name = db_config["pool_name"]

    except FileNotFoundError:
        print("Error: El archivo .config.ini no se encontró en la ubicación esperada.")
        exit()
    except KeyError as e:
        print(f"Error: Falta la clave '{e}' en la sección 'database' de .config.ini.")
        exit()
    except ValueError as e:
        print(f"Error: {e}")
        exit()
    except Exception as e:
        print(f"Error inesperado al leer .config.ini: {e}")
        exit()

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name=cls.pool_name,
                    pool_size=cls.pool_size,
                    host=cls.host,
                    port=cls.port,
                    database=cls.database,
                    user=cls.user,
                    password=cls.password
                )
                print(f"Pool '{cls.pool_name}' creado exitosamente.") # Feedback
                return cls._pool
            except Error as e:
                print(f'Error al crear el pool: {e}')
                cls._pool = None # Asegurar que siga None si falla
                return None
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        pool = cls.obtener_pool()
        conexion = None # Inicializar
        if pool:
            try:
                conexion = pool.get_connection()
                # print("Conexión obtenida del pool.") # Descomentar para depurar
                return conexion
            except Error as e:
                print(f"Error al obtener la conexión del pool: {e}")
                if conexion: # Si se obtuvo parcialmente antes del error
                    conexion.close()
                return None
        else:
            print("Error: Pool no disponible.")
            return None

    @classmethod
    def liberar_conexion(cls, conexion):
        if conexion:
            try:
                conexion.close()
                # print("Conexión liberada al pool.") # Descomentar para depurar
            except Error as e:
                print(f"Error al liberar la conexión: {e}")

# Bloque de prueba
if __name__ == '__main__':
    pool = Conexion.obtener_pool()
    if pool:
        print(f"Pool obtenido: {pool}")
        conexiones = []
        for i in range(Conexion.pool_size): # Intentar obtener hasta el tamaño del pool
            print(f"Intentando obtener conexión {i+1}...")
            conn = Conexion.obtener_conexion()
            if conn:
                print(f"Conexión {i+1} obtenida: {conn.connection_id}")
                conexiones.append(conn)
            else:
                print(f"Fallo al obtener conexión {i+1}")
                break

        print("\nLiberando conexiones...")
        for i, conn in enumerate(conexiones):
            Conexion.liberar_conexion(conn)
            print(f'Se ha liberado el objeto conexion {i+1} (ID: {conn.connection_id})')
    else:
        print("No se pudo crear u obtener el pool")
