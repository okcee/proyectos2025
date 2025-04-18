* **`__init__` y `_cargar_contactos`:** Carga correctamente los datos desde `lista_contactos.json` al iniciar, manejando `FileNotFoundError` y `JSONDecodeError`. Convierte los diccionarios JSON en objetos `Contacto`. ¡Perfecto!
* **`_guardar_contactos`:** Guarda la lista completa de objetos `Contacto` (convertidos a diccionarios) en el archivo JSON, sobrescribiéndolo. Usa `indent=4` y `ensure_ascii=False`, lo cual es bueno para legibilidad y caracteres especiales. Maneja `IOError`. ¡Muy bien!
* **`agregar_contacto`:**
    * Valida campos vacíos.
    * Valida formato de correo con `re.match`.
    * Valida si el contacto ya existe (evita duplicados por nombre, insensible a mayúsculas/minúsculas).
    * Crea el objeto `Contacto`.
    * Añade a la lista en memoria (`self.contactos`).
    * Llama a `_guardar_contactos` para persistir el cambio.
    * Devuelve `True`/`False` y mensajes claros. ¡Implementación completa y robusta!
* **`mostrar_contactos`:** Itera sobre la lista en memoria (`self.contactos`) y usa el `__str__` de cada objeto. Maneja el caso de lista vacía. ¡Correcto!
* **`buscar_contacto`:** Busca en la lista en memoria (insensible a mayúsculas/minúsculas). Maneja correctamente el caso "no encontrado". ¡Correcto!
* **`eliminar_contacto`:** Busca el objeto en la lista en memoria (insensible a mayúsculas/minúsculas), lo elimina si existe usando `self.contactos.remove()`, guarda los cambios y maneja el caso "no encontrado". ¡Correcto!