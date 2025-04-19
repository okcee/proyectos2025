# Clase Producto. Está será la clase modelo también conocida como clase de dominio

class Producto:
    def __init__(self, id=None, nombre=None, cantidad=None, precio=None, categoria=None):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
    
    def __str__(self): # Para poder imprimir en cualquier momento el estado de este objeto, que son los valores de los atributos de nuestro objeto
        return (f'Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.cantidad}, Membresia: {self.precio}, Categoría: {self.categoria}')