import numpy as np
import pandas as pd

np.random.seed(29)

def promedio_por_estudiante(datos):
    # Excluimos la columna "Nombre" para calcular el promedio
    return datos.set_index("Nombre").mean(axis=1)

def promedio_por_asignatura(datos):
    # Excluimos la columna "Nombre" para calcular el promedio
    return datos.set_index("Nombre").mean()


def maxima_calificacion_por_estudiante(datos):
    # Excluimos la columna "Nombre" para encontrar la calificación máxima
    return datos.set_index("Nombre").max(axis=1)

def suma_total_por_asignatura(datos):
    # Excluimos la columna "Nombre" para calcular la suma total
    return datos.set_index("Nombre").sum()




# Nombres de asignaturas
asignaturas = ["Matemáticas", "Historia", "Ciencias", "Inglés", "Arte"]

# Nombres de estudiantes
nombres_estudiantes = ["Estudiante_A", "Estudiante_B", "Estudiante_C", "Estudiante_D", "Estudiante_E"]

# Crear un DataFrame con calificaciones aleatorias
calificaciones = np.random.randint(60, 100, size=(5, 5))

# Crear un DataFrame de Pandas con columnas separadas para cada asignatura
datos = pd.DataFrame(calificaciones, columns=asignaturas)

# Agregar una columna para los nombres de los estudiantes
datos["Nombre"] = nombres_estudiantes

# Reorganizar las columnas para tener "Nombre" al principio
column_order = ["Nombre"] + asignaturas
datos = datos[column_order]

# Imprimir el DataFrame resultante
print("DataFrame con columnas separadas por asignatura:")
print(datos, '\n')

print("Promedio por estudiante:\n", promedio_por_estudiante(datos))

print("\nPromedio por asignatura:\n", promedio_por_asignatura(datos), sep="")

print("\nCalificación máxima por estudiante:\n", maxima_calificacion_por_estudiante(datos))

print("\nSuma total por asignatura:\n", suma_total_por_asignatura(datos), sep="")