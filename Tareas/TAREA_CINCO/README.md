# README de la tarea 5



# Respuestas a la parte teorica

## Iteradores

1. ¿Qué es un iterador en Python y cuál es su propósito?

- Es un objeto que permite ser iterado en un bucle, como un bucle for. Su propósito principal es proporcionar un mecanismo uniforme para recorrer secuencias de datos.

2. Explique la diferencia entre un iterable y un iterador.

- Un iterable es un objeto que puede ser iterado, mientras que un iterador es el objeto que realiza la iteración y mantiene el estado de la misma. Un iterable proporciona un iterador a través de su método \_\_iter\_\_, y el iterador proporciona los elementos sucesivos a través de su método \_\_next\_\_.

## Excepciones

1. Defina qué es una excepción en Python.

- Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal de ejecución, son utilizadas para manejar errores y situaciones excepcionales de manera controlada.

2. ¿Cuál es el propósito de la cláusula try... except en el manejo de excepciones?

- Su propósito principal es crear un mecanismo para manejar errores de manera controlada durante la ejecución del programa. Su función es permitir que el programa continúe ejecutándose incluso cuando ocurren errores.

3. Explica la diferencia entre las cláusulas except y finally en el manejo de excepciones.

- except se utiliza para manejar excepciones específicas que pueden ocurrir en un bloque try, finally se utiliza para especificar bloques de código que siempre se ejecutarán, ya sea que se produzca una excepción o no.

## Generadores

1. ¿Qué es un generador en Python y cuál es su ventaja sobre las listas tradicionales?

- Es una función que utiliza la palabra clave yield para producir una secuencia de valores en lugar de retornar una lista completa como lo haría una función que utiliza return. La principal ventaja de los generadores sobre las listas tradicionales radica en su eficiencia en términos de uso de memoria.

2. Explica cómo se puede crear un generador usando la función yield.

- Se utiliza la palabra clave yield en lugar de return en una función. Cuando la función con yield es llamada, no se ejecuta completamente en ese momento, sino que devuelve un objeto generador. Cuando se itera sobre este generador, la ejecución de la función se reanuda desde el punto donde se dejó, manteniendo su estado interno.

3. ¿Cuándo es más apropiado usar generadores en lugar de listas?

- Es más apropiado usar generadores en lugar de listas cuando se trabaja con conjuntos de datos grandes o cuando la generación de elementos es costosa en términos de memoria. Los generadores permiten la generación perezosa, lo que significa que los elementos se generan uno a la vez, según sea necesario, en lugar de crear una lista completa en la memoria. 

## Pandas

1.  ¿Cuál es la diferencia entre una Serie y un DataFrame en Pandas?

- una Serie es una estructura de datos unidimensional que puede almacenar datos de cualquier tipo. Cada elemento de la Serie tiene una etiqueta, llamada índice. Un DataFrame es una estructura bidimensional que puede almacenar datos de manera tabular. Se puede considerar como una hoja de cálculo o una tabla de base de datos, donde cada columna es una Serie y comparten el mismo índice.

2. Explique cómo manejar valores nulos o faltantes en un DataFrame.

- Se pueden utilizar métodos como isnull(), notnull(), dropna() y fillna(). Estos métodos permiten identificar, eliminar, o llenar los valores nulos en un DataFrame. isnull() y notnull() son útiles para verificar la presencia de valores nulos, mientras que dropna() elimina filas o columnas con valores nulos. fillna() permite rellenar valores nulos con un valor específico o mediante métodos de interpolación

3. ¿Cuál es la diferencia entre loc y iloc en Pandas?

- La diferencia entre loc e iloc radica en cómo especifican las ubicaciones de las filas y columnas. loc se utiliza con etiquetas, siendo inclusivo respecto a los límites, mientras que iloc se utiliza con índices enteros y es exclusivo respecto a los límites. 