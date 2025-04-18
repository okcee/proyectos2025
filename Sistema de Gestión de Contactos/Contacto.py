import sys  # Importa el módulo 'sys' para acceder a funcionalidades del sistema, como la ruta de búsqueda de módulos.
import os  # Importa el módulo 'os' para interactuar con el sistema operativo, como la manipulación de rutas de archivos.

class Contacto:
    def __init__(self, nombre=None, telefono=None, correo=None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
    def __str__(self):
        return (f'Nombre: {self.nombre}, Número de telefono: {self.telefono}, Correo electrónico: {self.correo}')
