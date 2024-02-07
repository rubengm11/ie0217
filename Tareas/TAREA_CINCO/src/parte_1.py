import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(ruta_archivo):
    try:
        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv(ruta_archivo)

        # Limpieza de datos de forma iterativa, utilizando la columna DEST_CITY_NAME
        for indice, fila in df.iterrows():
            df.at[indice, 'DEST_CITY_NAME'] = transformacion_personalizada(fila['DEST_CITY_NAME'])
        
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

def generar_informe_detallado(datos):
    # Se agrupa usando la columna 'CARRIER_NAME'
    grupos = datos.groupby('CARRIER_NAME')

    for nombre_aerolinea, grupo in grupos:
        cantidad_vuelos = len(grupo)
        cantidad_pasajeros = grupo['PASSENGERS'].sum()

        # Devolver información como un diccionario
        yield {
            'Aerolínea': nombre_aerolinea,
            'Cantidad de Vuelos': cantidad_vuelos,
            'Cantidad de Pasajeros': cantidad_pasajeros,
        }

def aerolinea_con_mas_vuelos(datos):
    # Encontrar la aerolínea con más vuelos
    aerolinea_max_vuelos = datos['CARRIER_NAME'].value_counts().idxmax()

    # Se obtiene un dataframe de la aerolinea con mas vuelos
    info_aerolinea = datos[datos['CARRIER_NAME'] == aerolinea_max_vuelos]

    # Mostrar información específica sobre la aerolínea con más vuelos
    print(f"Aerolínea con más vuelos: {aerolinea_max_vuelos}")
    # Numero de vuelos
    print(f"Número de vuelos: {len(info_aerolinea)}")
    # Numero de pasajeros
    print(f"Número total de pasajeros: {info_aerolinea['PASSENGERS'].sum()}")
    # Distancia total recorrida
    print(f"Distancia total recorrida: {info_aerolinea['DISTANCE'].sum()} km")

# Funcion para graficar la cantidad de vuelos en funcion del mes
def grafic_vuelos_mes(datos):
    datos['MONTH'] = pd.to_datetime(datos['MONTH'], format='%m')
    # Se agrupan los vuelos por mes
    vuelos_por_mes = datos.groupby(datos['MONTH'].dt.month)['PASSENGERS'].count()

    # Se crea el grafico
    plt.bar(vuelos_por_mes.index, vuelos_por_mes.values)
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Vuelos')
    plt.title('Cantidad de Vuelos por Mes')
    plt.show()

# Funcion para generar un diagrama circular del tipo de clases
def diagrama_circular_clases(datos):
    # Contar las clases
    clases_count = datos['CLASS'].value_counts()

    # Se obtienen las etiquetas y la cantidad de cada una
    labels = clases_count.index
    sizes = clases_count.values

    # Se crea el grafico
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Clases de Vuelo')
    plt.show()

# Diagrama de calor para analizar co-relacion de variables
def diagrama_calor(datos):
    # Dimensiones
    plt.figure(figsize=(10, 8))
    # Variables a analizar
    correlation_matrix = datos[['PASSENGERS', 'FREIGHT', 'DISTANCE', 'MONTH']].corr()
    # Se crea el diagrama
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlación entre Variables')
    plt.show()

# Funcion para generar el grafico de la cantidad de pasajeros segun la distancia de viaje.
def grafico_lineas(datos):
    sns.set(style="whitegrid") 

    plt.figure(figsize=(10, 6))
    # Crear un grafico de dispersión con líneas de conexión
    scatter_plot = sns.scatterplot(x="DISTANCE", y="PASSENGERS", data=datos, hue="CARRIER_NAME", palette="viridis")

    # Se crea el grafico
    plt.title("Relación entre Distancia de Vuelo y Cantidad de Pasajeros")
    plt.xlabel("Distancia (millas)")
    plt.ylabel("Cantidad de Pasajeros")
    plt.legend(title="Aerolínea")
    plt.show()

# Llamada a la función para cargar datos
datos = cargar_datos("src/T_T100D_MARKET_ALL_CARRIER.csv")

# Verificar que los datos se hayan cargado bien
if datos is not None:
    # Se imprimen los primerios 15 datos antes de la limpieza
    print("Datos cargados exitosamente:")
    print(datos.head(15))

    # Eliminando las columnas DEST (es redundante) y MAIL (es irrelevante)
    datos = datos.drop('DEST', axis=1)
    datos = datos.drop('MAIL', axis=1)

    # Convirtiendo la columna de cantidad de pasajeros a int
    datos['PASSENGERS'] = datos['PASSENGERS'].astype(int)

    # Se imprimen los primerios 15 datos despues de la limpieza
    print(datos.head(15))

    print("Info del dataframe\n")

    # Proporciona estadísticas descriptivas del DataFrame
    print(datos.describe())

    # Cálculo del promedio de la columna 'PASSENGERS'
    promedio_pasajeros = datos['PASSENGERS'].mean()
    print("\nPromedio de pasajeros:", promedio_pasajeros, "\n")

    # Cálculo de la moda de la columna 'DEST_CITY_NAME'
    moda_ciudad_destino = datos['DEST_CITY_NAME'].mode()
    print("\nCiudad destino mas frecuentada (moda)\n", moda_ciudad_destino, "\n")

    # Maxima distancia de vuelo
    distancia_maxima = datos['DISTANCE'].max()
    print("\nDistancia maxima de vuelo:", distancia_maxima, "\n")

    # Aerolinea mas usada
    moda_aerolinea = datos['CARRIER_NAME'].mode()
    print("\nAerolinea mas utilizada (moda)\n", moda_aerolinea, "\n")

    # De forma iterativa se crea el informe de aerolineas
    for informe in generar_informe_detallado(datos):
        print(informe, "\n")

    # llamada a la funcion para desplegar la info de la aerolinea con mas vuelos
    aerolinea_con_mas_vuelos(datos)

    # llamada para grafico 1
    grafic_vuelos_mes(datos)

    # llamada para grafico 2
    diagrama_circular_clases(datos)

    # llamada para grafico 3
    diagrama_calor(datos)
    
    # llamada para grafico 4
    grafico_lineas(datos)
