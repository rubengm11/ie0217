Este es el archivo README.md de la tarea 3.

# Instrucciones de utilizacion del programa:

## El archivo Makefile contiene los siguientes targets:

### Para el programa matriz

- Es importante destacar que no me fue posible separar los archivos de la parte practica 1. Por lo que el makefile ejecuta el archivo funcional, de igual forma se adjuntan los tres archivos.

1. clean_matriz: Limpia el directorio matriz de archivos compilados y deja unicamente el codigo fuente.
2. build_matriz: compila el codigo fuente y genera un ejecutable llamado matriz.
3. run_matriz: Ejecuta el programa matriz
4. matriz: compila y corre el programa.

### Para el programa correo

1. clean_correo: Limpia el directorio correo de archivos compilados y deja unicamente el codigo fuente.
2. build_correo: compila el codigo fuente y genera un ejecutable llamado correo.
3. run_correo: Ejecuta el programa correo
4. correo: compila y corre el juego.

# Respuestas a la parte teorica

## Templates

1.  Definicion de Templates: Explique el concepto de templates en C++ y
proporcione un ejemplo simple.
Los templates son una característica que permite escribir código genérico, es decir, código que puede trabajar con diferentes tipos de datos sin tener que repetir el código para cada tipo específico. La principal ventaja de los templates es que proporcionan flexibilidad y reutilización del código, por lo que es posible escribir algoritmos y estructuras de datos que funcionan con cualquier tipo de datos compatible.

2. Sobrecarga de Plantillas: ¿Como se realiza la sobrecarga de funciones con
plantillas en C++?
La sobrecarga de funciones con plantillas permite ingresar varias versiones de una plantilla de función, cada una aceptando diferentes tipos de parámetros. El compilador se encarga de seleccionar la versión adecuada en función de los argumentos proporcionados durante la llamada a la función.

3. Plantillas de Clases: Explique como se pueden utilizar plantillas en la definicion de clases en C++.
Se pueden utilizar en la definición de clases para crear clases que operen con tipos de datos genéricos. Esto permite escribir código que es independiente del tipo de datos que se utilizará.

## Excepciones

4. Manejo de Excepciones: Describa los bloques try, catch y throw y como
se utilizan para el manejo de excepciones en C++.
Un bloque try define un área del código donde se puede producir una excepción. Cada bloque catch especifica el tipo de excepción que puede manejar y el código que se ejecutará si se lanza esa excepción. La instrucción throw se utiliza para lanzar una excepción desde un bloque try. Puede lanzar cualquier tipo de dato.

5.  Excepciones Estandar: Nombre al menos tres excepciones estandar proporcionadas por C++ y proporciona ejemplos de situaciones en las que podrian ser
utiles.

- std::invalid_argument: Esta excepción se utiliza cuando se proporciona un argumento que no es válido para una función. Ejemplo: En una función que espera un número positivo, se lanzaria std::invalid_argument si se recibe un número negativo.

- std::out_of_range: Se utiliza cuando se produce un intento de acceder a un elemento fuera del rango válido en una estructura de datos, como un contenedor (std::vector, std::array, etc.).

- std::runtime_error: Esta excepción general se utiliza para situaciones inesperadas durante la ejecución del programa que no pueden clasificarse con otras excepciones más específicas.

6.  Politica de Manejo de Excepciones: ¿Que es una politica de manejo de
excepciones y por que es importante considerarla al disenar software?

Se refiere a las decisiones y estrategias que un desarrollador o un equipo de desarrollo elige para manejar errores dentro de un programa utilizando el mecanismo de excepciones proporcionado por el lenguaje de programación. Estas políticas pueden incluir cómo se lanzan, propagan, capturan y manejan las excepciones en un sistema. Claridad en el Código, Robustez del Programa, Seguridad.

7. Noexcept: Explica el proposito de la palabra clave noexcept y como se utiliza en C++.

Se utiliza para especificar que una función no lanza excepciones durante su ejecución. Se puede aplicar noexcept tanto a funciones como a operadores, indicando que no generan excepciones. Se coloca después de la lista de parámetros y antes del cuerpo de la función. También se puede utilizar para especificar que una función podría lanzar excepciones pero no especifica cuáles. 

## STL

8. Contenedores STL: Nombre cinco contenedores diferentes de la STL y explique brevemente en que situaciones seria apropiado usar cada uno.

- std::vector:
Descripción: Almacena elementos de manera dinámica en un arreglo contiguo.
Uso Apropiado: Útil cuando se necesita acceder rápido a los elementos y cuando el tamaño del contenedor puede cambiar dinámicamente.

- std::list:
Descripción: Implementa una lista doblemente enlazada.
Uso Apropiado: Sirve para inserciones y eliminaciones eficientes en cualquier posición de la lista. 

- std::map / std::unordered_map:
Descripción: es un contenedor asociativo ordenado (basado en árbol).
Uso Apropiado: std::map es apropiado cuando se necesita mantener los elementos ordenados según una clave. 

- std::queue:
Descripción: Implementa una cola FIFO.
Uso Apropiado: Útil cuando se necesita mantener un orden específico para procesar elementos en el mismo orden en que se insertaron.

- std::set / std::unordered_set:
Descripción: std::set es un contenedor asociativo ordenado que almacena elementos únicos y std::unordered_set es un contenedor asociativo no ordenado que almacena elementos únicos.
Uso Apropiado: std::set es adecuado cuando se necesita mantener elementos únicos y en orden. std::unordered_set es más eficiente para búsquedas, inserciones y eliminaciones, pero no garantiza un orden específico.

9. Iteradores en STL: Explique el concepto de iteradores en la STL y como se utilizan para acceder a elementos en contenedores.
Los iteradores son objetos que se utilizan para acceder y manipular elementos en contenedores, proporcionando una interfaz uniforme para el acceso secuencial a los elementos almacenados en una estructura de datos. Los iteradores actúan como punteros, permitiendo a los programadores recorrer y acceder a los elementos de los contenedores sin necesidad de conocer los detalles internos de la implementación del contenedor.

10. Algoritmos STL: Proporcione ejemplos de al menos tres algoritmos de la STL y describa sus funciones basicas.
- std::sort se utiliza para ordenar elementos en un rango especificado. Puede ordenar en orden ascendente (predeterminado) o en orden descendente si se proporciona un comparador personalizado.
Ejemplo: Ordenar una lista de nombres alfabeticamente

- std::find: se utiliza para buscar la primera aparición de un valor específico en un rango. Es útil para verificar la presencia de un elemento en una colección.
Ejemplo: Encontrar el primer numero primo de una lista.

- std::for_each: aplica una función a cada elemento en un rango. Es útil para realizar operaciones en cada elemento sin necesidad de bucles explícitos.
Ejemplo: Imprimir el cuadrado de cada elemento de una lista.

11. Algoritmos Personalizados: ¿Como podria utilizar un algoritmo personalizado con la STL?
Si tuviese una lista y quiero realizar una operación personalizada en cada elemento de ese conjunto, pero las funciones estándar de la STL no cubren exactamente la operacion deseada.
Por ejemplo, tener un vector de números e imprimir el cuadrado de cada número.
Es posible crear una función que implemente la lógica deseada. Luego, se utiliza esta función personalizada con un algoritmo de la STL, como std::for_each, para aplicar la operación a cada elemento del contenedor.

## Expresiones regulares

12. Definicion de Expresiones Regulares: Defina que son las expresiones
regulares y proporcione un ejemplo simple.
Son patrones de búsqueda y manipulación de cadenas de texto. Estos patrones son utilizados para realizar búsquedas, comparaciones, validaciones y manipulaciones de texto de manera eficiente. Expresión Regular: ^[a-zA-Z]+$
- ^: Indica que la coincidencia debe comenzar desde el inicio de la cadena.
- [a-zA-Z]: Representa un conjunto de caracteres que incluye todas las letras minúsculas y mayúsculas del alfabeto inglés.
- +: Indica que debe haber al menos un carácter del conjunto mencionado antes (letras minúsculas o mayúsculas).
- $: Indica que la coincidencia debe llegar hasta el final de la cadena.

13. Caracteres Especiales: Enumere al menos tres caracteres especiales comunmente utilizados en expresiones regulares y describa sus funciones
- ^ : Ancla de inicio: 
Función: Indica que la coincidencia debe comenzar desde el inicio de la cadena. Si se coloca al principio de una expresión regular, asegura que el patrón buscado esté presente desde el principio de la cadena.
- $ : Ancla de final:
Función: Indica que la coincidencia debe llegar hasta el final de la cadena. Si se coloca al final de una expresión regular, asegura que el patrón buscado esté presente hasta el final de la cadena.
- . : Comodín (punto):
Función: Coincide con cualquier carácter, excepto el salto de línea (\n). Es útil para representar cualquier carácter en un lugar específico de la cadena.

14. Uso de Expresiones Regulares en C++: ¿Como se utilizan las expresiones regulares en C++? Proporciona un ejemplo.
Por ejemplo, si quiero identificar todas las líneas que contienen direcciones IP válidas en formato IPv4.
Por lo que decido utilizar expresiones regulares para buscar y extraer direcciones IP en el formato adecuado. La expresión regular que adecuada podria ser algo como \\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b.

- \\b: Ancla de límite de palabra para asegurar que coincida con la dirección IP completa y no con parte de otra cadena.
- (?:\\d{1,3}\\.){3}: Un grupo no capturador que busca tres bloques de uno a tres dígitos seguidos por un punto.
- \\d{1,3}: Busca el último bloque de uno a tres dígitos.
- \\b: Ancla de límite de palabra al final.
Entonces, en el programa, podria leer cada línea del archivo de registro y aplicar la expresión regular para identificar y extraer las direcciones IP válidas. 


15. Validacion de Patrones: ¿Por que las expresiones regulares son utiles para la validacion de patrones en cadenas de texto?

- Flexibilidad en la Descripción de Patrones
Las expresiones regulares proporcionan una forma concisa y potente de describir patrones complejos en cadenas de texto. Es posible especificar reglas detalladas y condiciones para la búsqueda de patrones, como la longitud, el tipo de caracteres, y la secuencia específica de caracteres.

- Búsqueda Eficiente
Las expresiones regulares permiten buscar patrones de manera eficiente en grandes cantidades de texto. Utilizan algoritmos optimizados para realizar búsquedas y comparaciones de patrones, lo que mejora el rendimiento en comparación con implementaciones manuales.

- Validación de Formatos Específicos
Son especialmente útiles para validar cadenas de texto que deben cumplir con un formato específico, como direcciones de correo electrónico, números de teléfono, fechas, direcciones IP, entre otros. Las expresiones regulares permiten definir y verificar estos formatos de manera fácil y precisa.

- Automatización de Tareas de Procesamiento de Texto
Facilitan la automatización de tareas relacionadas con el procesamiento de texto, como la extracción de información específica, la corrección de formato, la validación de datos, entre otros. Esto es crucial en situaciones donde se manejan grandes volúmenes de datos.

- Mejora de la Legibilidad del Código
El uso de expresiones regulares puede mejorar la legibilidad del código al proporcionar una representación clara y concisa de los patrones que se estan buscando. Esto facilita la comprensión del código, especialmente cuando se trata de operaciones complejas de manipulación de cadenas.

- Adaptabilidad y Portabilidad
Las expresiones regulares son independientes del lenguaje de programación, lo que significa que se pueden utilizar en diferentes entornos y plataformas sin tener que reescribir la lógica de búsqueda. Esto facilita la portabilidad del código entre proyectos y aplicaciones.

- Manejo de Casos Específicos:
Permiten manejar casos específicos, como la búsqueda de palabras clave, la validación de patrones en campos de formularios, la filtración de información específica, entre otros.










