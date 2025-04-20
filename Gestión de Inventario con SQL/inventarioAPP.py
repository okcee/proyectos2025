# Contiene la lógica del menú y la interacción principal

from gestion_inventario import GestionInventario
from producto import Producto
from mysql.connector import Error as MySQLError

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print(f'''\n ~~~~~~ Menú: Sistema de Gestión de Inventario ~~~~~~
            1. Agregar un producto
            2. Mostrar todos los productos
            3. Buscar un producto por Nombre
            4. Actualizar un producto por Nombre
            5. Eliminar un producto por Nombre
            6. Salir ''')

def solicitar_datos_producto(para_actualizar=False, producto_existente=None):
    """
    Solicita los datos de un producto al usuario, con validación.
    Si es para actualizar, muestra los valores actuales y permite dejar en blanco para no cambiar.
    Devuelve un objeto Producto si los datos son válidos, o None si hay error o cancelación implícita.
    """
    print("-" * 20)
    nombre_actual = f" (actual: {producto_existente.nombre})" if producto_existente else ""
    nombre_var = input(f'Ingrese nombre del producto{nombre_actual}: ')
    if para_actualizar and nombre_var.strip() == "" and producto_existente:
        nombre_var = producto_existente.nombre # Mantener nombre actual si se deja en blanco

    cantidad_var = None
    cantidad_actual = f" (actual: {producto_existente.cantidad})" if producto_existente else ""
    while cantidad_var is None:
        cantidad_str = input(f'Ingrese cantidad (entero){cantidad_actual}: ')
        if para_actualizar and cantidad_str.strip() == "" and producto_existente:
            cantidad_var = producto_existente.cantidad # Mantener cantidad actual
            break
        try:
            cantidad_var = int(cantidad_str)
            if cantidad_var < 0: # Validación adicional (opcional)
                print("Error: La cantidad no puede ser negativa.")
                cantidad_var = None # Forzar a pedir de nuevo
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    precio_var = None
    precio_actual = f" (actual: {producto_existente.precio})" if producto_existente else ""
    while precio_var is None:
        precio_str = input(f'Ingrese precio (decimal, ej: 10.99){precio_actual}: ')
        if para_actualizar and precio_str.strip() == "" and producto_existente:
            precio_var = producto_existente.precio # Mantener precio actual
            break
        try:
            # Reemplazar coma por punto para mayor flexibilidad de entrada
            precio_var = float(precio_str.replace(',', '.'))
            if precio_var < 0: # Validación adicional opcional
                print("Error: El precio no puede ser negativo.")
                precio_var = None # Forzar a pedir de nuevo
        except ValueError:
            print("Error: El precio debe ser un número.")

    categoria_actual = f" (actual: {producto_existente.categoria})" if producto_existente else ""
    categoria_var = input(f'Ingrese categoría del producto{categoria_actual}: ')
    if para_actualizar and categoria_var.strip() == "" and producto_existente:
        categoria_var = producto_existente.categoria # Mantener categoría actual

    print("-" * 20)

    # Crear y devolver el objeto Producto
    try:
        if para_actualizar and producto_existente:
            # Para actualizar, usamos el ID existente
            producto_obj = Producto(id=producto_existente.id, nombre=nombre_var, cantidad=cantidad_var, precio=precio_var, categoria=categoria_var)
        else:
            # Para crear, el ID será None (o asignado por la BD)
            producto_obj = Producto(nombre=nombre_var, cantidad=cantidad_var, precio=precio_var, categoria=categoria_var)

        # Verificar si las conversiones internas en Producto fallaron (aunque ya validamos antes)
        if producto_obj.cantidad is None or producto_obj.precio is None:
            print("Advertencia: Hubo un problema interno con la cantidad o el precio.")
            return None # Indicar que algo falló

        return producto_obj

    except Exception as e:
        print(f"Error inesperado al crear objeto Producto: {e}")
        return None


# --- Lógica Principal de la Aplicación ---
print('~~~~~~ Iniciando Sistema de Gestión de Inventario ~~~~~~')
opcion = None
while opcion != 6:
    mostrar_menu()
    try:
        opcion_str = input('Ingrese una opción (1-6): ')
        opcion = int(opcion_str)

        # --- Bloque principal de opciones ---
        if opcion == 1: # Agregar un producto
            print("\n--- 1. Agregar Producto ---")
            producto_nuevo = solicitar_datos_producto()
            if producto_nuevo: # Verificar que solicitar_datos_producto devolvió un objeto válido
                productos_insertados = GestionInventario.create(producto_nuevo)
                # El manejo de duplicados (nombre UNIQUE) se hace en el DAO (imprime error específico)
                if productos_insertados > 0:
                    print(f'Producto "{producto_nuevo.nombre}" agregado exitosamente.')
                # Si create devuelve 0 o menos, el error ya se imprimió desde el DAO.
            else:
                print("Creación cancelada o datos inválidos.")

        elif opcion == 2: # Mostrar todos los productos
            print("\n--- 2. Listado de Productos ---")
            productos = GestionInventario.read()
            if not productos:
                # Podría ser lista vacía o error de conexión (el error se imprime desde el DAO)
                print("No hay productos en el inventario o no se pudo acceder a la base de datos.")
            else:
                print("-" * 60)
                for producto in productos:
                    print(producto) # Usa el __str__ de Producto
                print("-" * 60)

        elif opcion == 3: # Buscar un producto por Nombre
            print("\n--- 3. Buscar Producto por Nombre ---")
            nombre_a_buscar = input("Introduce el nombre exacto del producto a buscar: ")
            producto_encontrado = GestionInventario.find_by_name(nombre_a_buscar)
            if producto_encontrado:
                print("\nProducto encontrado:")
                print(producto_encontrado)
            else:
                # Requisito: Manejar producto no encontrado
                print(f"\nNo se encontró ningún producto con el nombre '{nombre_a_buscar}'.")

        elif opcion == 4: # Actualizar un producto POR NOMBRE
            print("\n--- 4. Actualizar Producto por Nombre ---")
            nombre_a_actualizar = input("Ingrese el NOMBRE del producto que desea actualizar: ")

            producto_existente = GestionInventario.find_by_name(nombre_a_actualizar)

            if producto_existente:
                print(f"\nProducto encontrado: {producto_existente}")
                print("Ingrese los nuevos datos (deje en blanco para no cambiar):")

                producto_actualizado = solicitar_datos_producto(para_actualizar=True, producto_existente=producto_existente)

                if producto_actualizado: # Verificar que solicitar_datos devolvió un objeto válido
                    filas_afectadas = GestionInventario.update(producto_actualizado)
                    if filas_afectadas > 0:
                        print(f"Producto '{producto_actualizado.nombre}' (ID: {producto_actualizado.id}) actualizado exitosamente.")
                    else:
                        # Podría ser 0 si no se encontró (raro si find_by_name funcionó) o si los datos eran iguales
                        print(f"El producto '{nombre_a_actualizar}' no fue actualizado (posiblemente no hubo cambios o hubo un error).")
                else:
                    print("Actualización cancelada o datos inválidos.")
            else:
                # Manejo de error: producto no encontrado
                print(f"No se encontró ningún producto con el nombre '{nombre_a_actualizar}'.")

        elif opcion == 5: # Eliminar un producto POR NOMBRE
            print("\n--- 5. Eliminar Producto por Nombre ---")
            nombre_a_eliminar = input("Ingrese el NOMBRE del producto que desea eliminar: ")

            producto_a_eliminar = GestionInventario.find_by_name(nombre_a_eliminar)

            if producto_a_eliminar:
                print(f"\nProducto encontrado: {producto_a_eliminar}")
                # Confirmación
                confirmacion = input(f"¿Está seguro de que desea eliminar este producto? (s/N): ").lower()
                if confirmacion == 's':
                    # Llamar a delete pasando el ID del producto encontrado
                    filas_afectadas = GestionInventario.delete(producto_a_eliminar.id)
                    if filas_afectadas > 0:
                        print(f"Producto '{producto_a_eliminar.nombre}' (ID: {producto_a_eliminar.id}) eliminado exitosamente.")
                    else:
                        # El error (si lo hubo) ya se imprimió desde el DAO
                        print(f"No se pudo eliminar el producto '{nombre_a_eliminar}' (quizás ya fue eliminado o hubo un error).")
                else:
                    print("Eliminación cancelada.")
            else:
                # Manejo de error: producto no encontrado
                print(f"No se encontró ningún producto con el nombre '{nombre_a_eliminar}'.")

        elif opcion == 6: # Salir
            print("\nSaliendo del sistema...")

        else: # Opción inválida
            print("Opción no válida. Por favor, ingrese un número entre 1 y 6.")

    except ValueError:
        print("Error: Por favor, ingrese un número válido para la opción del menú.")
    # Captura errores específicos de MySQL si se propagan hasta aquí (menos probable)
    except MySQLError as db_error:
        print(f"Error inesperado de base de datos en la aplicación: {db_error}")
    # Captura general para otros errores inesperados
    except Exception as e:
        print(f"Ocurrió un error inesperado en la aplicación: {e}")
        # Considera añadir 'import traceback; traceback.print_exc()' aquí para depuración avanzada

print('~~~~~~ Sistema de Gestión de Inventario Finalizado ~~~~~~')
