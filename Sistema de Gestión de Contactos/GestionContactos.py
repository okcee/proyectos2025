import sys  # Importa el módulo 'sys' para acceder a funcionalidades del sistema, como la ruta de búsqueda de módulos.
import os  # Importa el módulo 'os' para interactuar con el sistema operativo, como la manipulación de rutas de archivos.

from .Contacto import Contacto

class GestionContactos:
    lista_contactos = 'lista_contactos.txt'
    
    def agregar_contacto(self):
        with open(self.lista_contactos.txt, 'w', encoding='utf8') as archivo:
            archivo.write(f'{Contacto}\n')
    
    def mostrar_contactos(self):
        with open(self.lista_contactos.txt, 'r', encoding='utf8') as archivo:
            print('~~~~~~ Listado de Contactos ~~~~~~','\n')
            print(archivo.read())
    
    def buscar_contacto(self):
        with open(self.lista_contactos.txt, 'r', encoding='utf8') as archivo:
            print('El contacto buscado es: ','\n')
            archivo.find(f'{Contacto}\n')
    
    def eliminar_contacto(self):
        with open(self.lista_contactos.txt, 'w', encoding='utf8') as archivo:
            archivo.write(f'{Contacto}\n')
            print('El contacto buscado es: ','\n')