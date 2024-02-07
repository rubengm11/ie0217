import numpy as np
import pandas as pd

np.random.seed(29)

# Funcion para calcular la el promedio por estudiante en todas las asignaturas
def promedio_por_estudiante(datos):
    # Se exclutye la columna "Nombre" para calcular el promedio con los numeros
    return datos.set_index("Nombre").mean(axis=1)

# Funcion para calcular el promedio de calificaciones por asignatura 
def promedio_por_asignatura(datos):
    # Se exclutye la columna "Nombre" para calcular el promedio con los numeros
    return datos.set_index("Nombre").mean()

# Funcion para calcular la nota mas alta por estudiante
def maxima_calificacion_por_estudiante(datos):
    # Se exclutye la columna "Nombre" para calcular el promedio con los numeros
    return datos.set_index("Nombre").max(axis=1)

# Funcion para calcular la suma total por asignatura
def suma_total_por_asignatura(datos):
    # Se exclutye la columna "Nombre" para calcular el promedio con los numeros
    return datos.set_index("Nombre").sum()

# Nombres de asignaturas
asignaturas = ["Matemáticas", "Historia", "Ciencias", "Inglés", "Arte"]

# Nombres de estudiantes
nombres_estudiantes = ["Estudiante_A", "Estudiante_B", "Estudiante_C", "Estudiante_D", "Estudiante_E"]

# Crear un DataFrame con calificaciones aleatorias
calificaciones = np.random.randint(60, 100, size=(5, 5))
datos = pd.DataFrame(calificaciones, columns=asignaturas)

# Agregar una columna para los nombres de los estudiantes
datos["Nombre"] = nombres_estudiantes

# Reorganizar las columnas para tener "Nombre" al principio
column_order = ["Nombre"] + asignaturas
datos = datos[column_order]

# Imprimir el DataFrame resultante
print("DataFrame con columnas separadas por asignatura:")
print(datos, '\n')

# Promedio por estudiante en todas las asignaturas
print("Promedio por estudiante:\n", promedio_por_estudiante(datos))

# Promedio por asignatura
print("\nPromedio por asignatura:\n", promedio_por_asignatura(datos), sep="")

# Calificaciones maximas por estudiante
print("\nCalificación máxima por estudiante:\n", maxima_calificacion_por_estudiante(datos))

# Suma total por asignatura
print("\nSuma total por asignatura:\n", suma_total_por_asignatura(datos), sep="")