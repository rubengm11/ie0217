Este es el archivo README.md de la tarea 1.

# Instrucciones de utilizacion del programa:

- El archivo Makefile contiene los siguientes targets:

1. clean: Limpia el directorio de archivos compilados y deja nicamente el codigo fuente.
2. build: compila el codigo fuente y genera un ejecutable llamado adivina.x.
3. run: Ejecuta el programa adivina.x
4. all: compila y corre el juego.


# Respuestas las partes teoricas de la tarea.

1.	Ambos lenguajes comparten muchas similitudes y comparten gran parte de la sintaxis, pero C++ agrega características que permiten la programación orientada a objetos, un mejor manejo de memoria y librerías estándar adicionales.

2.	En un lenguaje compilado, el código fuente se traduce por completo a un código de máquina específico de la arquitectura del sistema antes de la ejecución. El resultado de esta traducción es un programa ejecutable independiente. En un lenguaje interpretado, el código fuente se traduce y ejecuta línea por línea en tiempo de ejecución por un intérprete. No se genera un archivo ejecutable independiente antes de la ejecución.
Ejemplos de casos donde sería óptimo utilizar un lenguaje compilado: Desarrollo de sistemas operativos, programación de sistemas embebidos donde se requiere un control preciso del hardware, aplicaciones que necesitan rendimiento máximo, como juegos o software de procesamiento intensivo.
Ejemplos de casos donde sería óptimo utilizar un lenguaje interpretado: Desarrollo web, donde la flexibilidad y la facilidad de actualización son críticas, tareas automatizadas o secuencias de comandos.

3.	Es una herramienta esencial en el proceso de compilación. Su función principal es combinar y vincular los archivos objeto generados durante la fase de compilación para producir un programa ejecutable o una biblioteca. Su función es esencial para crear aplicaciones que consisten en múltiples archivos fuente y que hacen uso de bibliotecas externas.

4.	Los datos primarios son datos básicos que no se construyen a partir de otros tipos, representan valores simples y directos (como int, float, char…). Los datos derivados se construyen a partir de los tipos de datos primarios mediante combinaciones y modificaciones (como arrays, strucs, clases…)

5.	Declarar una variable se refiere a la acción de informar al compilador acerca de la existencia de una variable antes de que se utilice en el programa. Inicializar una variable significa asignarle un valor específico durante su declaración o en un punto posterior del programa. La inicialización es la acción de proporcionar un valor inicial a una variable para que tenga un estado conocido y definido.

6.	Es una característica que permite definir múltiples funciones con el mismo nombre en el mismo ámbito, siempre y cuando tengan firmas diferentes (diferentes tipos de parámetros o un número diferente de parámetros).

7.	Un puntero es una variable que almacena la dirección de memoria de otra variable. En otras palabras, un puntero apunta a la ubicación en memoria de otra variable. Los punteros son una característica fundamental en lenguajes como C y C++, y ofrecen un alto grado de flexibilidad y control sobre la memoria. Una analogía a un puntero sería la dirección o ubicación de un libro en una biblioteca, pues brinda información sobre el espacio físico en el que se encuentra el contenido deseado.

8.	Una variable global almacena el valor original de una operación en una función, por lo que su valor es compartido y puede ser modificado directamente por cualquier función en el programa. Las variables globales se eligen en ciertos contextos por su accesibilidad global y persistencia de valor entre funciones, pero su uso excesivo puede llevar a problemas de mantenimiento, legibilidad y concurrencia.

9.	La biblioteca string en C++ proporciona una variedad de funciones y métodos para manipular cadenas de caracteres.
a.	El método length() (o size()) devuelve el tamaño (número de caracteres) de la cadena.
b.	El método substr() devuelve una subcadena de la cadena original
c.	El método find() busca la primera aparición de una subcadena en la cadena original y devuelve la posición en la que se encuentra.

10.	En un bucle while, la condición de parada se evalúa antes de ejecutar el bloque de código del bucle. Si la condición es falsa desde el principio, el bloque de código no se ejecuta en absoluto. En un bucle do-while, el bloque de código se ejecuta al menos una vez, independientemente de si la condición es verdadera o falsa. Después de la ejecución del bloque, se evalúa la condición

11.	No se pueden almacenar funciones directamente como miembros de una estructura, pero se puede lograr una funcionalidad similar utilizando punteros a funciones o funciones miembro en una clase.

12.	Es una práctica común que sigue el modelo de separación de declaraciones e implementaciones. Esta organización tiene varios beneficios, como facilitar el mantenimiento del código, mejorar la legibilidad, permitir la reutilización de código y reducir el tiempo de compilación.
a.	.hpp: Contienen las declaraciones de las clases, estructuras, funciones y variables que se utilizarán en el programa. Incluyen prototipos de funciones, definiciones de clases, estructuras y declaraciones de variables globales.
b.	.cpp: Contienen las implementaciones de las funciones y métodos declarados en los archivos .hpp. Incluyen la lógica detallada de cómo se deben realizar las operaciones definidas en las declaraciones.
c.	Main.cpp: Contiene la función main, que es el punto de entrada del programa. Incluye las declaraciones de clases, estructuras, funciones o variables necesarias para ejecutar el programa. Sirve como el archivo fuente principal que inicia la ejecución del programa.

13.	El Type Casting (o conversión de tipos) en C++ se refiere a la capacidad de cambiar el tipo de una variable o expresión a otro tipo de dato. Permite operaciones entre tipos diferentes cuando sea necesario y facilita la asignación de valores entre diferentes tipos para cumplir con los requisitos de una expresión o función.

14.	Su uso se ha desaconsejado en la programación moderna debido a varios problemas asociados, como la dificultad para entender y mantener el código, la posibilidad de generar código no estructurado y la introducción de errores difíciles de localizar. En lugar de goto, se pueden utilizar estructuras de control de flujo como if, else, while, for, y switch para gestionar el flujo del programa de manera más estructurada.

15.	Las variables locales se almacenan en la pila con una duración vinculada al tiempo de ejecución de la función o bloque donde se declaran, mientras que las variables globales se almacenan en el segmento de datos y tienen una duración que abarca toda la ejecución del programa. Las locales tienen un ámbito limitado a la función o bloque, mientras que las globales son accesibles en todo el programa.

16.	Pasar parámetros por valor implica copiar el valor del argumento a la función, sin afectar la variable original. Al pasar parámetros por referencia, se trabaja directamente con el valor original, permitiendo modificaciones dentro de la función. Por último, al pasar parámetros por puntero, se pasa la dirección de memoria del argumento, lo que también permite modificar el valor original.

17.	El puntero inicialmente apunta a la dirección de memoria del primer elemento del arreglo. Se puede acceder a todos los datos del arreglo se realiza mediante el puntero utilizando la aritmética de punteros.

18.	Los punteros dobles en C++ son utilizados para manejar matrices bidimensionales o para trabajar con la asignación dinámica de memoria. Un puntero doble es un puntero que apunta a otra dirección de memoria que contiene otro puntero. Si se tiene una lista de nombres, por ejemplo, se tendría un puntero apuntando a dicha lista, la cual es una lista de punteros hacia las cadenas de caracteres que componen cada nombre.

19.	Break se utiliza para salir inmediatamente de un bucle, independientemente de la iteración actual, mientras que continue se utiliza para omitir el resto del código dentro del bucle para la iteración actual y pasar directamente a la siguiente iteración.

20.	Se utiliza para prevenir la inclusión redundante de un archivo de encabezado. Junto con #define y #endif, forma un mecanismo conocido como guardia de inclusión, que evita problemas de declaración duplicada al asegurarse de que un archivo de encabezado solo se incluya una vez en un programa.

21.	Es un puntero implícito que apunta al objeto actual dentro de una clase. Este puntero se utiliza para referenciar los miembros de la clase, permitiendo distinguir entre variables locales y variables de instancia

22.	Es un valor literal que representa de manera explícita un puntero nulo o vacío. Ofrece una alternativa más clara y segura a los antiguos valores 0 o NULL.

23.	Los arreglos tienen un tamaño fijo que se define en la declaración, permitiendo un acceso directo a elementos mediante índices, mientras que las listas son estructuras dinámicas que ofrecen flexibilidad en términos de crecimiento y decrecimiento durante la ejecución del programa.

24.	Un prototipo de función es una declaración anticipada que describe la firma de una función, incluyendo su nombre, tipo de retorno y parámetros, sin proporcionar el cuerpo de la función.

25.	Ocurre cuando un programa reserva dinámicamente memoria, pero no libera correctamente esa memoria cuando ya no es necesaria. Como resultado, la memoria asignada permanece ocupada incluso 
después de que el programa ha dejado de hacer uso de ella.


# Parte Automatización – Makefile 

1.	
CC: Especifica el compilador a utilizar.
CFLAGS: Contiene las opciones de compilación para el compilador.
CXXFLAGS: Similar a CFLAGS, pero específico para el compilador de C++.
LDFLAGS: Contiene las opciones para el enlazador (linker).

2.	Una regla en un Makefile consta de tres partes principales: 
El objetivo (target): Es el nombre del archivo o tarea que se desea construir.

Las dependencias (prerequisites): Son los archivos o tareas que deben estar actualizados antes de que el objetivo pueda ser construido.
Las acciones (commands): Son los comandos que se ejecutarán para construir el objetivo. Pueden incluir comandos de compilación, enlace, copia, etc.

3.	Un target representa un archivo ejecutable o cualquier otro tipo de archivo que se pretenda generar. Este target tiene prerequisitos, que son archivos o tareas necesarios antes de su construcción. La relación entre un target y sus prerequisitos se establece mediante reglas en el Makefile, donde se definen las acciones a ejecutar para construir el target en caso de que algún prerequisito esté desactualizado.

4.	Las banderas -I, -c, y -o son opciones utilizadas para personalizar el proceso de compilación:
-I (Include): Agrega un directorio al conjunto de directorios en los cuales el compilador buscará archivos de encabezado (header files).
-c (Compile): Indica al compilador que solo realice la fase de compilación y no realice la fase de enlace. Esto produce un archivo objeto (object file) sin realizar la creación del ejecutable final.
-o (Output): Especifica el nombre del archivo de salida (ejecutable o archivo objeto).

5. Las variables se definen mediante la asignación de valores con la sintaxis NOMBRE = valor, y se utilizan expandiendo su contenido con $NOMBRE. Estas variables permiten parametrizar y configurar el proceso de construcción, simplificando la gestión de opciones como configuraciones del compilador, nombres de archivos o rutas de directorios.

6. El símbolo @ se emplea para suprimir la impresión en la salida estándar de la línea de comando que le precede. Al añadir @ a un comando en una regla de construcción, se logra que la ejecución del comando sea silenciosa, lo que mejora la claridad de la salida al evitar la visualización de cada comando individual.

7. La directiva .PHONY se utiliza para declarar que un target no representa un archivo físico, sino una tarea o acción. Al marcar un target como .PHONY, se garantiza que la acción asociada se ejecutará siempre, independientemente de la existencia de archivos con el mismo nombre.

