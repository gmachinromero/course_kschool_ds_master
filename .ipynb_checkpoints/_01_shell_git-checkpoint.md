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

Mediante este comando se pueden modificar los permisos de lectura, escritura y ejecución de los ficheros, teniendo en cuenta si la clase es usuario, grupo u otro.

El comando a utilizar es `chmod [u+rwx],[g+rwx],[o+rwx] file_name`. El símbolo `+` se sustituye por `-` si lo que se quiere es eliminar permisos de un tipo de usuario.

Existe una forma abreviada de modificar los permisos de un fichero que se indica mediante un número de tres cifras. Cada crifra atiende respectivamente a las clases: usuario, grupo y otros; y el valor de cada cifra es la suma de los diferentes permisos que se tienen dentro de una clase.

- Lectura: 4
- Escritura: 2
- Ejecución: 1

Por ejemplo, si se quiere indicar que para un fichero el usuario va a tener permisos de lectura, escritura y ejecución (rwx), y que tanto las clases de grupo y otros van a tener permisos de lectura unicamente (r), se indicaría con el comando `chmod 744`.

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

**Contabilizar registros / wc - word count:**

Muestra por consola tres datos: número de filas, palabra y bytes. La sintaxis es `wc file`.

### 1.3.4. Anaizando ficheros

**Ordenar ficheros / sort:**

Este comando permite ordenar un fichero en base a diferentes condiciones. La sintaxis es `sort [opt] file`. Algunas de las opciones más comunes son:

- `sort -d`: alfanumérico
- `sort -n`: numérico
- `sort -r`: inverso
- `sort -f`: no se tienen en cuenta mayúsculas y minúsculas

Las anteriores opciones pueden se pueden combinar entre sí. Adicionalmente, en ficheros con muchas columnas se pueden utilizar opciones más avanzadas para ordenar el mismo en base a un mayor número de parámetros:

- `sort -t "delimiter"`: indica el delimitador del fichero
- `sort -k M[,N]`: los campos clave para ordenar el fichero van desde la columna M hasta la N en caso de indicarse, si no hasta el final del fichero

**Duplicados / uniq:**

Este comando permite analizar las duplicidades dentro de un fichero, en función de las opciones de la herramienta se pueden obtener diferentes resultados. Para que este comando funcione correctamente, el fichero debe estar ordenado. La sintaxis es `uniq [opt] file`.

Algunas de las opciones más comunes son:

- `uniq -c`: añade un prefijo a las líneas con el número de ocurrencias
- `uniq -d`: solo muestra aquellos registros duplicados

Si se quieren eliminar los duplicados de un fichero, se tiene que recurrir al comando `sort -u file`.




### 1.3.5. Entradas, salidas y redirecciones

**Redirecciones:**

De forma predeterminada, el último comando ejecutado en la shell es mostrado como salida en la terminal. Esta salida se puede guardar en un fichero mediante el comando`>`. Esto se denomina redirección.

Si la información se redirecciona a un fichero que no existe este es creado automáticamente, sin embargo si ya existía, se sobreescribe. Si lo que se quiere es adjuntar información adicional a un fichero existente, se puede llevar a cabo mediante el comando `>>`.

Ejemplo:

- `head -n 10 optd_aircraft.csv > first_10_aircraft.txt`
- `tail -n 10 optd_aircraft.csv > last_10_aircraft.txt`
- `wc optd_aircraft.csv > number_of_lines.txt`

### 1.3.6. Pipeline

Como se indica al principio de este notebook, las herramientas de UNIX están pensadas para realizar una única opción pero con una eficiencia muy alta, ¿pero que ocurre cuando necesitamos realizar tareas más complejas?

En la shell existe un comando denominado pipeline `|` que concatena herramientas más sencillas, permitiendo llevar a cabo operaciones más complejas.

Ejemplo:

- `head -n 10 optd_aircraft.csv | wc`

### 1.3.7. Buscar ficheros

Cuando se trabaja con muchos ficheros, en ordenadores que no son los habituales (clusters) y donde tiene accesos mucha gente, puede darse el caso de que archivos con los que estábamos trabajando se extravíen.

En la shell contamos con la herramientas `find` que permite buscar en todos los ficheros del ordenador, filtrando por unas condiciones dadas como tamaño, formato, nombre, última fecha de modificación...etc.

La sintaxis de este comando es `find [path] [coditions]`. Algunas de las condiciones más útiles que podemos utilizar con esta herramienta son:

- `-type f`, `-type d`: fichero o directorio
- `-name`: nombre del fichero, se pueden utilizar asteriscos si no se sabe como termina un nombre por ejemplo
- `-iname`: nombre del fichero ignorando mayúsculas o minúsculas
- `-maxdepth`: máximo nivel de subdirectorios en los que se va a realizar la búsqueda a partir del directorio actual
- `-mindepth`: mínimo nivel de subdirectorios en los que se va a realizar la búsqueda a partir del directorio actual
- `-perm n`: permisos del fichero de búsqueda, donde n es un número de tres cifras que indica los permisos para cada clase
- `-size +- n`: mayor o menor tamaño que n. M para megasbytes, k para kilobytes
- `-empty`: ficheros vacios
- `-mmin -N`: ficheros modificados en los último N minutos
- `-mtime -N`: ficheros modificados en los último N días

Cualquiera de las condiciones anteriores puede invertirse si se coloca delante el símbolo `!`.


## 1.4. Ejercicios

### 1.4.1. Ejercicios navegación directorios

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


### 1.4.2. Ejercicios exploración / análisis ficheros

1. Find top 10 files by size in your home directory including the subdirectories. Sort them by size and print the result including the size and the name of the file (hint: use find with –size and -exec ls –s parameters)

2. Create a dummy file with this command : seq 15> 20lines.txt; seq 9 1 20 >> 20lines.txt; echo"20\n20" >> 20lines.txt; (check the content of file first)
a) Sort the lines of file based on alphanumeric characters
b) Sort the lines of file based on numeric values and eliminate the duplicates
c) Print just duplicated lines of the file
d) Print the line which has most repetitions
e) Print unique lines with the number of repetitions sorted by the number of repetitions from lowest to highest

3. Create another file with this command : seq 0 2 40 > 20lines2.txt
a) Create 3rd file combining the first two files (20lines.txt and 20lines2.txt) but without duplicates
b) Merge the first two files. Print unique lines together with the number of occurrences inside the merged file and sorted based on
line content.

4. Go to ~/Data/opentraveldata Get the line with the highest number of engines from optd_aircraft.csv by using sort.

### 1.4.3. Ejercicios búsqueda ficheros

1. Find all files located inside subdirectories of your home directory which have been modified in last 60min

> `find . -type f -mmin -60 `

2. Find all empty files inside subdirectories of your home directory which do NOT have read-write-execute permissions given to all users

> `find . -mindepth 2 -type f -empty ! -perm 777`

3. Expand previous command to grant these permissions using “ok” option.

> `find . -mindepth 2 -type f -empty ! -perm 777 -ok chmod 777 {} \;`

4. Get top 3 largest files per subdirectory inside ~/Data/

> `find . -mindepth 1 -type d -exec echo {} \; -exec zsh -c "ls -lS {} | head 3" \;`

# 2. Git

# 3. Bibliografía

- https://towardsdatascience.com/shell-basics-every-data-scientist-should-know-3f012ef5c38c
- https://www.datascienceatthecommandline.com/1e/index.html