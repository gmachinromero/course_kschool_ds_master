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

### 1.3.1. Navegación por directorios

**Directorio actual: pwd - print working directory**

En UNIX todos los directorios cuelgan de un directorio denominado "/". Dentro de este directorio se identifica un subdirectorio con la siguiente estructura: /home/[user]; esto es lo que se denomina el *home*.

La ruta del *home* puede ser definida con la estructura indicada en el parrafo anterior, o existe un atajo mediante el símbolo denominado virgulilla "~".

> *Para escribir la virguilla en Linux: alt gr + ñ.*

> *Para escribir la virgulilla en Windows: alt gr + 4 + space.*

Para saber en que directorio nos encontramos se escribe `pwd` en la la shell.

**Cambiar de directorio: cd - change directory**

Para cambiar de directorio se utiliza el comando: `cd [directorio_destino]`.

Con este comando existen algunos atajos que permiten navegar por el ordenador de forma más eficiente:

- `cd`: ir al home
- `cd ~`: ir al home
- `cd ../`: ir a la carpeta anterior

**Ver subdiectorios/ficheros dentro de un directorio: ls - list directory contents**

Para listar el contenido de un directorio se escribe el comando dentro del mismo directorio: `ls`.

## 1.4. Ejercicios

# 2. Git

# 3. Bibliografía

- https://towardsdatascience.com/shell-basics-every-data-scientist-should-know-3f012ef5c38c
- https://www.datascienceatthecommandline.com/1e/index.html