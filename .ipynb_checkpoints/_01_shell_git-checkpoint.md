# 1. Linux Shell

## 1.1. Intro

Aunque a primera vista podría parecer que esta herramienta está un poco desfasada, y que no habría necesidad hoy en día de utilizar una aplicación con una interfaz gráfica tan arcaica y obsoleta, lo cierto es que tener unos conocimientos básicos de línea de comandos puede ser terriblemente útil en las tareas diarias de un data scientist.

La filosofía que subyace detrás de la línea de comandos es la misma que la de UNIX, la filosofía de las herramientas simples, es decir, cada herramienta puede realizar una única tarea pero con un grado de eficiencia muy alto. Por lo que concatenando de la manera correcta una serie de ordenes simples, se pueden llevar a cabo tareas complejas de forma muy eficiente.

Otro motivo por el que puede ser interesante tener conocimientos de shell a parte de su efectividad, es que cuando se trabaja con grandes volúmenes de datos empieza a ser necesario necesario contar con capacidades de computación superiores y esto solo es posible conectándose a un grupo de servidores o clúster. Pues bien, lo más seguro es que un cluster no tenga una GUI (graphical user interface) habilitada, y la comunicación sea exclusivamente a través de una shell.

## 1.2. Terminología

La arquitectura de cualquier sistema UNIX o basado en el, está definido más o menos en cuatro capas. A continuación se listan en orden descendente:

- Línea de comandos: Herramientas paa escribir los comandos.
- Terminal: Herramienta donde se escriben los comandos. Una vez introducidos en la terminal, ésta los envía a la shell.
- Shell: Programa que interpreta los comandos enviados por la terminal.
- Sistema operativo

## 1.3. Comandos

En los siguientes apartados se explican por temáticas los comandos que pueden ser de mayor utilidad a la hora de trabajar con la línea de comandos.

Se incluyen en este apartado algunos comandos que pueden ser de ayuda para saber más acerca de otros comandos:

- `man tool`: muestra el manual de la herramientas en cuestión, no todas las herramientas tienen manual.
- `tool --help`: muesra ayuda sobre la herramienta.
- `type tool`: indica información sobre la herramienta, si es un alias de otra herramienta o donde se aloja.

### 1.3.1. Navegación por directorios

**Directorio actual / pwd - print working directory:**

En UNIX todos los directorios cuelgan de un directorio denominado "/". Dentro de este directorio se identifica un subdirectorio con la siguiente estructura: /home/[user]; esto es lo que se denomina el *home*.

La ruta del *home* puede ser definida con la estructura indicada en el parrafo anterior, o existe un atajo mediante el símbolo denominado virgulilla "~".

> *Para escribir la virguilla en Linux: alt gr + ñ.*

> *Para escribir la virgulilla en Windows: alt gr + 4 + space.*

Para saber en que directorio nos encontramos se escribe `pwd` en la la shell.

**Cambiar de directorio / cd - change directory:**

Para cambiar de directorio se utiliza el comando: `cd dir_dest`.

Con este comando existen algunos atajos que permiten navegar por el ordenador de forma más eficiente:

- `cd`: ir al home
- `cd ~`: ir al home
- `cd ..`: ir a la carpeta anterior
- `cd -`: ir a la carpeta anterior

**Listar contenido dentro de un directorio / ls - list directory contents:**

Para listar el contenido de un directorio se escribe el comando dentro del mismo directorio: `ls [opt]`. Este comando se puede acompañar de argumentos adicionales para modificar la salida, algunos de los más utilizados son:

- `ls -a`: lista todo el contenido incluso el oculto.
- `ls -l`: lista el contenido añadiendo información adicional como permisos de escritura, tamaño y tipo de fichero.

### 1.3.2. Creación y modificación de directorios y ficheros

**Modificar permisos / chmod - change mode:**

Mediante este comando se pueden modificar los permisos de lectura, escritura y ejecución de los ficheros, teniendo en cuenta si el usuario es usuario, grupo u otro.

El comando a utilizar es `chmod [u+rwx],[g+rwx],[o+rwx] file_name`. El símbolo `+` se sustituye por `-` si lo que se quiere es eliminar permisos de un tipo de usuario.

**Crea directorio / mkdir - make directory:**

Mediante este comando se pueden crear directorios/subdirectorios en la ruta en la que se ejecuta. El comando a utilizar es `mkdir [opt] dir_name`.

Algunos casos de usos interesantes son:

- `mkdir dir_name_1] dir_name_2`: crear diferentes directorios a la vez, todos alojados en el directorio padre.
- `mkdir -p dir_name_1/dir_name_2`: crea un directorio 1, y el resto los va anidando.

**Crear fichero / touch - make directory:**

Este comando permite crear un fichero en blanco, o si ya existe, modificar su fecha de moficación a la actual. El comando a utilizar es `touch file_name[.ext]`.

**Copiar ficheros y directorios / cp - copy:**

Este comando permite copiar ficheros/directorios de un lugar a otro. La sintaxis es `cp [opt] org_source dest_source`. Si se trabaja con directorios es necesario indicarlos mediante el comando `cp -r`.

**Mover ficheros y directorios / mv - move:**

Este comando permite mover ficheros/directorios de un lugar a otro. La sintaxis es `mv [opt] org_source dest_source`.

**Renombrar ficheros y directorios / mv - move:**

Sí, está bien y no se trata de un error, mediante el mismo comando anterior también se pueden renombrar los ficheros y directorios. En verdad lo que sea realiza en este caso es un mover un fichero de un directorio a ese mismo directorio, pero con otro nombre. La sintaxis es `mv (opt) [org_name] [dest_name]`.

**Eliminar ficheros y directorios / rm - remove:**

Este comando permite eliminar ficheros de un directorio. La sintaxis es `rm [opt] file/dir`. Si se trabaja con directorios es necesario indicarlos mediante el comando `rm -r`.

### 1.3.3. Explorar ficheros

**Visualizar fichero interactivo / less:**

Muestra información de un fichero de forma interactiva, la linea de comandos permite navegar por el fichero con algunas teclas. La sintaxis es `less file`.

**Visualizar fichero completo / cat:**

Muestra por consola el contenido completo de un fichero, hay que tener cuidado si son muy grandes. La sintaxis es `cat file`.

**Visualizar las primeras K líneas de un fichero / head:**

Muestra por consola las primeras líneas que definamos de un fichero. La sintaxis es `head -n K file`.

**Visualizar las últimas K líneas de un fichero / tail:**

Muestra por consola las últimas líneas que definamos de un fichero. La sintaxis es `tail -n K file`.

## 1.4. Ejercicios

1. Create a directory “first_dir” in you home folder:

> `cd ~`
> `mkdir first_dir`

2. Create an empty file “text_file.txt” inside “first_dir” directory.

> `cd ~/first_dir`
> `touch text_file.txt`

3. Add execute permissions to group users, and write permissions to other users to “text_file.txt”

> `cd ~/first_dir`
> `chmod u+x,o+w text_file.txt`

4. Create 3 subdirectories inside “first_dir”: “sub1”, “sub2”, “text_file”

> `cd ~/first_dir`
> `mkdir sub1 sub2 text_file`

5. Copy the “text_file.txt” file into “sub1” directory.

> `cd ~/first_dir`
> `cp text_file.txt sub1`

6. Move the “text_file.txt” into sub2 under name “text_file.txt.2”.

> `cd ~/first_dir`
> `mv text_file.txt sub2/text_file.txt.2`

7. Copy the whole directory “sub1” to “sub3” directory.

> `cd ~/first_dir`
> `cp -r sub1 sub3`

8. Change file name of “first_dir /sub2/text_file.txt.2” to “first_dir /sub2/text_file.txt.backup”

> `cd ~/first_dir/sub2`
> `mv text_file.txt.2 text_file.txt.backup`

9. Move “first_dir /sub2/text_file.txt.backup” to “first_dir” directory as hidden file

> `cd ~/first_dir/sub2`
> `mv text_file.txt.2 first_dir/.text_file.txt.backup`

10. Delete the “sub2” subdirectory

> `cd ~/first_dir`
> `rm -r sub2`

# 2. Git

# 3. Bibliografía

- https://towardsdatascience.com/shell-basics-every-data-scientist-should-know-3f012ef5c38c
- https://www.datascienceatthecommandline.com/1e/index.html