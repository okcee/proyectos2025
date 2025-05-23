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

**Estructura:** 

Sistema de Gestión de Contactos/ # Raíz del proyecto
├── GestionAPP.py                          # Contiene la lógica del menú y la interacción principal
│   ├── agregar un contacto
│   ├── mostrar todos los contactos
│   ├── buscar un contacto
│   └── eliminar un contacto
├── GestionContactos.py                 # Contiene la clase GestionContactos con los métodos
│   ├── agregar un contacto
│   ├── mostrar todos los contactos
│   ├── buscar un contacto
│   └── eliminar un contacto
├── Contacto.py                         # Contiene la clase Contacto
└── listaContactos.txt

Análisis de la estructura final:  
- Sistema de Gestión de Contactos/: Define claramente la raíz del proyecto.  
- GestionAPP.py: Este archivo actuará como el punto de entrada principal de la aplicación. Contendrá la lógica para mostrar el menú al usuario, capturar sus interacciones y coordinar las acciones llamando a los métodos de la clase GestionContactos. Los subpuntos dentro del comentario indican claramente las funcionalidades del menú.  
- GestionContactos.py: Aquí se definirá la clase GestionContactos, que encapsulará la lógica de negocio para administrar la lista de contactos (agregar, mostrar, buscar, eliminar). Los subpuntos dentro del comentario detallan los métodos que contendrá esta clase.  
- Contacto.py: Este archivo contendrá la definición de la clase Contacto, que representará la estructura de cada contacto con sus atributos (nombre, número de teléfono, correo electrónico).  
- listaContactos.txt: Este será el archivo de texto utilizado para guardar y cargar la persistencia de los datos de los contactos. Su ubicación en la raíz del proyecto es adecuada para este tipo de aplicación.  