# Clase Conexion. Gestiona las conexiones con la base de datos MySQl

import configparser
import mysql.connector

from mysql.connector import pooling
from mysql.connector import Error

config = configparser.ConfigParser()  # Crear un objeto ConfigParser

class Conexion:
    # Intentar leer el archivo de configuración dentro de la clase
    try:
        config.read('.config.ini')  # Leer el archivo de configuración
        # Verificar si la sección 'database' existe
        if 'database' not in config:
            raise ValueError("La sección 'database' no se encuentra en config.ini")

        # Obtener los datos de la sección 'database'
        db_config = {
            "host": config['database']['host'],
            "user": config['database']['user'],
            "password": config['database']['password'],
            "database": config['database']['database'],
            "db_port": config['database']['db_port'],
            "pool_size": config['database']['pool_size'],
            "pool_name": config['database']['pool_name'],
            "pool": config['database']['pool']
        }
        
        # Asignar los valores a atributos de clase
        host = db_config["host"]
        user = db_config["user"]
        password = db_config["password"]
        database = db_config["database"]
        port = int(db_config["db_port"])
        pool_size = int(db_config["pool_size"])
        pool_name = db_config["pool_name"]
        pool = None # Inicializar pool como None
    
    except FileNotFoundError:
        print("Error: El archivo config.ini no se encontró.")
        exit()
    except KeyError as e:
        print(f"Error: Falta la clave '{e}' en la sección 'database' de config.ini.")
        exit()
    except ValueError as e:
        print(f"Error: {e}")
        exit()
    except Exception as e:
        print(f"Error inesperado al leer config.ini: {e}")
        exit()
    
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.pool_name,
                    pool_size=cls.pool_size,
                    host=cls.host,
                    port=cls.port,
                    database=cls.database,
                    user=cls.user,
                    password=cls.password,
                )
                return cls.pool
            except Error as e:
                print(f'Error al crear el pool: {e}')
                return None # Retornar None en caso de error
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        pool = cls.obtener_pool()
        if pool:
            try:
                return pool.get_connection()
            except Error as e:
                print(f"Error al obtener la conexión del pool: {e}")
                return None
        else:
            return None

    @classmethod
    def obtener_cursor(cls):
        conexion = cls.obtener_conexion()
        if conexion:
            return conexion.cursor()
        else:
            return None

    @classmethod
    def liberar_conexion(cls, conexion):
        if conexion:
            conexion.close()

if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    if pool:
        print(pool)
        conexion1 = pool.get_connection()
        print(conexion1)
        conexion2 = pool.get_connection()
        print(conexion2)
        conexion3 = pool.get_connection()
        print(conexion3)
        conexion4 = pool.get_connection()
        print(conexion4)
        conexion5 = pool.get_connection()
        print(conexion5)
        Conexion.liberar_conexion(conexion1)
        print(f'Se ha liberado el objeto conexion1')
        Conexion.liberar_conexion(conexion2)
        print(f'Se ha liberado el objeto conexion2')
        Conexion.liberar_conexion(conexion3)
        print(f'Se ha liberado el objeto conexion3')
        Conexion.liberar_conexion(conexion4)
        print(f'Se ha liberado el objeto conexion4')
        Conexion.liberar_conexion(conexion5)
        print(f'Se ha liberado el objeto conexion5')
    else:
        print("No se pudo crear el pool")