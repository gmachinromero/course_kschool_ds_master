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

### 1.3.3. Exploración de ficheros

**Visualizar fichero interactivo / less:**

Muestra información de un fichero de forma interactiva, la linea de comandos permite navegar por el fichero con algunas teclas. La sintaxis es `less file`.

**Visualizar fichero completo / cat:**

Muestra por consola el contenido completo de un fichero, hay que tener cuidado si son muy grandes. La sintaxis es `cat file`.

**Visualizar las primeras K líneas de un fichero / head:**

Muestra por consola las primeras líneas que definamos de un fichero. La sintaxis es `head -n K file`.

**Visualizar las últimas K líneas de un fichero / tail:**

Muestra por consola las últimas líneas que definamos de un fichero. La sintaxis es `tail -n K file`.

**Contabilizar registros / wc - word count:**

Muestra por consola tres datos: número de filas, palabra y bytes. La sintaxis es `wc [opt] file`. Algunas de las opciones más comunes son:

- `wc -c`: muestra el número de bytes del fichero
- `wc -m`: muestra el número de caracteres
- `wc -l`: muestra el número de lineas
- `wc -w`: muestra el número de palabras

**Ordenar ficheros / sort:**

Este comando permite ordenar un fichero en base a diferentes condiciones. La sintaxis es `sort [opt] file`. Algunas de las opciones más comunes son:

- `sort -d`: alfanumérico
- `sort -n`: numérico
- `sort -r`: inverso
- `sort -f`: no se tienen en cuenta mayúsculas y minúsculas

Las anteriores opciones pueden se pueden combinar entre sí. Adicionalmente, en ficheros con muchas columnas se pueden utilizar opciones más avanzadas para ordenar el mismo en base a un mayor número de parámetros:

- `sort -t "delimiter"`: indica el delimitador del fichero
- `sort -k M[,N]`: los campos clave para ordenar el fichero van desde la columna M hasta la N en caso de indicarse, si no hasta el final del fichero. Índice 1.

**Duplicados / uniq:**

Este comando permite analizar las duplicidades dentro de un fichero, en función de las opciones de la herramienta se pueden obtener diferentes resultados. Para que este comando funcione correctamente, el fichero debe estar ordenado. La sintaxis es `uniq [opt] file`.

Algunas de las opciones más comunes son:

- `uniq -c`: añade un prefijo a las líneas con el número de ocurrencias
- `uniq -d`: solo muestra aquellos registros duplicados

Si se quieren eliminar los duplicados de un fichero, se tiene que recurrir al comando `sort -u file`.

### 1.3.4. Procesamiento y filtrado de ficheros

**Extraer columnas / cut:**

Este comando permite extraer de un fichero solo aquellas columnas con las que se vaya a trabajar. La sintaxis es `cut [opt] file`.

Algunas de las opciones más comunes son:

- `cut -d ["delimiter"]`: indicar el delimitador que separa las columnas, por defecto es TAB.
- `cut -f K[-M][,N]`: indica las columnas a extraer. Índice 1.
- `cut --output-delimiter`: indica el delimitador del fichero de salida, por defecto es el mismo que el de entrada.

Ejemplo:

- `cut -d "^" -f 1-3,5 --output-delimiter "," optd_aircraft.csv | head`

**Concatenar horizontal / paste:**

Este comando permite trasponer de forma horizontal, los registros de un fichero. La sintaxis es `paste [opt] file_1 file_2`.

Algunas de las opciones más comunes son:

- `paste -d ["delimiter"]`: indica el delimitador de la concatenación, po defecto es TAB. Si se indican varios se van utilizando alternativamente.
- `paste -s`: concatena o¡los ficheros de forma hoizontal, y luego traspone los resultados.

**Reemplazar caracteres / tr:**

Este comando permite eliminar o reemplazar los caracteres que cumplan una condicion (set1) por otros (set2). La sintaxis es `tr [opt] set1 [set2]`. Los sets pueden ser conjuntos de caracteres 

Algunas de las opciones más comunes son:

- `tr -s`: reemplaza todos los caracteres iguales que sean adyacentes.
- `tr -d`: elimina los caracteres indicados en el set1.
- `tr -c`: conserva solo aquellos caracteres indicados en el set1.

En los sets se pueden pasar como argumentos clases predefinidas de caracteres como: `[:digit:]`, `[:alpha:]`...etc.



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

1. Create a directory “first_dir” in you home folder

> `cd ~`
> `mkdir first_dir`

2. Create an empty file “text_file.txt” inside “first_dir” directory

> `cd ~/first_dir`
> `touch text_file.txt`

3. Add execute permissions to group users, and write permissions to other users to “text_file.txt”

> `cd ~/first_dir`
> `chmod u+x,o+w text_file.txt`

4. Create 3 subdirectories inside “first_dir”: “sub1”, “sub2”, “text_file”

> `cd ~/first_dir`
> `mkdir sub1 sub2 text_file`

5. Copy the “text_file.txt” file into “sub1” directory

> `cd ~/first_dir`
> `cp text_file.txt sub1`

6. Move the “text_file.txt” into sub2 under name “text_file.txt.2”

> `cd ~/first_dir`
> `mv text_file.txt sub2/text_file.txt.2`

7. Copy the whole directory “sub1” to “sub3” directory

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

> `find ~ -type f -size +10M -exec ls -sh {} \; | sort -nr | head`

2. Create a dummy file with this command: seq 15 > 20lines.txt; seq 9 1 20 >> 20lines.txt; echo"20\n20" >> 20lines.txt; (check the content of file first)

- Sort the lines of file based on alphanumeric characters

> `sort -d 20lines.txt`

- Sort the lines of file based on numeric values and eliminate the duplicates

> `sort -nu 20lines.txt`

- Print just duplicated lines of the file

> `sort -n 20lines.txt | uniq –d`

- Print the line which has most repetitions

> `sort -n 20lines.txt | uniq -d -c | sort -nr | head -1`

> `sort -n 20lines.txt | uniq -d -c | sort -n | tail -1`

- Print unique lines with the number of repetitions sorted by the number of repetitions from lowest to highest

> `sort -n 20lines.txt | uniq -c | sort -nr`

3. Create another file with this command: seq 0 2 40 > 20lines2.txt

- Create 3rd file combining the first two files (20lines.txt and 20lines2.txt) but without duplicates

> `sort -nu 20lines.txt 20lines2.txt > 20files_no_dupl.txt`

- Merge the first two files. Print unique lines together with the number of occurrences inside the merged file and sorted based on line content.

> `sort 20lines2.txt 20lines.txt | uniq -c | sort -k 2n,2`

4. Go to ~/Data/opentraveldata and get the line with the highest number of engines from optd_aircraft.csv by using sort.

> `sort -t "^" -k 7nr,7 optd_aircraft.csv | head -1`

### 1.4.3. Ejercicios procesamiento y filtrado de ficheros

1. Change the delimiter of optd_aircraft.csv to “,”

> `cat optd_aircraft.csv | tr "^“ ","`

2. Check if optd_por_public.csv has repeated white spaces (hint: use tr with wc)

> `wc optd_por_public.csv`

> `cat optd_por_public.csv | tr -s "[:blank:]" | wc`

> `Compare the results!`

3. How many columns has optd_por_public.csv? (hint: use head and tr)

> `head -n 1 optd_por_public.csv| tr "^" " " | wc`

> `head -n 1 optd_por_public.csv| tr "^" "\n" | wc`

4. Print column names of optd_por_public.csv together with their column number. (hint: use paste)

> `paste <(seq 46) <(head -1 optd_por_public.csv | tr "^" "\n")`

5. Use optd_airlines.csv to obtain the airline with the most flights

> `cat optd_airlines.csv | cut -d "^" -f 8,14 | sort -t "^" -k 2nr,2 | head -1`

6. Use optd_airlines.csv to obtain number of airlines in each alliance

> `cat optd_airlines.csv| cut -d "^" -f 10 | sort| uniq -c | sort -rn | head`

### 1.4.4. Ejercicios búsqueda ficheros

1. Find all files located inside subdirectories of your home directory which have been modified in last 60min

> `find . -type f -mmin -60 `

2. Find all empty files inside subdirectories of your home directory which do NOT have read-write-execute permissions given to all users

> `find . -mindepth 2 -type f -empty ! -perm 777`

3. Expand previous command to grant these permissions using “ok” option.

> `find . -mindepth 2 -type f -empty ! -perm 777 -ok chmod 777 {} \;`

4. Get top 3 largest files per subdirectory inside ~/Data/

> `find . -mindepth 1 -type d -exec echo {} \; -exec zsh -c "ls -lS {} | head 3" \;`

# 2. Git

## 2.1. Intro

Git es un software de control de versiones diseñado por Linus Torvalds, pensando en la eficiencia y la confiabilidad del mantenimiento de versiones de aplicaciones cuando éstas tienen un gran número de archivos de código fuente. Su propósito es llevar registro de los cambios en archivos de computadora y coordinar el trabajo que varias personas realizan sobre archivos compartidos.

Git presenta una arquitectura distribuida, es un ejemplo de DVCS (sistema de control de versiones distribuido, por sus siglas en inglés). En lugar de tener un único espacio para todo el historial de versiones del software, como sucede de manera habitual en los sistemas de control de versiones de antaño más populares como CVS o Subversion (también conocido como SVN), en Git, la copia de trabajo del código de cada desarrollador es también un repositorio que puede albergar el historial completo de todos los cambios

Fundamentalmente, un proyecto Git se estructura en tres áreas:

- Working directory: es donde se alojan todos nuestros ficheros, y el lugar donde se trabaja constantemente.
- Staging area: es donde se alojan los ficheros que han sido modificados, y que aceptamos para que vayan en una futura revisión.
- local/remote repo: es donde se almacena la revisión completa, y puede ser local y/o remoto.

<img src="_images\git_structure.png" alt="Drawing" style="width: 400px;"/>

## 2.2. Terminología

A continuación se listan los términos que se utilizan con mayor frecuencia dentro de Git, y su dfeinición:

- Repositorio: todo directorio que está siendo monitorizado por Git, es decir, tiene un historial de todas las modificaciones que se van registrando en cada uno de los componentes de ese directorio.
- Commit: cada uno de los cambios registrado en el historial de un repositorio.
- Master: rama principal del proyecto
- Branch: ramificaciones o bifurcaciones del proyecto master donde se trabajan funcionalidades nuevas de forma aislada. De este modo se pueden testear modificaciones en el código, sin comprometer el resto del proyecto.
- Fork: es un proyecto diferente que se crea a partir de otro.

## 2.3. Comandos

### 2.3.1. Congifurar Git

Cada vez que actualicemos nuestro código a una nueva versión en el repositorio, aparecerá registrado con estos datos que hemos configurado. De esta forma, cuando subamos los cambios al repositorio remoto, cada revisión del código irá registrada al nombre del programador que ha efectuado los cambios.

Para configurar nuestro usuario, basta con ejecutar los siguientes dos comandos:

- `git config --global user.name "user"`
- `git config --global user.email "user@email.com"`

También se puede viausalizar a través del terminal, la configuración actual de Git mediante el comando `git config --list`.

### 2.3.2. Comandos asociados a repos

**Crear un repositorio / git init:**

Este comando convierte una directorio local, en un repo de Git, y lo prepara para empezar a trabajar bajo este marco de trabajo. Para convertir un directorio en un repo se ejecuta el comando `git init` dentro del directorio que queremos transformar.

Mediante este comando lo que en verdad ocurre es que se crea un directorio denominado *.git*, donde se documenta todo el historial de los cambios. Si se elimanara este directorio, la carpeta dejaría de ser un repo.

En el caso de que queramos tener archivos en nuestro directorio que no se encuentren en el repositorio, se puede crear un archivo que se llame *.gitignore* donde alojaremos el nombre (permite utilizar *wildcards*) de los ficheros que no queramos que sean públicos.

**Añadir fichero al staging area / git add:**

Este comando añade los ficheros que no estén trackeados, al staging area. La sintaxis de este comando es `git add [file]`.

**Eliminar fichero del staging area / git rm:**

Este comando permite eliminar fucheros trackeados del staging area. La sintaxis de este comando es `git rm .cached file`

**Añadir ficher al repo / git commit:**

Una vez los ficheros están trackeados en el staging area, podemos enviarlos al repo mediante el comando `git commit`.

Una buena práctica a la hora de realizar un commit es incluír un comentario en el que se indique la naturaleza, motivación y alcance del mismo. Para ello se puede utilizar el comando `git commit -m ["comment"]`.

**Sincronizar nube con repo local / git push:**

Mediante este comando se puede envíar realizar una copia del repo local en la nube, de este modo, si otras personas estám colaborando en el mismo proyecto, podrán descargar en sus repos locales las modificaciones.

Para subir un repo local a uno en la nube, se ejecuta el comando `git push origin master`.

**Clonar un repo / git clone:**

Este comando permite clonar un repo que se encuentre en Git. Una vez se tenga el repo en local se podrá empezar a trabajar con el. Este comando se utiliza cuando se quiere descargar un repo por primera vez.

Para clonar un repo se puede utilizar el comando `git clone [url]`.

**Sincronizar repo local con la nube / git pull:**

Mediante este comando podemos descargar las modificaciones que hayan tenido lugar en un repo en la nube, y sincronizar de este modo nuestro repo local.

Para alinear el repo local con las modificaciones de la nube, se ejecuta el comando `git pull origin master`.

**Analizar diferencias de un repo / git diff:**

Este comando permite visualizar las diferencias que existen entre un fichero que se encuentra en el working area y que ha sido modificado, frente a la versión alojada en el repo.

Para utilizar esta función basta con ejecutar `git diff` en el repo en cuestión.

**Histórico del repo / git log:**

Mediante el comando `git log` se puede obtener el histórico de modificaciones asociadas a un repositorio.

# 3. Bibliografía

- KSchool Data Science Master Ed. 23.
- https://towardsdatascience.com/shell-basics-every-data-scientist-should-know-3f012ef5c38c
- https://www.datascienceatthecommandline.com/1e/index.html
- https://es.wikipedia.org/wiki/Git
- https://www.atlassian.com/es/git/tutorials/what-is-git
- https://www.git-scm.com/doc