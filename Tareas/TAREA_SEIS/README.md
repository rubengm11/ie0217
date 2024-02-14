# Instrucciones de uso
- Para la ejecucion del programa utilice el comando make run desde el directorio donde se encuentra el Makefile, si tiene algun problema ejecutando el comando debido al compilador utilizado, tenga en cuenta que lo unico que se debe ejecutar es el archivo main.py cuyo path es ./src/carpetita/main.py

- Es importante mencionar que debe tener el archivo kaggle.json en su carpeta .kaggle para realizar la autenticacion, si no es asi, de igual forma se adjunta el archivo .csv en el directorio. Puede verificar que la descarga funciona eliminando dicho archivo y descargandolo de nuevo.

- Al iniciar el programa, se desplegara en consola un breve analisis del dataframe y comandos relacionados a la limpieza de datos. 

- La primera ventana muestra un analisis de regresion lineal del precio de venta en funcion del modelo (año), tambien se imprimen en consola los resultados de la evaluacion de rendimiento para cada caso.

- La segunda ventana que se abre muestra un analisis de regresion lineal del precio de venta en funcion del kilometraje del auto.

- Las siguientes dos ventanas comparan las mismas columnas pero utilizando un analisis de regresion no lineal, con un polinomio de grado 2.

- Luego se utiliza el metodo del codo y de Silhouette para determinar el numero optimo de cluster, donde se decide utilizar 3, debido a los resultados de ambas graficas, principalmente a la grafica del metodo de Silhouette, pues el punto mas alto es 3.

- Finalmente se utiliza 3 como el numero de clusters y se hace una visualizacion de clusters con PCA.

# Analisis de resultados

- Para la primera regresion lineal (Precio de venta en funcion del año), se observa una leve diferencia en los datos, pues hay puntos que se elevan muy por encima de la recta de regresion lineal, por lo que talvez el comportamiento de esta grafica pueda ser cuadratico o inclusive exponencial, lo cual tiene sentido, entre mas nuevo un auto, su precio tiende a ser muy elevado.

- Para la segunda regresion lineal (Precio de venta en funcion del kilometraje), se observa nuevamente ciertos puntos que se alejan de la recta, es logico pensar que entre mayor kilometraje tenga un automovil, su precio de venta tiende a ser menor.

- En la regresiones no lineales sucede algo similar, no se obtiene un comportamiento tan acertado, talvez podria implementarse un polinomio de grado mayor para analizar su comportamiento.

- Para determinar el numero optimo de clusters se utilizaron dos metodos, de los cuales se concluyo que el numero optimo es 3, pues en el metodo del codo se busca el punto en el cual la curva se dobla o forma un codo (cercano a 3, como se puede observar), en el metodo de Silhouette se busca el número de clusters que maximiza el valor medio del coeficiente de Silhouette sobre todos los puntos.


# Respuestas a las preguntas de teoria

## Regresion 

1. ¿Que es la regresion lineal y como se diferencia de la regresion no lineal?

- La regresión lineal asume que la relación entre variables es lineal, la regresión no lineal permite relaciones más complejas mediante funciones no lineales como polinomios, exponenciales o logarítmicas.

2. ¿Que son los coeficientes de regresion y que informacion proporcionan sobre la relacion
entre las variables?

- Son los parámetros que definen la relación entre las variables en un modelo de regresión. En una regresión lineal, estos coeficientes representan la pendiente y la intercepción de la línea de regresión. 

3. ¿Que es el error cuadratico medio (MSE) y como se utiliza para evaluar la precision
de un modelo de regresion?

- Es una métrica utilizada para evaluar la precisión de un modelo de regresión. Se calcula como la media de los cuadrados de las diferencias entre las predicciones del modelo y los valores reales. Cuanto menor sea el MSE, mejor será el rendimiento del modelo

4. ¿Cual es la diferencia entre regresion simple y regresion multiple y cuando se utiliza
cada una?

- La diferencia principal radica en el número de variables predictoras involucradas en el modelo. En la regresión simple, hay una sola variable predictora, mientras que en la regresión múltiple, hay dos o más variables predictoras.

## Clusterig 

1. ¿Que es el clustering y cual es su objetivo principal en el analisis de datos?

- Es una técnica de aprendizaje no supervisado que tiene como objetivo principal dividir un conjunto de datos en grupos homogéneos, donde los elementos dentro de un mismo grupo son más similares entre sí que con aquellos en otros grupos. La idea es descubrir patrones o estructuras subyacentes en los datos sin conocer de antemano las categorías a las que pertenecen.

2. Describa brevemente los algoritmos K-Means y DBSCAN y como funcionan.

- K-Means es un algoritmo de clustering que divide un conjunto de datos en k clusters. Comienza seleccionando k centroides de forma aleatoria, asigna cada punto al cluster cuyo centroide está más cercano y luego recalcula los centroides basándose en la media de los puntos asignados a cada cluster. 

- DBSCAN es un algoritmo de clustering basado en densidad. Se centra en la densidad de los puntos en lugar de la distancia. Funciona identificando regiones densas del espacio de datos, agrupando puntos que están cerca unos de otros y asignando puntos a categorías como núcleos, bordes o ruido. 

3. ¿Que es la inercia en el contexto del clustering y como se utiliza para evaluar la calidad
de un agrupamiento?

- La inercia en el contexto del clustering es una medida que evalúa cómo están distribuidos los puntos dentro de cada cluster. La inercia se utiliza para evaluar la calidad de un agrupamiento en el método del codo (elbow method). Este método consiste en ejecutar el algoritmo de K-Means para diferentes valores de k (número de clusters) y graficar la inercia en función de k.

4. ¿Que son los centroides y como se utilizan en el algoritmo K-Means?

- Son puntos representativos que se utilizan en el algoritmo K-Means para definir la posición central de cada cluster. En el contexto de K-Means, el centroide de un cluster es el promedio de las posiciones de todos los puntos dentro de ese cluster. 

5. Escriba la diferencia entre datos estructurados y no estructurados para analisis de datos.

- Los datos estructurados están organizados de manera específica, generalmente en tablas con filas y columnas, donde cada columna representa un atributo y cada fila una entrada. 

- Los datos no estructurasdos carecen de una estructura predefinida y organizada. Pueden ser de diversos formatos, como texto libre, imágenes, videos o archivos de audio. Los datos no estructurados requieren técnicas más avanzadas de procesamiento y análisis, como procesamiento de lenguaje natural (NLP) para texto o aprendizaje profundo para imágenes. 

## Paquetes en Python __init__.py

1. ¿Que es un paquete en Python y como se diferencia de un modulo?

- Un paquete es una colección de módulos organizados en un directorio. Un paquete incluye un archivo especial llamado \_\_init\_\_.py en su directorio para indicar que es un paquete y puede contener subdirectorios y más módulos.

- Un módulo es un archivo que contiene definiciones y declaraciones de Python. Puede contener funciones, variables y clases, y se utiliza para organizar el código de manera más modular y reutilizable

2. ¿Cual es la funcion del archivo \_\_init\_\_.py dentro de un paquete de Python?

- Su funcion es indicar que el directorio que lo contiene debe ser tratado como un paquete, permitiendo la importación de módulos desde ese directorio. Además, puede contener código de inicialización que se ejecuta durante la importación del paquete, facilitando configuraciones específicas.

3. ¿Como se importa un modulo o funcion desde un paquete en Python?

- Se utiliza la linea from nombre_del_paquete import nombre_del_modulo

4. ¿Que es la variable \_\_all\_\_ en el archivo \_\_init\_\_.py y cual es su proposito?

- Se utiliza para especificar qué nombres de módulos o funciones se importarán cuando se utiliza la sintaxis from paquete import ...

5.  ¿Cual es la ventaja de organizar el codigo en paquetes y modulos en Python?

- Organizar el codigo en paquetes y modulos brinda una estructura ordenada y modular, facilitando la reutilización, mantenimiento y comprensión del código.