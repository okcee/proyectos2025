# Clase GestionInventario. Implementa operaciones CRUD (Create, Read, Update, Delete)
''' 
Se usará para las operaciones CRUD:
Patrón de diseño DAO
DAO = Data Accesss Object
Este patrón se utiliza para acceder a la información de una entidad de nuestra aplicación.
En este caso a través del cliente DAO vamos a acceder a la información de la tabla cliente y poder mediante métodos de la clase Cliente DAO, interactuar con la clase Cliente para ejecutar sentencias en la tabla cliente
Esta forma de relacionar los datos es el principio de aplicaciones que se conocen como ORM (Object Relational Mappin), o también de mapeo relación entidad
'''
from conexion import Conexion
from producto import Producto
from mysql.connector import Error

class GestionInventario:
    # Asume tabla 'inventario' y columnas: id (PK, AI), nombre, cantidad, precio, categoria
    _CREATE = 'INSERT INTO inventario(nombre, cantidad, precio, categoria) VALUES(%s, %s, %s, %s)'
    _READ = 'SELECT id, nombre, cantidad, precio, categoria FROM inventario ORDER BY nombre'
    _UPDATE = 'UPDATE inventario SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE id=%s'
    _DELETE = 'DELETE FROM inventario WHERE id=%s'
    _FIND_BY_NAME = "SELECT id, nombre, cantidad, precio, categoria FROM inventario WHERE nombre = %s"
    _FIND_BY_ID = "SELECT id, nombre, cantidad, precio, categoria FROM inventario WHERE id = %s"


    @classmethod
    def create(cls, producto: Producto) -> int:
        """Inserta un nuevo producto."""
        conexion = None
        cursor = None
        rows_affected = 0
        try:
            conexion = Conexion.obtener_conexion()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                # Los valores se toman del objeto Producto
                valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
                # Se ejecuta la constante _CREATE
                cursor.execute(cls._CREATE, valores)
                conexion.commit()
                rows_affected = cursor.rowcount
                print(f"Producto '{producto.nombre}' insertado en tabla 'inventario'. Filas afectadas: {rows_affected}") # Mensaje actualizado opcional
            else:
                print("Error: No se pudo obtener conexión para crear.")
        except Error as e:
            # Manejo de error específico para duplicados si 'nombre' es UNIQUE en 'inventario'
            if e.errno == 1062: # Código de error para entrada duplicada
                print(f"Error: Ya existe un producto con el nombre '{producto.nombre}' en la tabla 'inventario'. No se pudo insertar.")
            else:
                print(f'Ocurrió un error al insertar en la tabla inventario: {e}')
            if conexion:
                conexion.rollback() # Deshacer en caso de error
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return rows_affected

    @classmethod
    def read(cls) -> list[Producto]:
        """Lee todos los productos."""
        conexion = None
        cursor = None
        productos = []
        try:
            conexion = Conexion.obtener_conexion()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                cursor.execute(cls._READ)
                registros = cursor.fetchall()
                for registro in registros:
                    # Crear Producto con elementos de la tupla
                    producto = Producto(id=registro[0], nombre=registro[1], cantidad=registro[2], precio=registro[3], categoria=registro[4])
                    productos.append(producto)
            else:
                print("Error: No se pudo obtener conexión para leer.")
        except Error as e:
            print(f'Ocurrió un error al seleccionar los productos: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return productos
    
    @classmethod
    def find_by_name(cls, nombre_buscado: str) -> Producto | None:
        """Busca un producto por nombre."""
        conexion = None
        cursor = None
        producto_encontrado = None
        try:
            conexion = Conexion.obtener_conexion()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                valores = (nombre_buscado,)
                cursor.execute(cls._FIND_BY_NAME, valores)
                registro = cursor.fetchone()
                if registro:
                    producto_encontrado = Producto(id=registro[0], nombre=registro[1], cantidad=registro[2], precio=registro[3], categoria=registro[4])
            else:
                print("Error: No se pudo obtener conexión para buscar por nombre.")
        except Error as e:
            print(f'Ocurrió un error al buscar el producto por nombre: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return producto_encontrado

    @classmethod
    def find_by_id(cls, id_buscado: int) -> Producto | None:
        """Busca un producto por su ID."""
        conexion = None
        cursor = None
        producto_encontrado = None
        try:
            conexion = Conexion.obtener_conexion()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                valores = (id_buscado,) # Pasar ID como tupla
                cursor.execute(cls._FIND_BY_ID, valores)
                registro = cursor.fetchone()
                if registro:
                    producto_encontrado = Producto(id=registro[0], nombre=registro[1], cantidad=registro[2], precio=registro[3], categoria=registro[4])
            else:
                print("Error: No se pudo obtener conexión para buscar por ID.")
        except Error as e:
            print(f'Ocurrió un error al buscar el producto por ID: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return producto_encontrado

    @classmethod
    def update(cls, producto: Producto) -> int:
        """Actualiza un producto existente usando su ID."""
        conexion = None
        cursor = None # Inicializar
        rows_affected = 0
        # --- MEJORA: Validar que el producto tenga ID ---
        if producto.id is None:
            print("Error: No se puede actualizar un producto sin ID.")
            return 0
        try:
            conexion = Conexion.obtener_conexion()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                # --- CORRECCIÓN: Valores para UPDATE por ID ---
                valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria, producto.id)
                cursor.execute(cls._UPDATE, valores)
                conexion.commit()
                rows_affected = cursor.rowcount
                print(f"Producto ID {producto.id} actualizado. Filas afectadas: {rows_affected}")
                if rows_affected == 0:
                    print(f"Advertencia: No se encontró/modificó producto con ID {producto.id}.")
            else:
                print("Error: No se pudo obtener conexión para actualizar.")
        except Error as e:
            print(f'Ocurrió un error al actualizar el producto: {e}')
            if conexion:
                conexion.rollback()
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return rows_affected

    @classmethod
    def delete(cls, producto_id: int) -> int: # Cambiado para aceptar ID directamente
        """Elimina un producto usando su ID."""
        conexion = None
        cursor = None # Inicializar
        rows_affected = 0
        try:
            conexion = Conexion.obtener_conexion()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                # --- CORRECCIÓN: Valor para DELETE por ID ---
                valores = (producto_id,)
                cursor.execute(cls._DELETE, valores)
                conexion.commit()
                rows_affected = cursor.rowcount
                print(f"Producto ID {producto_id} eliminado. Filas afectadas: {rows_affected}")
                if rows_affected == 0:
                    print(f"Advertencia: No se encontró producto con ID {producto_id} para eliminar.")
            else:
                print("Error: No se pudo obtener conexión para eliminar.")
        except Error as e:
            print(f'Ocurrió un error al eliminar el producto: {e}')
            if conexion:
                conexion.rollback()
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return rows_affected

# Bloque de prueba corregido
if __name__ == '__main__':
    print("\n--- Probando GestionInventario ---")
    print("Leyendo productos existentes...")
    # --- CORRECCIÓN: Usar "productos" ---
    productos_iniciales = GestionInventario.read()
    if productos_iniciales:
        for prod in productos_iniciales:
            print(prod)
    else:
        print("No se encontraron productos iniciales o hubo un error.")
