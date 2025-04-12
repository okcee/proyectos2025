# Enunciado de la Práctica

**Título:** Sistema de Gestión de Contactos

**Descripción:** Crear un programa en Python que simule un sistema de gestión de contactos. El programa debe permitir a los usuarios realizar las siguientes acciones:

1.  **Agregar un contacto:** Permite al usuario agregar un contacto a la lista de contactos. Los contactos deben tener atributos como nombre, número de teléfono y correo electrónico.
2.  **Mostrar todos los contactos:** Muestra una lista de todos los contactos disponibles.
3.  **Buscar un contacto:** Permite al usuario buscar un contacto por nombre.
4.  **Eliminar un contacto:** Permite al usuario eliminar un contacto de la lista.

**Requisitos:**

1.  Utiliza clases para representar los contactos y el sistema de gestión de contactos.
2.  Implementa métodos para agregar, mostrar, buscar y eliminar contactos.
3.  Utiliza estructuras de control y ciclos para manejar la interacción con el usuario.
4.  Utiliza manejo de archivos para guardar y cargar la lista de contactos en un archivo de texto.
5.  Implementa gestión de errores para manejar situaciones como:
    * Intentar agregar un contacto con un formato de correo electrónico inválido.
    * Intentar buscar o eliminar un contacto que no existe.
    * Manejo de errores al leer o escribir en el archivo.

**Instrucciones:**

1.  Crea una clase `Contacto` con atributos para el nombre, número de teléfono y correo electrónico.
2.  Crea una clase `GestionContactos` que contenga una lista de contactos y métodos para agregar, mostrar, buscar y eliminar contactos.
3.  Implementa un menú que permita al usuario seleccionar una acción (agregar, mostrar, buscar o eliminar un contacto).
4.  Utiliza un archivo de texto para guardar la lista de contactos y carga los datos al iniciar el programa.
5.  Implementa validaciones para asegurar que el formato del correo electrónico es válido y que los campos requeridos no están vacíos.
6.  Implementa manejo de excepciones para capturar y manejar errores relacionados con el archivo y las operaciones de contacto.

**Entrega:** Los estudiantes deben entregar el código fuente del programa junto con un archivo de texto que contenga algunos contactos de ejemplo.