# Instrucciones de uso
- Para la ejecucion del programa utilice el comando make run desde el directorio donde se encuentra el Makefile, si tiene algun problema ejecutando el comando debido al compilador utilizado, tenga en cuenta que lo unico que se debe ejecutar es el archivo main.py cuyo path es ./src/carpetita/main.py

- Es importante mencionar que debe tener el archivo kaggle.json en su carpeta .kaggle para realizar la autenticacion, si no es asi, de igual forma se adjunta el archivo .csv en el directorio. Puede verificar que la descarga funciona eliminando dicho archivo y descargandolo de nuevo.

- Al iniciar el programa, se desplegara en consola un breve analisis del dataframe y comandos relacionados a la limpieza de datos. 

- La primera ventana muestra un analisis de regresion lineal del precio de venta en funcion del modelo (año), tambien se imprimen en consola los resultados de la evaluacion de rendimiento para cada caso.

- La segunda ventana que se abre muestra un analisis de regresion lineal del precio de venta en funcion del kilometraje del auto.

- Las siguientes dos ventanas comparan las mismas columnas pero utilizando un analisis de regresion no lineal, con un polinomio de grado 2.

- Luego se utiliza el metodo del codo y de silhouette para determinar el numero optimo de cluster, donde se decide utilizar 3, debido a los resultados de ambas graficas, principalmente a la grafica del metodo de silhouette, pues el punto mas alto es 3.

- Finalmente se utiliza 3 como el numero de clusters y se hace una visualizacion de clusters con PCA.

# Analisis de resultados

- 


# Respuestas a las preguntas de teoria

## Regresion 

1. ¿Que es la regresion lineal y como se diferencia de la regresion no lineal?

2. ¿Que son los coeficientes de regresion y que informacion proporcionan sobre la relacion
entre las variables?

3. ¿Que es el error cuadratico medio (MSE) y como se utiliza para evaluar la precision
de un modelo de regresion?

4. ¿Cual es la diferencia entre regresion simple y regresion multiple y cuando se utiliza
cada una?

## Clusterig 

1. ¿Que es el clustering y cual es su objetivo principal en el analisis de datos?

2. Describa brevemente los algoritmos K-Means y DBSCAN y como funcionan.

3. ¿Que es la inercia en el contexto del clustering y como se utiliza para evaluar la calidad
de un agrupamiento?

4. ¿Que son los centroides y como se utilizan en el algoritmo K-Means?

5. Escriba la diferencia entre datos estructurados y no estructurados para analisi de datos.

## Paquetes en Python __init__.py

1. ¿Que es un paquete en Python y como se diferencia de un modulo?

2. ¿Cual es la funcion del archivo \_\_init\_\_.py dentro de un paquete de Python?

3. ¿Como se importa un modulo o funcion desde un paquete en Python?

4. ¿Que es la variable \_\_all\_\_ en el archivo \_\_init\_\_.py y cual es su proposito?

5.  ¿Cual es la ventaja de organizar el codigo en paquetes y modulos en Python?