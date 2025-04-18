from GestionContactos import GestionContactos

class GestionAPP:
    def __init__(self):
        self.gestion_contactos = GestionContactos()
    
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
                    # Validación de entrada vacía
                    if not nombre or not telefono or not correo:
                        print("\nError: Todos los campos (nombre, teléfono, correo) son obligatorios.\n")
                    else:
                        # Llamar solo si los campos no están vacíos
                        self.gestion_contactos.agregar_contacto(nombre, telefono, correo)
                elif opcion == 2:
                    self.gestion_contactos.mostrar_contactos()
                elif opcion == 3:
                    nombre = input('Introduce el nombre del contacto: ')
                    self.gestion_contactos.buscar_contacto(nombre)
                elif opcion == 4:
                    nombre = input('Introduce el nombre del contacto: ')
                    self.gestion_contactos.eliminar_contacto(nombre)
                elif opcion == 5:
                    print('Salimos del programa...')
                    break
                else:
                    print('Opción inválida, Introduce un valor entre 1 y 4.')
                
            except ValueError:
                print('Error: Introduce un número válido.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')

if __name__ == '__main__':
    app = GestionAPP()
    app.mostrar_menu()