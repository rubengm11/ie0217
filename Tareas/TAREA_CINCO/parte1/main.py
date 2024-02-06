import pandas as pd

def cargar_datos(ruta_archivo):
    try:
        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv(ruta_archivo)

        # Realizar operaciones de limpieza y preparacion de datos
        for indice, fila in df.iterrows():
            df.at[indice, 'nombre'] = transformacion_personalizada(fila['nombre'])

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
    # Aqui va la logica de preparacion de datos
    return valor.upper()  


# Llamada a la función para cargar datos
datos = cargar_datos("archivo.csv")

# Verificar que los datos se hayan cargado bien
if datos is not None:
    print("Datos cargados exitosamente:")
    print(datos.head())