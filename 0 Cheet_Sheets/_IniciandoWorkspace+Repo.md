# --- **Preparación de Visual Studio Code en Windows11 con la consola Bash** ---

El flujo de trabajo típico es:

1. Instalar y configurar `Git` y `GitHub`.
2. intalar `pip` y `virtualenv` globalmente (o accesible en tu entorno base).  
3. Navegar a la carpeta de tu nuevo proyecto en la terminal.  
4. Usar el comando virtualenv para crear un nuevo entorno virtual dentro de esa carpeta.  
5. Activar el entorno virtual que se creó en el paso anterior.  
6. Se puede crear la carpeta `vscode` para establecer configuraciones personalizadas para el proyecto y su entorno virtual, mediante archivos como  `settings.json`, `launch.json` y `tasks.json`.  
7. Una vez activado el entorno virtual, pip estará disponible dentro de ese entorno para instalar las dependencias específicas de tu proyecto.  

## Iniciando un nuevo Workspace y vincularlo con un repositorio de GitHub.

1. Debemos iniciar un nuevo `workspace` en VSCode. Tenemos que ir al `menu bar`, seleccionar `File` y después `New Window` (con o sin profile, que son los datos y configuraciones del usuario).  
2. Crear en los directorios de nuestro sistema de almacenamiento local (disco duro o disco ssd) a nuestra elección, la carpeta principal (carpeta raíz) del sistema de directorios que, en un futuro contendrá el total de carpetas y archivos del `repositorio local`. GitHub se compone de un `repositorio local` y un `repositorio remoto`.  
3. Iniciar sesión en [GitHub](https://github.com/), si no estamos registrados tendremos que registrar una cuenta nueva.  
4. Crear un nuevo repositorio, dentro de nuestro usuario, vamos a `Repositories` y clicamos en `New`. Rellenamos los campos necesarios, con lo que obtendremos un enlace al repositorio creado como: `https://github.com/usuario/nombre_repositorio.git`. Sabiendo la dirección a nuestro repositorio, vamos a VScode para hacer las configuraciones iniciales necesarias.  
5. Tenemos que añadir a nuestro workspace en VScode la carpeta raíz creada en el paso 2 para el `repositorio local`. Tenemos que ir al `menu bar`, seleccionar `File` y después `Open Folder`.  
6. Ahora iniciaremos una Terminal, para ejecutar los comandos de Git en su consola. Tenemos que ir al `menu bar`, seleccionar `Terminal` y después `New Terminal`. Verificamos que la dirección abierta en la terminal coíncida con la carpeta raíz creada en el paso 2 y añadida en el paso 5.  
7. Configuración para Visual Studio Code para que los nuevos repositorios creados localmente usen "main" por defecto en vez de "master".  
   1. Comando que configura en branch principal como main.  
        git config --global init.defaultBranch main  
   2. Comando para comprobar que el branch principal sea main.  
        git checkout main  
8.  Procedemos a ejecutar los comandos de GitHub, para configurar el `repositorio local`.  
    1.  Comando que inicia Git en la carpeta raíz.  
        git init  
    2. Comando que añade la totalidad de los archivos locales al `repositorio local`.  
        git add .  
       Hay la posibilidad de añadir un sólo archivo.  
        git add nombreDelArchivo  
       Podemos ver el estado en el que se encuentran nuestros archivos.  
        git status  
    3. Configuración de los datos personales en el `repositorio local`, que se compartiran también al `repositorio remoto`.  
        git config --global user.email "nombre_email@nombre_dominio_email.com"  
        git config --global user.name "nombre_usuario"  
9.  Pasamos a asignar la dirección remota, para que quede conectada con nuestro `repositorio local`.  
    1. Asignar la dirección remota.  
        git remote add origin "https://github.com/usuario/nombre_repositoro.git"  
    2. Ya podemos hacer la primera sincronización. Subida y bajada de datos. Si fallase el paso 10, siempre podemos usar el comando siguiente para reasignar la rama local main a la nueva rama remota main. Esto permite usar git pull y git push en el futuro sin especificar el remoto y la rama.  
        git push --set-upstream origin main  
10. Primera bajada `pull` de datos de remoto a local, para bajar archivos de readme o licencias creadas en el `repositorio remoto` por GitHub.  
        git pull origin main  
11. Preparamos la primera subida `push`, creando un archivo de prueba del formato que queremos (txt, md, py, etc.), o podemos aprovechar y crear en la carpeta raíz, el archivo `.gitignore` para, en un futuro, si queremos que nos se suban al `repositorio remoto` archivos concretos, añadirlos en este, como por ejemplo `*.eve` y `**/*.config.ini`.  

El contenido del archivo `.gitignore` básico que sugiero para un principio es el siguiente:
```nfo
# Settings
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace

# Local History for Visual Studio Code
.history/
*.app
.snapshots/*

# Security settings
*.eve
**/*.config.ini
```
<Se puede configurar a gusto de cada cual>  

12. Pasamos a realizar la subida de datos `push`, el archivo .gitignore, para lo cual debemos:  
    1.  Ejecutamos el comando del primer commit para pasar la información del almacenamiento local al `repositorio local`.  
        git commit -m "descripcion"  
    2.  Hacemos el `push`.
        git push -u origin main  
13. Podemos crear en la carpeta raíz los archivos `*.eve` y `*.config.ini`, que si necesitasemos a lo largo del tiempo, podemos configurar para guardar datos sensibles, como de conexiones a databases o posibles contraseñas, que serán ignorados para la subida al `repositorio remoto`.  
    Después de realizar un commit, con el comando siguiente podemos comprobar que ambos archivos son ignorados.  
        git status --ignored  
14. Con esto debería quedar Git y GitHub configurados en nuestro workspace, se añaden algunos comandos a mayores por si surgen problemas.  
    1.  Para cambiar el origen del `repositorio remoto`.  
    Mostrar los remotos configurados actualmente.  
        git remote -v  
    Reasignar la dirección remota.  
        git remote set-url origin "https://github.com/usuario/nombre_repositoro.git"  
    Reasignar la rama local main a la nueva rama remota main. Esto permite usar git pull y git push en el futuro sin especificar el remoto y la rama.  
        git push --set-upstream origin main  
    2. Clonar un repositorio.  
        git clone https://github.com/usuario/nombre_repositoro.git  
    3. Uso de Branchs (Ramas).  
    Crear rama.  
        git branch nombreRama  
    Ver las ramas del proyecto y en qué rama me encuentro trabajando.  
        git branch  
    Cambiar de rama.  
        git checkout nombreRama  
    Eliminar rama.  
        git branch -d nombreRama  
    4. Merge (fusionar rama).  
        git merge nombreRamaAFusionar  
    5. Comandos de Repositorios.  
    Este comando te mostrará información sobre el repositorio remoto, incluyendo la rama principal.  
        git remote show origin  
    Este comando muestra todas las ramas, tanto las locales como las remotas. Esto te permite ver si el repositorio tiene una rama "main" o "master" remota.  
        git branch -a  
    Listado de todas las copias que tenemos en el repositorio  
        git log --oneline  
    Actualizar referencias locales, para asegurarte de que tu repositorio local está sincronizado y reconoce los cambios remotos.  
        git remote prune origin  
        git fetch --all  
    6. Comandos de deshacer o eliminar (¡Precaución! Esta acción es destructiva y los cambios perdidos generalmente no se pueden recuperar)  
    Descarta todos los cambios en tu directorio de trabajo y en el área de staging, y retrocede el HEAD (la punta de tu rama actual) al commit especificado.  
        git reset --hard  
        git reset --hard\<commit>  
    Crea un nuevo commit que deshace los cambios introducidos por el commit especificado. Es una forma segura de deshacer cambios en ramas compartidas, ya que no modifica el historial existente.  
        git revert \<commit>  
    Mueve el HEAD al commit especificado, pero mantiene los cambios en el área de staging y en el directorio de trabajo. Útil para rehacer un commit con cambios adicionales o un mensaje corregido.  
        git reset --soft \<commit>  
    Mueve el HEAD al commit especificado y quita los cambios del área de staging, dejándolos en el directorio de trabajo. Es el modo por defecto de git reset.  
        git reset --mixed \<commit>  
    Permite una edición interactiva del historial de commits desde el commit especificado. Puedes reordenar, combinar, editar o eliminar commits. Es potente pero requiere precaución, especialmente en ramas compartidas.  
        git reset --hard \<commit>  
    Descarta los cambios sin commitear en el archivo especificado, restaurándolo a la última versión commiteada.  
        git checkout -- \<archivo>  
    Remueve el archivo del área de staging, pero mantiene los cambios en el directorio de trabajo.  
        git restore --staged \<archivo  
    
15. Comandos de Ayuda.  
    1. Ayuda general.  
        git --help
    2. Lista disponible de subcomandos y guías de conceptos.  
        git help -a and git help -g
    3. Ayuda específica de un subcomando o concepto.  
        git help \<command> or git help \<concept>
    4. Para un overview del sistema
        git help git

# Creando carpetas como un proyecto y configurando su entorno virtual.

En cada proyecto nuevo vamos a instalar y usar `virtualenv` en lugar de `venv` con Python 3, ofrece más funcionalidades y es más rápido con el método de inicialización `app-data`.  
Con el uso `virtualenv` se resuelve el problema principal, la gestión de dependencias y versiones entre diferentes proyectos Python. Si dos aplicaciones requieren versiones conflictivas de la misma librería, instalar todo globalmente puede generar problemas. También ayuda a mantener un entorno estable para una aplicación específica y a trabajar sin permisos para modificar la instalación global de Python.  
Si está trabajando con Python 3, debe instalar virtualenv usando pip3, se da por hecho que ya están instalado, tanto Python3 en el sistema operativo, como las extensiones oficiales de Python3 en VScode.  

Pasamos a hacer las configuraciones necesarias para configurar el entorno del proyecto:  
1. Instalar pip en las dependencias generales del `workspace`, para ello:
   1. Ahora iniciaremos una Terminal, para ejecutar los comandos de Git en su consola. Tenemos que ir al `menu bar`, seleccionar `Terminal` y después `New Terminal`. Verificamos que la dirección abierta en la terminal coíncida con la carpeta raíz del `workspace`. 
   2. Procedemos a ejecutar los comandos necesarios para instalar pip.  
   3. El comando para **instalar** la última versión de `pip` es:  
        python -m pip install --upgrade pip  
   4. El comando para **actualizar** a la última versión de `pip` es:  
        pip3 install --upgrade pip  
   5. El comando para **comprobar la versión** instalada de `pip` es:  
        pip3 --version  
        pip --version  
2. Instalación de `Virtualenv` mediante comandos en la consola.  
        pip3 install virtualenv  
        pip install --upgrade virtualenv
3. Creamos la carpeta del proyecto con el nombre deseado, en la explicación la denominaremos `Proyecto`, por lo general en la carpeta raíz de nuestro `workspace`.  
4. Una vez creada, sobre el nombre de la misma, abrimos con el ratón derecho del ratón el menú contextual y seleccionamos la opción `Open in Integrated Terminal`, de manera que está consola de terminal esté con la dirección principal del proyecto.
5. Creamos el entorno virtual `Virtualenv` con el siguiente comando, si le añadimos un `.` al inicio del nombre del entorno, se podrá añadir después al archivo `.gitignore`:  
   1. La sintaxis básica del comando para crear un entorno virtual utilizando `Virtualenv` es:  
        virtualenv \<.nombre_del_entorno>  
   2. Activar el entorno virtual
        source \<.nombre_del_entorno>/Scripts/activate
   3. Opciones adicionales comunes, por si fueran necesarias:  
      1. Especifica la versión de Python que se utilizará para crear el entorno virtual.  
        virtualenv --python=/ruta/a/python \<.nombre_del_entorno>  
      2. Muestra la ayuda completa del comando virtualenv, listando todas las opciones disponibles.  
        virtualenv -h  
        virtualenv --help  
      3. Pasos para eliminar el entorno virtual creado.  
                pip uninstall virtualenv  
         1. Desactivar el entorno virtual actual (si está activo):  
        deactivate  
         2. Eliminar la carpeta del entorno virtual creado:  
        rmvirtualenv \<.nombre_del_entorno>  
        rm -rf \<.nombre_del_entorno>  
      4. Si necesitamos desinstalar `Virtualenv` sería el comando:  
        pip uninstall virtualenv  
   4. Comprobamos en el sistema de archivos `explorer` de `VScode` que se haya creado con éxito el entorno virtual creado, que será una carpeta con ese nombre.  
6. Si nuestro entorno virtual \<.nombre_del_entorno> se creo correctamente, en la consola de comandos aparecerá su nombre entre paréntesis.
7. Se deberá seleccionar el intérprete desde la Paleta de Comandos (Ctrl+Shift+P) cada vez que trabajemos en el proyecto.  

# Creando archivos de configuración en un proyecto.

Para que nuestro entorno esté configurado de manera independiente en cada proyecto, es recomendable (casi absolutamente necesario) crear un archivo de configuración de usuario `settings.json` para que así `VScode` sepa que interpréte Python usa en cada proyecto y no sea necesario decírselo cada vez que cambiemos entre proyectos.  
A parte si queremos también emplear el Debugger, deberemos crear ahora, o más adelante un archivo `launch.json`.  

Es necesario crear una carpèta `.vscode` dentro de la carpeta principal del proyecto, dónde van alojadas los archivos de configuración (`settings.json` y `launch.json`).  
Se puede crear usando el menú contextual, clicando con el botón del ratón derecho sobre la carpeta principal del proyecto y seleccionar `New Folder`.  
Dentro de la carpeta `.vscode` creamos ambos archivos. Con el menú contextual del botón derecho del ratón y seleccionando `New File`.

## Configurar archivo `settings.json`

¿Por qué es importante settings.json para el entorno virtual?  
1. Aislamiento: Al especificar el intérprete dentro del entorno virtual, aseguras que VS Code utilice las librerías instaladas dentro de ese entorno y no las librerías globales de tu sistema.  
2. Funcionalidades de VS Code: La extensión de Python utiliza esta configuración para todas las funcionalidades relacionadas con Python en tu proyecto, como ejecutar scripts, depurar, linting, formatting, IntelliSense, etc.  

Aquí tienes una estructura básica con explicaciones y opciones:  
```JSON
{
    // Configuración general de Python
    "python.pythonPath": "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\python.exe", // Ruta al intérprete de Python del entorno virtual
    "python.envFile": "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\activate", // (Opcional) Archivo de activación del entorno virtualProyecto\\
    "python.terminal.activateEnvironment": true, // Activa el entorno virtual en el terminal

    // Configuración del linter ("pylint", "flake8", "mypy", "bandit" para seguridad, etc.)
    "python.linting.enabled": true,
    "python.linting.linter": "pylint", // Asigna el que tienes instalado en tu entorno virtual
    "python.linting.pylintPath": "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\pylint.exe", // Ruta al ejecutable del linter
    // Opcional: Configuración específica del linter
    "python.linting.pylintArgs": [
        "--rcfile=${workspaceFolder}\\.pylintrc", // Si tienes un archivo de configuración
        "--errors-only"
    ],
    // Para flake8:
    // "python.linting.flake8Path": "${workspaceFolder}\\.venv\\Scripts\\flake8.exe",
    // "python.linting.flake8Args": [
    //     "--max-line-length=120",
    //     "--ignore=E501,W503"
    // ],
    // Para mypy (requiere instalación con pip install mypy):
    // "python.linting.mypyPath": "${workspaceFolder}\\.venv\\Scripts\\mypy.exe",
    // "python.linting.mypyArgs": [
    //     "--strict",
    //     "--ignore-missing-imports"
    // ],

    // Configuración del formateador de código (autopep8, black)
    "python.formatting.provider": "black", // Asigna el que tienes instalado en tu entorno virtual
    "python.formatting.autopep8Path": "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\autopep8.exe", // Ruta al ejecutable de autopep8
    "python.formatting.blackPath": "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\black.exe", // Ruta al ejecutable de black
    // Opcional: Configuración específica del formateador
    "python.formatting.autopep8Args": [
        "--max-line-length=120"
    ],
    "python.formatting.blackArgs": [
        "--line-length",
        "120"
    ],
    "editor.formatOnSave": true, // Formatear automáticamente al guardar

    // Configuración de IntelliSense (pylance es el recomendado)
    "python.languageServer": "Pylance",
    // Opcional: Configuración específica de Pylance
    "python.analysis.typeCheckingMode": "basic", // O "strict", "off"

    // Configuración del entorno de pruebas (unittest, pytest)
    "python.testing.framework": "pytest", // O "unittest"
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.unittestRootDirectory": "${workspaceFolder}", // Directorio raíz para buscar pruebas de unittest
    "python.testing.pytestArgs": [
        "." // Ejecutar pruebas en el directorio actual y subdirectorios
    ],
    // Para unittest:
    // "python.testing.unittestEnabled": true,
    // "python.testing.pytestEnabled": false,
    // "python.testing.unittestPattern": "test_*.py", // Patrón para encontrar archivos de prueba
    // "python.testing.cwd": "${workspaceFolder}" // Directorio de trabajo para las pruebas

    // Otras configuraciones útiles
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}\\${env:PYTHONPATH}" // Asegura que PYTHONPATH incluya el workspace
    }
}
```

Explicación de cada sección y recomendaciones:  

1. `python.pythonPath:`  
Importante: Esta es la configuración crucial. Debes establecer la ruta absoluta al ejecutable python.exe dentro de tu entorno virtual.  
Recomendación: Asumiendo que tu entorno virtual se llama .venv y está ubicado en la raíz de tu proyecto, la ruta suele ser "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\python.exe". Ajusta la ruta si tu entorno virtual tiene un nombre o ubicación diferente.  
"${workspaceFolder}": Esta variable de VS Code representa la ruta al directorio raíz de tu proyecto abierto.  

2. `python.envFile:`  
Opcional pero útil: Puedes especificar la ruta al script de activación de tu entorno virtual (activate para cmd o PowerShell). Aunque python.pythonPath suele ser suficiente para que VS Code detecte el entorno, esto puede ayudar en algunos casos o para otras extensiones.  
Recomendación: Para entornos virtuales creados con venv, la ruta suele ser "${workspaceFolder}\\Proyecto\\.venv\\Scripts\\activate".  

3. `python.linting:` Configuración del Linter:  
Recomendación: Activa el linter ("python.linting.enabled": true) para identificar errores de sintaxis, problemas de estilo y posibles errores en tu código.  
"python.linting.linter": Elige el linter que prefieras ("pylint", "flake8", "mypy", "bandit" para seguridad, etc.). Asegúrate de que el linter esté instalado en tu entorno virtual (pip install pylint o el nombre del linter que elijas).  
"python.linting.pylintPath", "python.linting.flake8Path", "python.linting.mypyPath": Especifica la ruta al ejecutable del linter dentro de tu entorno virtual.  
"python.linting.<linter>Args": Puedes pasar argumentos específicos al linter. Por ejemplo, para usar un archivo de configuración (.pylintrc o .flake8), ignorar ciertos errores o establecer la longitud máxima de línea.  

Linters (para análisis estático de código):  
- Pylint: Uno de los linters más completos y configurables. Puede detectar una amplia gama de problemas de estilo y posibles errores. Requiere configuración (a través de un archivo .pylintrc).  
- Flake8: Un linter popular que combina PyFlakes (para errores lógicos), pycodestyle (para estilo PEP 8) y McCabe (para complejidad ciclomática). Es más rápido y menos configurable que Pylint, pero a menudo es un buen punto de partida.  
- mypy: Un verificador de tipos estático opcional. Te ayuda a encontrar errores relacionados con los tipos de datos en tu código Python (requiere el uso de anotaciones de tipo).  
- Bandit: Un linter específicamente diseñado para encontrar problemas de seguridad en el código Python.  


1. `python.formatting:` Configuración del Formateador de Código:  
Recomendación: Utiliza un formateador de código ("autopep8" o "black") para mantener un estilo de código consistente automáticamente. Asegúrate de que el formateador esté instalado en tu entorno virtual (pip install autopep8 o pip install black).  
"python.formatting.provider": Elige el formateador.  
"python.formatting.autopep8Path", "python.formatting.blackPath": Especifica la ruta al ejecutable del formateador dentro de tu entorno virtual.  
"python.formatting.<formatter>Args": Pasa argumentos específicos al formateador, como la longitud máxima de línea.  
"editor.formatOnSave": true: Activa el formateo automático cada vez que guardas un archivo. ¡Muy recomendable!  

Formateadores de Código (para aplicar un estilo consistente):  
- Black: Un formateador de código "opinionado" que impone un estilo consistente con mínimas opciones de configuración. Es muy popular por su simplicidad y por eliminar las discusiones sobre el formato.  
- Autopep8: Un formateador que intenta formatear el código para que cumpla con la guía de estilo PEP 8. Ofrece más opciones de configuración que Black.  

1. `python.languageServer:` Configuración del Language Server:  
Recomendación: "Pylance" es el Language Server recomendado por Microsoft para Python en VS Code. Ofrece características avanzadas como autocompletado, verificación de tipos y navegación de código.  
"python.analysis.typeCheckingMode": Si usas Pylance, puedes configurar el nivel de verificación de tipos ("basic", "strict", "off"). Para un análisis estático más riguroso, considera "strict" (requiere anotaciones de tipo).  

1. `python.testing:` Configuración del Entorno de Pruebas:  
Recomendación: Configura el framework de pruebas que utilizas ("unittest" o "pytest"). Asegúrate de que el framework esté instalado en tu entorno virtual (pip install pytest).  
"python.testing.framework": Elige el framework.  
"python.testing.<framework>Enabled": Activa el framework seleccionado.  
"python.testing.unittestRootDirectory" / "python.testing.pytestArgs": Especifica la ubicación de tus archivos de prueba y cualquier argumento adicional para el ejecutor de pruebas.  
"python.testing.cwd" (para unittest): Establece el directorio de trabajo para ejecutar las pruebas.  

Extensión recomendada: "**Python Test Explorer UI (por LittleFoxTeam)**": Proporciona una interfaz gráfica para ejecutar y ver los resultados de tus pruebas unitarias (unittest, pytest, etc.).  

1. Otras configuraciones útiles
"terminal.integrated.env.windows": Esta configuración asegura que la variable de entorno PYTHONPATH dentro de la terminal integrada de VS Code incluya la raíz de tu proyecto. Esto puede ser útil si tienes dependencias o módulos relativos a tu espacio de trabajo.  

## Configurar archivo `launch.json`

El archivo launch.json se utiliza para configurar cómo se debe ejecutar tu aplicación Python cuando la depuras. Aquí también debes asegurarte de que se utilice el intérprete correcto (el del entorno virtual).  
Te propongo la siguiente configuración en tu launch.json. Esta configuración asume que quieres ejecutar y depurar el archivo actualmente abierto en el editor, y que el directorio de trabajo debe ser la carpeta donde se encuentra ese archivo.  
```JSON
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true, // Indica al depurador que se centre únicamente en tu código fuente y que omita el código de las bibliotecas estándar de Python y de los paquetes de terceros que hayas instalado.
            "cwd": "${fileDirname}", // Establece el directorio del archivo como directorio de trabajo
            "python": "${command:python.interpreterPath}" // Utiliza el intérprete de Python seleccionado en VS Code
        },
        {
            "name": "Python: Current File (Debugger)",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true, // Indica al depurador que se centre únicamente en tu código fuente y que omita el código de las bibliotecas estándar de Python y de los paquetes de terceros que hayas instalado.
            "cwd": "${fileDirname}", // Establece el directorio del archivo como directorio de trabajo
            "python": "${command:python.interpreterPath}" // Utiliza el intérprete de Python seleccionado en VS Code
        }
    ]
}
```

## Añadiendo y configurando un archivo `tasks.json`.

El archivo `tasks.json` se puede crear  dentro de la carpeta de configuraciones `.vscode` usando el menú contextual, clicando con el botón del ratón derecho sobre la carpeta principal del proyecto y seleccionar `New File`.  

Ventajas de la configuración propuesta a continuación:  
1. Utiliza el intérprete configurado: Asegura que tu script se ejecute con el intérprete de Python correcto, especialmente si estás utilizando un entorno virtual.  
2. Ejecución rápida: Te permite ejecutar el archivo actual directamente desde VS Code sin tener que abrir una terminal y escribir el comando manualmente. Puedes ejecutar la tarea desde el menú "Ejecutar tarea" o configurando un atajo de teclado personalizado.  
3. Directorio de trabajo consistente: Al establecer el directorio de trabajo en la raíz del espacio de trabajo, facilita el manejo de rutas relativas dentro de tu script.  

```JSON
// El archivo tasks.json en Visual Studio Code (VS Code) se utiliza para automatizar tareas dentro de tu flujo de trabajo de desarrollo.
// Se ha añadido una configuración "Run Python File (Workspace Root)", una forma útil de configurar una tarea rápida para ejecutar el archivo Python actualmente abierto utilizando el intérprete de Python configurado para el proyecto (idealmente el de tu entorno virtual).
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Python File (Workspace Root)",
            "type": "shell",
            "command": "${config:python.pythonPath} ${file}", // Alternativa: "python ${file}"
            "options": {
                "cwd": "${workspaceFolder}"
            },
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        }
    ]
}
```

# Instalar dependencias del proyecto

Mediante `pip` instalariamos las dependencias que necesitemos o querramos para cada proyecto, y se podrían configurar en el `settings.json` del proyecto en cuestión.  
pip install flake8 bandit black

## --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- # --- #

Ejemplo de árbol de estructura de múltiples proyectos.  
Proyectos/  
├── Proyecto1/  
│   ├── .vscode/  
│   │   ├── settings.json # Configuración de VS Code para el proyecto y sus dependencias.  
│   │   ├── launch.json # Configuración de depuración guardada junto con su configuración del entorno virtual.  
│   │   └── tasks.json # Es más común para la configuración global, automatiza tareas dentro de tu flujo de trabajo de desarrollo.  
│   ├── mi_script1.py  
│   └── .virtEnv1/  
│       └── Scripts/  
│           └── python.exe  
├── Proyecto2/  
│   ├── .vscode/  
│   │   ├── settings.json
│   │   ├── launch.json
│   │   └── tasks.json
│   ├── mi_script1.py  
│   └── .virtEnv1/  
│       └── Scripts/  
│           └── python.exe  
└── Proyecto3/  
    ├── .vscode/  
    │   ├── settings.json  
    │   ├── launch.json
    │   └── tasks.json  
    ├── mi_script3.py  
    └── .virtEnv3/  
        └── Scripts/  
            └── python.exe  