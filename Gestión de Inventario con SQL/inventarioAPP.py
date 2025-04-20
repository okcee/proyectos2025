# Contiene la lógica del menú y la interacción principal
'''Sistema de Gestión de Contactos/ # Raíz del proyecto
├── inventarioAPP.py                          # Contiene la lógica del menú y la interacción principal
│   ├── agregar un producto
│   ├── mostrar todos los productos
│   ├── buscar un producto
│   ├── actualizar un producto
│   └── eliminar un producto
salir
'''

from gestion_inventario import GestionInventario
from producto import Producto

print('~~~~~~ Menú: Sistema de Gestión de Inventario con Base de Datos ~~~~~~')
opcion = None
while opcion !=6:
    print(f'''\n MENU:
            1. Agregar un producto
            2. Mostrar todos los productos
            3. Buscar un producto
            4. Actualizar datos de un producto
            5. Eliminar un producto
            6. Salir ''')
    opcion = int(input('Ingrese una opción (1-6): '))
    if opcion == 1: # Agregar un producto
        nombre_var = input('Ingrese el nombre del producto: ')
        cantidad_var = input('Ingrese el apellido del producto: ')
        precio_var = input('Ingrese la membresia del producto: ')
        categoria_var = input('Ingrese la membresia del producto: ')
        producto = Producto(nombre=nombre_var, cantidad=cantidad_var, precio=precio_var, categoria=categoria_var)
        productos_insertados = GestionInventario.create(producto)
        print(f'Productos insertados: {productos_insertados}')
    elif opcion == 2: # Mostrar todos los productos
        productos = GestionInventario.read()
        print('\n*** Listado de productos ***')
        for producto in productos:
            print(producto)
    elif opcion == 3: # Buscar un producto
        print("\n--- Buscar Producto por Nombre ---") # Mensaje más descriptivo
        nombre_a_buscar = input("Introduce el nombre del producto que deseas buscar: ")
        producto = GestionInventario.find_by_name(nombre_a_buscar)
        if producto:
            print("\nProducto encontrado:")
            print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}, Categoría: {producto.categoria}")
        else:
            print(f"\nNo se encontró ningún producto con el nombre '{nombre_a_buscar}'.")
    elif opcion == 4: # Actualizar datos de un producto
        id_producto_var = int(input('Ingrese el id del producto a modificar: '))
        nombre_var = input('Ingrese el nombre del producto a modificar: ')
        cantidad_var = input('Ingrese el apellido del producto a modificar: ')
        precio_var = input('Ingrese la membresia del producto a modificar: ')
        categoria_var = input('Ingrese la membresia del producto a modificar: ')
        producto = Producto(Producto(id=id_producto_var, nombre=nombre_var, cantidad=cantidad_var, precio=precio_var, categoria=categoria_var))
        producto_actualizado = GestionInventario.actualizar(producto)
    elif opcion == 5: # Eliminar un producto
        id_producto_var = int(input('Ingrese el id del producto a eliminar: '))
        producto = Producto(id=id_producto_var)
        producto_eliminados = GestionInventario.delete(producto)
        print(f'Producto eliminado: {producto_eliminados}')
else:
    print("Salimos de la aplicación")