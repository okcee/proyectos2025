import sys  # Importa el módulo 'sys' para acceder a funcionalidades del sistema, como la ruta de búsqueda de módulos.
import os  # Importa el módulo 'os' para interactuar con el sistema operativo, como la manipulación de rutas de archivos.

from .GestionContactos import GestionContactos
from .Contacto import Contacto

class GestionAPP:
    def __init__(self):
        self.GestionContactos = GestionContactos()
    
    def mostrar_menu(self):
        print('~~~~~~ MENÚ: Gestión de Contactos ~~~~~~','\n')
        while True:
            try:
                print(f'''Opciones:
                        1. Agregar un contacto
                        2. Mostrar todos los contactos
                        3. Buscar un contacto
                        4. Eliminar un contacto
                        5. Salir del menú''')
                opcion = int(input('Escribe tu opción (1-4): '))
                if opcion == 1:
                    nombre = input('Introduce el nombre del contacto: ')
                    telefono = input('Introduce el numero de teléfono: ')
                    correo = input('Introduce el correo electrónico')
                    self.GestionContactos.agregar_contacto(nombre, telefono, correo)
                elif opcion == 2:
                    self.GestionContactos.mostrar_contactos()
                elif opcion == 3:
                    nombre = input('Introduce el nombre del contacto: ')
                    self.GestionContactos.buscar_contacto(nombre)
                elif opcion == 4:
                    nombre = input('Introduce el nombre del contacto: ')
                    self.GestionContactos.eliminar_contacto(nombre)
                elif opcion == 5:
                    print('Salimos del programa...')
                    break
                else:
                    print('Opción inválida, Introduce un valor entre 1 y 4.')
                
            except ValueError:
                print('Error: Introduce un número válido.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')