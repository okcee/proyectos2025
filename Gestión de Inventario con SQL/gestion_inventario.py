# Clase GestionInventario. Implementa operaciones CRUD (Create, Read, Update, Delete)
''' 
Se usará para las operaciones CRUD:
Patrón de diseño DAO
DAO = Data Accesss Object
Este patrón se utiliza para acceder a la información de una entidad de nuestra aplicación.
En este caso a través del cliente DAO vamos a acceder a la información de la tabla cliente y poder mediante métodos de la clase Cliente DAO, interactuar con la clase Cliente para ejecutar sentencias en la tabla cliente
Esta forma de relacionar los datos es el principio de aplicaciones que se conocen como ORM (Object Relational Mappin), o también de mapeo relación entidad
'''

'''Sistema de Gestión de Contactos/ # Raíz del proyecto
├── gestion_inventario.py                     # Contiene la clase GestionInventario. Implementa operaciones CRUD
│   ├── agregar un producto
│   ├── mostrar todos los productos
│   ├── buscar un producto
│   ├── actualizar un producto
│   └── eliminar un producto
'''
from conexion import Conexion
from producto import Producto

class GestionInventario:
    CREATE = 'INSERT * FROM producto ORDER BY id' # Define una constante con la consulta SQL para seleccionar todos los registros de la tabla 'inventario' ordenados por 'id'.
    READ = 'SELECT * FROM producto ORDER BY id'  # Define una constante con la consulta SQL para seleccionar todos los registros de la tabla 'producto' ordenados por 'id'.
    UPDATE = 'UPDATE producto SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'  # Define una constante con la consulta SQL para actualizar un registro existente en la tabla 'producto'.
    DELETE = 'DELETE FROM producto WHERE id=%s'  # Define una constante con la consulta SQL para eliminar un registro de la tabla 'producto' por su 'id'.
    
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
    def update(cls, producto):
        