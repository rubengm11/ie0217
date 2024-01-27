from alergia import Alergia
from evaluacion_especifica import EvaluacionEspecifica
from tipos_de_alergias import TiposDeAlergias
from evaluacion_general import EvaluacionGeneral

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Ingresar puntuacion de alergia")
        print("2. Ingresar nombre de alergia")
        print("3. Nueva alergia")
        print("4. Mostrar informacion de alergias")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            try:
                puntuacion_usuario = int(input("Ingrese su puntuacion de alergia: "))
                usuario1 = EvaluacionEspecifica(puntuacion_usuario)
                usuario1.evaluar_alergias()
                usuario1.mostrar_info()

            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        elif opcion == "2":
            alergia_usuario = input("Ingrese el nombre de la alergia: ")
            if alergia_usuario.isalpha():
                print(f"Alergia ingresada: {alergia_usuario}")
            else:
                print("Error: Debe ingresar una cadena de caracteres sin numeros")
        elif opcion == "3":
            nueva_alergia = input("Ingrese el nombre o codigo de la alergia: ")
            print(f"Nueva alergia ingresada: {nueva_alergia}")
        elif opcion == "4":
            consulta = Alergia()
            consulta.imprimirInfo()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")

mostrar_menu()

