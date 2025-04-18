
class Contacto:
    def __init__(self, nombre=None, telefono=None, correo=None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
    def __str__(self):
        return (f'Nombre: {self.nombre}, Número de telefono: {self.telefono}, Correo electrónico: {self.correo}')
