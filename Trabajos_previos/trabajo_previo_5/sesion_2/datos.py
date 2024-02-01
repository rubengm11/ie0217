import pandas as pd

# Leer el archivo CSV en un DataFrame llamado 'datos'
datos = pd.read_csv("datos.csv")

# Mostrar las primeras 2 filas del DataFrame
datos.head(2)

# Mostrar los tipos de datos de cada columna en el DataFrame
datos.dtypes

# Mostrar todo el DataFrame
print(datos)

# Mostrar información detallada sobre el DataFrame
datos.info()

# Seleccionar las columnas 'edad' y 'altura' y mostrar las primeras filas
edad_altura = datos[['edad', 'altura']]
edad_altura.head()

# Mostrar el tipo de datos de la selección de columnas
type(datos[["edad", "altura"]])

# Filtrar el DataFrame para obtener solo las filas donde la edad es mayor a 18
adultos = datos[datos["edad"] > 18]
adultos.head()

# Mostrar la forma (número de filas y columnas) del DataFrame de adultos
adultos.shape

# Seleccionar los nombres de las personas mayores de 18 años
nombres_de_adultos = datos.loc[datos["edad"] > 18, "nombre"]

# Calcular la edad promedio en el DataFrame
datos["edad"].mean()

# Calcular la mediana de las columnas 'edad' y 'peso'
datos[["edad", "peso"]].median()

# Mostrar estadísticas descriptivas para las columnas 'edad' y 'peso'
datos[["edad", "peso"]].describe()

# Calcular varias estadísticas para las columnas 'edad' y 'peso' usando agg()
datos.agg(
    {
        "edad": ["min", "max", "median", "skew"],
        "peso": ["min", "max", "median", "mean"]
    }
)