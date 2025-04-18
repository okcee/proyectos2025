import json
import re

from Contacto import Contacto

class GestionContactos:
    lista_contactos = 'lista_contactos.json'
    
    def __init__(self): # Carga Inicial
        self.contactos = self._cargar_contactos() # Cargamos datos desde el archivo
    # 
    def _cargar_contactos(self): # Gestión en Memoria, las operaciones no usan self.contactos como fuente inicial de datos, por lo que tendrán que operar sobre este método
        """Carga los contactos desde el archivo JSON."""
        try:
            with open(self.lista_contactos, 'r', encoding='utf8') as archivo:
                datos_json = json.load(archivo)
                # Convertir diccionarios JSON a objetos Contacto
                contactos_cargados = []
                for data in datos_json:
                    # Asegurarse que los nombres de las claves coinciden con los atributos de Contacto
                    contactos_cargados.append(Contacto(data['nombre'], data['telefono'], data['correo']))
                return contactos_cargados
        except FileNotFoundError:
            print(f"Advertencia: Archivo '{self.lista_contactos}' no encontrado. Se iniciará con una lista vacía.")
            return [] # Si no existe el archivo, empezar con lista vacía
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self.lista_contactos}' no tiene formato JSON válido o está vacío. Se iniciará con una lista vacía.")
            return []
        except Exception as e:
            print(f"Error inesperado al cargar contactos: {e}")
            return []
    #  Método _guardar_contactos: centraliza la lógica de escritura en el archivo JSON después de modificar la lista en memoria.
    # Convertir la lista de objetos Contacto a una lista de diccionarios y usa json.dump.
    def _guardar_contactos(self):
        """Guarda la lista actual de contactos en el archivo JSON."""
        lista_para_guardar = []
        for contacto in self.contactos:
            lista_para_guardar.append({
                'nombre': contacto.nombre,
                'telefono': contacto.telefono,
                'correo': contacto.correo
            })
        try:
            with open(self.lista_contactos, 'w', encoding='utf8') as archivo:
                json.dump(lista_para_guardar, archivo, indent=4, ensure_ascii=False) # indent=4 para formato legible
        except IOError as e:
            print(f"Error al guardar contactos en '{self.lista_contactos}': {e}")
        except Exception as e:
            print(f"Error inesperado al guardar contactos: {e}")
    # Debe aceptar todos los datos, validar campos, validar email, añadir a la lista en memoria y guardar.
    def agregar_contacto(self, nombre, telefono, correo):
        """Agrega un nuevo contacto a la lista."""
        # Validación campos vacíos
        if not nombre or not telefono or not correo:
            print("Error: Nombre, teléfono y correo no pueden estar vacíos.")
            return False # Indicar fallo

        # Validación formato correo
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_correo, correo):
            print("Error: Formato de correo electrónico inválido.")
            return False # Indicar fallo

        # Validación si el contacto (por nombre) ya existe (opcional pero recomendable)
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Error: Ya existe un contacto con el nombre '{nombre}'.")
                return False

        # Crear y añadir el contacto a la lista en memoria
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)

        # Guardar la lista actualizada en el archivo
        self._guardar_contactos()
        print(f"Contacto '{nombre}' agregado correctamente.")
        return True # Indicar éxito
    # Debe mostrar los contactos de la lista en memoria (self.contactos).
    def mostrar_contactos(self):
        """Muestra todos los contactos de la lista en memoria."""
        print('\n~~~~~~ Listado de Contactos ~~~~~~')
        if not self.contactos:
            print("No hay contactos para mostrar.")
            return

        for i, contacto in enumerate(self.contactos):
            print(f"{i + 1}. {contacto}") # Usa el __str__ de Contacto
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    # Debe aceptar un nombre, buscar en la lista en memoria y manejar el caso "no encontrado"
    def buscar_contacto(self, nombre): # Cambiar firma
        """Busca un contacto por nombre en la lista en memoria."""
        encontrado = False
        print(f"\n--- Buscando contacto: {nombre} ---")
        for contacto in self.contactos:
            # Comparación insensible a mayúsculas/minúsculas
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                print(contacto) # Usa el __str__
                encontrado = True
                # Podríamos parar aquí si solo queremos el primero: break
                # O seguir por si hay duplicados (aunque agregar_contacto lo evita)
        
        if not encontrado:
            # Manejo de error: contacto no existe
            print(f"Error: No se encontró ningún contacto con el nombre '{nombre}'.")
        print("-----------------------------------\n")
        # Podríamos devolver el objeto encontrado o None/False si no se encuentra
        # return contacto_encontrado if encontrado else None
    # Debe aceptar un nombre, buscar en la lista en memoria, eliminarlo si existe, guardar la lista actualizada y manejar el caso "no encontrado".
    def eliminar_contacto(self, nombre): # Cambiar firma
        """Elimina un contacto por nombre de la lista en memoria."""
        contacto_a_eliminar = None
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto_a_eliminar = contacto
                break # Encontramos el contacto, salimos del bucle

        if contacto_a_eliminar:
            self.contactos.remove(contacto_a_eliminar)
            self._guardar_contactos() # Guardar cambios
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            # Manejo de error: contacto no existe
            print(f"Error: No se encontró ningún contacto con el nombre '{nombre}' para eliminar.")
