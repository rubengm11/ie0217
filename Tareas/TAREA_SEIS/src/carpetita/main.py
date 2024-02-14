import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from regresion import regresion_lineal_precios, regresion_lineal_kilometros, regresion_no_lineal_precios, regresion_no_lineal_kilometros

def cargar_datos(ruta_archivo):
    try:
        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv(ruta_archivo)

        # Limpieza de datos de forma iterativa, utilizando la columna DEST_CITY_NAME
        for indice, fila in df.iterrows():
            df.at[indice, 'name'] = transformacion_personalizada(fila['name'])
        
        return df

    # Posibles excepciones
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo en la ruta {ruta_archivo}")
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV esta vacio o no contiene datos.")
    except pd.errors.ParserError:
        print("Error: Problema al parsear el archivo CSV. Verificar el formato.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

def transformacion_personalizada(valor):
    # Se utiliza esta funcion para convertir los elementos de una columna en mayusculas.
    return valor.upper()  



# Llamada a la función para cargar datos
datos = cargar_datos("./src/carpetita/datos.csv")

# Verificar que los datos se hayan cargado bien
if datos is not None:
    # Se imprimen los primerios 15 datos antes de la limpieza
    print("Datos cargados exitosamente:")
    print(datos.head(15))

    # Convirtiendo la columna de cantidad de pasajeros a int
    #datos['PASSENGERS'] = datos['PASSENGERS'].astype(int)

    # Se imprimen los primerios 15 datos despues de la limpieza
    #print(datos.head(15))

    #print("Info del dataframe\n")

    # Proporciona estadísticas descriptivas del DataFrame
    print(datos.describe())

    # Cálculo del promedio de la columna 'PASSENGERS'
    #promedio_pasajeros = datos['PASSENGERS'].mean()
    #print("\nPromedio de pasajeros:", promedio_pasajeros, "\n")

    # Cálculo de la moda de la columna 'DEST_CITY_NAME'
    #moda_ciudad_destino = datos['DEST_CITY_NAME'].mode()
    #print("\nCiudad destino mas frecuentada (moda)\n", moda_ciudad_destino, "\n")

    # Maxima distancia de vuelo
    #distancia_maxima = datos['DISTANCE'].max()
    #print("\nDistancia maxima de vuelo:", distancia_maxima, "\n")

    # Aerolinea mas usada
    #moda_aerolinea = datos['CARRIER_NAME'].mode()
    #print("\nAerolinea mas utilizada (moda)\n", moda_aerolinea, "\n")

    # De forma iterativa se crea el informe de aerolineas
    #for informe in generar_informe_detallado(datos):
     #   print(informe, "\n")
    
    # Identificar Datos Faltantes
    print("\nDatos Faltantes por Columna:")
    print(datos.isnull().sum())

    # Eliminar Datos Duplicados
    print("\nEliminando datos duplicados")
    datos.drop_duplicates(inplace=True)

    print("\nDataFrame Resultante:")
    print(datos)

    print("\nModelos de regresion lineal:")
    print("\n")
    regresion_lineal_precios(datos)
    print("\n")
    regresion_lineal_kilometros(datos)

    print("\nModelos de regresion no lineal:")
    print("\n")
    regresion_no_lineal_precios(datos)
    print("\n")
    regresion_no_lineal_kilometros(datos)