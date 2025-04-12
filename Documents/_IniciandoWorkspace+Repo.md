# Preparación de Visual Studio Code
## Iniciando un nuevo Workspace y vincularlo con un repositorio de GitHub

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

# Creando carpetas como un proyecto