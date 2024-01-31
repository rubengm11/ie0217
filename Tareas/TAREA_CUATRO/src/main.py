from alergia import Alergia
from evaluacion_especifica import EvaluacionEspecifica
from tipos_de_alergias import TiposDeAlergias
import timeit
import cProfile

def mostrar_menu():
    """Función principal que muestra un menú interactivo y realiza diversas operaciones según la opción seleccionada por el usuario."""
    while True:
        print("\nMenú:")
        print("1. Consultar nombres por puntuación de alergia")
        print("2. Consultar puntuación por nombres de alergias")
        print("3. Consultar por cualquier alergia")
        print("4. Mostrar información de alergias")
        print("5. Salir")

        alergia_consulta = []
        nuevas_alergias_usuario = []

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            try:
                puntuacion_usuario = int(input("Ingrese su puntuación de alergia: "))
                print("")
                usuario1 = EvaluacionEspecifica()
                usuario1.evaluar_alergias(puntuacion_usuario)
                usuario1.mostrar_info()

            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        elif opcion == "2":
            while True:
                alergia_usuario = input("Ingrese el nombre de la alergia: ")
                if alergia_usuario.isalpha():
                    print(f"Alergia ingresada: {alergia_usuario}")
                    alergia_consulta.append(alergia_usuario)
                else:
                    print("Error: Debe ingresar una cadena de caracteres sin números")
                salir = input("Digite 0 para salir y ver su información de alergia, o cualquier otra tecla para continuar: ")
                if salir == "0":
                    usuario2 = EvaluacionEspecifica()
                    usuario2.calcularPuntuacion(alergia_consulta)
                    break
        elif opcion == "3":
            while True:
                nombre_alergia = input("Ingrese el nombre de la alergia: ")
                codigo_alergia = input("Ingrese el código de la alergia: ")
                nuevas_alergias_usuario.append(nombre_alergia)
                nuevas_alergias_usuario.append(codigo_alergia)
                salir = input("Ingrese 0 para salir, enter para continuar.")
                if salir == "0":
                    nuevasAlergias = TiposDeAlergias(nuevas_alergias_usuario)
                    nuevasAlergias.analizarAlergia()
                    break
        elif opcion == "4":
            consulta = Alergia()
            consulta.imprimirInfo()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")


    # Análisis de la clase EvaluacionEspecifica
#    evaluacion = EvaluacionEspecifica()

    # Medir el tiempo de ejecución utilizando timeit para el método evaluar_alergias
#    tiempo_evaluar_alergias = timeit.timeit(lambda: evaluacion.evaluar_alergias(128), number=10)
#    print(f"Tiempo de ejecución de evaluar_alergias: {tiempo_evaluar_alergias} segundos")

    # Medir el tiempo de ejecución utilizando timeit para el método mostrar_info
#    tiempo_mostrar_info = timeit.timeit(evaluacion.mostrar_info, number=10)
#    print(f"Tiempo de ejecución de mostrar_info: {tiempo_mostrar_info} segundos")

    # Medir el tiempo de ejecución utilizando timeit para el método calcularPuntuacion
#    tiempo_calcular_puntuacion = timeit.timeit(lambda: evaluacion.calcularPuntuacion(["aguacate", "melocotón", "gatos"]), number=10)
#    print(f"Tiempo de ejecución de calcular_puntuacion: {tiempo_calcular_puntuacion} segundos")

    # Perfilado del código utilizando cProfile para cada método
#    cProfile.runctx("evaluacion.evaluar_alergias(128)", globals(), locals(), filename="perfilado_evaluar_alergias.txt")
#    cProfile.runctx("evaluacion.mostrar_info()", globals(), locals(), filename="perfilado_mostrar_info.txt")
#    cProfile.runctx("evaluacion.calcularPuntuacion(['aguacate', 'melocotón', 'gatos'])", globals(), locals(), filename="perfilado_calcular_puntuacion.txt")

    # Análisis de la clase TiposDeAlergias
#    tipos_alergias = TiposDeAlergias([])

    # Medir el tiempo de ejecución utilizando timeit para el método analizarAlergia
#    tiempo_analizar_alergia = timeit.timeit(tipos_alergias.analizarAlergia, number=10)
#    print(f"Tiempo de ejecución de analizarAlergia: {tiempo_analizar_alergia} segundos")

    # Perfilado del código utilizando cProfile para el método analizarAlergia
#    cProfile.runctx("tipos_alergias.analizarAlergia()", globals(), locals(), filename="perfilado_analizar_alergia.txt")

    # Análisis de la clase Alergia
#    alergia_obj = Alergia()

    # Medir el tiempo de ejecución utilizando timeit para el método crearAlergia
#    tiempo_crear_alergia = timeit.timeit(alergia_obj.crearAlergia, number=10)
#    print(f"Tiempo de ejecución de crearAlergia: {tiempo_crear_alergia} segundos")

#    # Perfilado del código utilizando cProfile para el método crearAlergia
#    cProfile.runctx("alergia_obj.crearAlergia()", globals(), locals(), filename="perfilado_crear_alergia.txt")
#
#    # Medir el tiempo de ejecución utilizando timeit para el método imprimirInfo
#    tiempo_imprimir_info = timeit.timeit(alergia_obj.imprimirInfo, number=1)
#    print(f"Tiempo de ejecución de imprimirInfo: {tiempo_imprimir_info} segundos")
#
#    # Perfilado del código utilizando cProfile para el método imprimirInfo
#    cProfile.runctx("alergia_obj.imprimirInfo()", globals(), locals(), filename="perfilado_imprimir_info.txt")

# Ejecutar la función principal
mostrar_menu()
