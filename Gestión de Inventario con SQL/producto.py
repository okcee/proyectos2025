# Clase Producto. Está será la clase modelo también conocida como clase de dominio

class Producto:
    def __init__(self, id=None, nombre=None, cantidad=None, precio=None, categoria=None):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria

        try:
            self.cantidad = int(cantidad) if cantidad is not None else None
        except (ValueError, TypeError):
            print(f"Advertencia: Cantidad '{cantidad}' no es un número entero válido. Se establecerá como None.")
            self.cantidad = None # Asignar 0 o lanzar excepción

        try:
            self.precio = float(precio) if precio is not None else None
        except (ValueError, TypeError):
            print(f"Advertencia: Precio '{precio}' no es un número válido. Se establecerá como None.")
            self.precio = None # Asignar 0.0 o lanzar excepción

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, '
                f'Precio: {self.precio}, Categoría: {self.categoria}')
