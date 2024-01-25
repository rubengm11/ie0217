Instrucciones de utilizacion


# Respuestas a la parte teorica

1. Explique la diferencia entre una lista y una tupla en Python.

- La diferencia principal entre una lista y una tupla radica en la mutabilidad. Las listas son mutables, lo que significa que se pueden modificar, agregar o eliminar elementos después de la creación, las tuplas son inmutables, pero presentan un mejor rendimiento al compilar el codigo.

2. ¿Que es la sobrecarga de operadores en Python y como se implementa?

- Se refiere a la capacidad de definir o personalizar el comportamiento de los operadores para objetos de clases definidas por el usuario. Esto permite que los objetos de esas clases respondan a operadores como +, -, *, ==, entre otros, de una manera específica.

3. Explique el concepto de alcanzabilidad (scope) de una variable en Python.

- Se refiere a la región del código en la que una variable es accesible y puede ser utilizada. Python tiene reglas claras sobre cómo se determina el alcance de una variable, los niveles de alcance son local, encerrado, global e incorporado (Built-in Scope).

4. ¿Que es un decorador en Python y cual es su funcion principal?

- Un decorador es una función especial que se utiliza para modificar o extender el comportamiento de otra función. Los decoradores proporcionan una forma compacta y elegante de aplicar funciones adicionales a otras funciones sin tener que modificar su código interno. La función decoradora toma como argumento la función que se va a decorar y devuelve una nueva función (o modifica la función existente) que generalmente agrega funcionalidad adicional. Los decoradores son comúnmente utilizados para tareas como el registro de funciones, el manejo de excepciones, la medición del tiempo de ejecución, la autenticación, entre otros.

5. ¿Cómo se gestionan las excepciones en Python? Proporcione ejemplos de uso de bloques try, except y finally.

- La gestión de excepciones se realiza mediante los bloques try, except, y opcionalmente finally. Este mecanismo permite manejar situaciones excepcionales de manera controlada, evitando que los errores detengan la ejecución del programa. 

    - Ejemplo:

    - try:
            # Código que podría generar una excepción
    - except ZeroDivisionError:
            # Manejo del error, en este caso division entre 0, por ejemplo.
            print("¡Error! División entre cero.")
    - else:
            # Se ejecuta si no se generó ninguna excepción en el bloque try
    - finally:
            # Se ejecuta siempre, independientemente de si se generó una excepción o no

6. ¿Qué son los generadores en Python y para qué se utilizan?

- Los generadores son una forma eficiente de crear iteradores. Proporcionan una manera de generar secuencias de valores uno a la vez, en lugar de generar todos los valores de antemano y almacenarlos en la memoria.

7. Explique la diferencia entre \_\_init\_\_ y \_\_call\_\_ en clases de Python.

- \_\_init\_\_ es un método especial utilizado para inicializar instancias de una clase. Es llamado automáticamente cuando se crea un nuevo objeto de esa clase.
- \_\_call\_\_ es otro método especial que permite que una instancia de la clase sea llamada como si fuera una función.

8. ¿Cómo se organizan los módulos y paquetes en Python? ¿Qué es \_\_init\_\_ .py?

- Un módulo es un archivo de Python que contiene definiciones y declaraciones de código, mientras que un paquete es una colección de módulos organizados en un directorio. El archivo \_\_init\_\_.py en un paquete sirve para indicar que el directorio debe ser considerado como un paquete de Python. Puede estar vacío o contener código de inicialización para el paquete. Si está vacío, simplemente se usa para señalar que el directorio debe ser tratado como un paquete.

9. Explique la diferencia entre métodos append() e extend() en listas de Python.

- El método append() se utiliza para agregar un solo elemento al final de la lista. Toma un único argumento, que es el elemento que se desea agregar. Modifica la lista original y agrega el elemento al final de la misma.
- El método extend() se utiliza para agregar múltiples elementos a una lista, ya sea otra lista o cualquier iterable. Toma un iterable como argumento y agrega cada elemento individual al final de la lista original. Modifica la lista original y extiende su longitud con los elementos del iterable.

10. ¿Cuál es la diferencia entre un método de clase y un método estático en Python?

- La diferencia clave entre un método de clase y un método estático radica en los argumentos que reciben. Un método de clase recibe la clase como primer argumento (cls) y puede acceder y modificar atributos de clase, mientras que un método estático no recibe la clase ni la instancia, siendo independiente de ellas. 

11. Hable sobre las diferencias entre herencia simple y herencia méltiple en Python.

- La herencia simple implica que una clase puede heredar de una única clase padre, estableciendo una relación lineal entre ellas. La herencia múltiple permite que una clase herede de varias clases padres, ofreciendo flexibilidad al combinar funcionalidades de diferentes fuentes.

12. ¿Cómo se manejan los errores de importación de módulos en Python?

- Se pueden utilizar modulos try y except, por ejemplo:

    - try:
        import modulo_inexistente
    - except ImportError:
        print("El módulo no pudo ser importado.")

13. ¿Cuál es la diferencia entre una clase y un objeto en Python?

- Una clase es una plantilla que define la estructura y el comportamiento de objetos, proporcionando atributos y métodos. Un objeto es una instancia específica de esa clase, con valores particulares para sus atributos. Las clases sirven como moldes para crear objetos.

14. Hable sobre la diferencia entre una clase abstracta y una interfaz en Python.

-  L diferencia entre una clase abstracta y una interfaz se encuentra principalmente en la terminología y la implementación. Una clase abstracta utiliza el módulo abc para definir métodos abstractos, que deben ser implementados por las clases hijas. Para el caso de la interfaz, esta se puede lograr mediante clases abstractas que contienen métodos abstractos que actúan como reglas contractuales para las clases que las implementan. 

15. Explique el concepto de sobreescritura de métodos en Python y cómo se realiza.

- se refiere a la capacidad de una clase hija para proporcionar una implementación diferente para un método que ya está definido en su clase padre. Cuando una clase hija redefine un método que ya está presente en la clase padre. La sobreescritura de métodos se realiza al definir el mismo método en la clase hija, utilizando el mismo nombre y parámetros que en la clase padre. La clase hija proporciona una nueva implementación para ese método, y cuando se llama en una instancia de la clase hija, se ejecuta la versión del método de la clase hija en lugar de la de la clase padre.