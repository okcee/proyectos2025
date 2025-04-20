# Clase GestionInventario. Implementa operaciones CRUD (Create, Read, Update, Delete)
''' 
Se usará para las operaciones CRUD:
Patrón de diseño DAO
DAO = Data Accesss Object
Este patrón se utiliza para acceder a la información de una entidad de nuestra aplicación.
En este caso a través del cliente DAO vamos a acceder a la información de la tabla cliente y poder mediante métodos de la clase Cliente DAO, interactuar con la clase Cliente para ejecutar sentencias en la tabla cliente
Esta forma de relacionar los datos es el principio de aplicaciones que se conocen como ORM (Object Relational Mappin), o también de mapeo relación entidad
'''
import sqlite3

from conexion import Conexion
from producto import Producto
from mysql.connector import Error # Importar Error para manejo específico


class GestionInventario:
    CREATE = 'INSERT * FROM producto ORDER BY nombre' # Define una constante con la consulta SQL para seleccionar todos los registros de la tabla 'inventario' ordenados por 'nombre'.
    READ = 'SELECT * FROM producto ORDER BY nombre'  # Define una constante con la consulta SQL para seleccionar todos los registros de la tabla 'producto' ordenados por 'nombre'.
    UPDATE = 'UPDATE producto SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE nombre==%s'  # Define una constante con la consulta SQL para actualizar un registro existente en la tabla 'inventario'.
    DELETE = 'DELETE FROM producto WHERE nombre=%s'  # Define una constante con la consulta SQL para eliminar un registro de la tabla 'inventario' por su 'nombre'.
    FIND = "SELECT id, nombre, cantidad, precio, categoria FROM producto WHERE nombre = %s"
    
    @classmethod
    def create(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(cls.CREATE, valores) # Ejecuta la consulta SQL definida en el atributo constante 'CREATE'.
            conexion.commit() # Confirma la subida los cambios en la base de datos.
            return cursor.rowcount # Está variable indica cuatos datos se modificaron en la base de datos
        except Exception as e:
            print(f'Ocurrió un error al insertar el prodcuto: {e}')
        finally: # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el métod'liberar_conexion' de la clase 'Conexion'.
    
    @classmethod
    def read(cls):
        conexion = None  # Inicializa la variable 'conexion' a 'None' para almacenar la conexión a la base de datos.
        try:  # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion()  # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor()  # Crea un objeto cursor para ejecutar consultas SQL.
            cursor.execute(cls.READ)  # Ejecuta la consulta SQL definida en la constante 'READ'.
            registros = cursor.fetchall()  # Obtiene todos los registros resultantes de la consulta y los almacena en 'registros'.
            # Mapeo de clase-tabla producto
            productos = []  # Inicializa una lista vacía llamada 'productos' para almacenar los objetos 'Producto'.
            for registro in registros:  # Itera sobre cada registro obtenido de la base de datos.
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])  # Crea un objeto 'Producto' con los datos del registro.
                productos.append(producto)  # Añade el objeto 'Producto' a la lista 'productos'.
            return productos  # Retorna la lista de objetos 'Producto'.
        except Exception as e:  # Captura cualquier excepción que ocurra dentro del bloque 'try'.
            print(f'Ocurrió un error al seleccionar los productos: {e}')  # Imprime un mensaje de error con la excepción capturada.
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el método 'liberar_conexion' de la clase 'Conexion'.

    @classmethod
    def find_by_name(cls, nombre_buscado: str):
        conexion = None  # Inicializa la variable 'conexion' a 'None' para almacenar la conexión a la base de datos.
        producto_encontrado = None  # Inicializamos a None para controlar si se encontró algo
        cursor = None
        try:  # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion()  # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            if conexion and conexion.is_connected(): # Buena práctica verificar conexión
                cursor = conexion.cursor() # Crea un objeto cursor para ejecutar consultas SQL
                valores = (nombre_buscado,) # Pasar el nombre_buscado como una tupla con un argumento
                cursor.execute(cls.FIND, valores)
                registro = cursor.fetchone() # Usar fetchone() para obtener un solo registro o None
                if registro:
                    # Crear el objeto Producto a partir de la tupla devuelta
                    # Asumiendo el orden: id, nombre, cantidad, precio, categoria
                    producto_encontrado = Producto(id=registro[0], nombre=registro[1], cantidad=registro[2], precio=registro[3], categoria=registro[4])
            else:
                print("Error: No se pudo obtener conexión para buscar por nombre.")
        
        except Error as e:
            print(f'Ocurrió un error de base de datos al buscar el producto: {e}')
        except Exception as e:  # Captura cualquier excepción que ocurra dentro del bloque 'try'.
            print(f'Ocurrió un error al buscar el producto: {e}')  # Imprime un mensaje de error con la excepción capturada.
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el método 'liberar_conexion' de la clase 'Conexion'.
        return producto_encontrado  # Retorna la lista de objetos 'Producto' o None si no lo encuentra.
    
    @classmethod
    def update(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion() # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor() # Crea un objeto cursor para ejecutar consultas SQL.
            valores = (producto.nombre, producto.apellido, producto.membresia, producto.id) # Especifica los valores para hacer el UPDATE, tomando los valores del objeto producto
            cursor.execute(cls.UPDATE, valores) # Ejecuta la consulta SQL definida en el atributo constante 'UPDATE'.
            conexion.commit() # Confirma la subida los cambios en la base de datos.
            return cursor.rowcount # Está variable indica cuatos datos se modificaron en la base de datos
        except Exception as e:
            print(f'Ocurrió un error al insertar el producto: {e}')
        finally:
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión con la db
    
    @classmethod
    def delete(cls, producto):
        conexion = None
        try: # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion() # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor() # Crea un objeto cursor para ejecutar consultas SQL.
            valores = (producto.id,) # Especifica el valor de "ID" para ejecutar la sentencia delete, tomando los valores del objeto producto (como valores es una tupla, añadimos la "," después del primer valor para especificar que es una tupla con solo un dato)
            cursor.execute(cls.DELETE, valores) # Ejecuta la consulta SQL definida en el atributo constante 'DELETE'.
            conexion.commit() # Confirma la subida del cambio en la base de datos.
            return cursor.rowcount # Está variable indica cuatos datos se modificaron en la base de datos
        except Exception as e:
            print(f'Ocurrió un error al insertar el producto: {e}')
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos
    
if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente (no importado como módulo).
    clientes = GestionInventario.read()  # Llama al método 'read' de la clase 'GestionInventario' para obtener todos los clientes.
    for cliente in clientes:  # Itera sobre la lista de clientes obtenida.
        print(cliente)  # Imprime la información de cada cliente (utilizando el método '__str__' de la clase 'Cliente').