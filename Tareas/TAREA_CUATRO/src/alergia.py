class Alergia:
    def __init__(self):
        """Constructor de la clase Alergia.

        Inicializa la base de datos de alergias conocidas y la lista de alergias nuevas.
        """
        self.alergias_conocidas = {
            "huevos": 1, "cacahuetes": 2, "mariscos": 4, "fresas": 8, "tomates": 16,
            "chocolate": 32, "polen": 64, "gatos": 128, "sardina": 256, "gluten": 512
        }
        self.alergias_nuevas = []

    def crearAlergia(self):
        """Método para crear una nueva alergia.

        Imprime un mensaje indicando que se está creando una alergia.
        """
        print("Creando una alergia")

    def imprimirInfo(self):
        """Método para imprimir información sobre las alergias.

        Muestra un menú para consultar información sobre las alergias conocidas.
        """
        print('\nBienvenido a la base de datos de alergias')
        print('1. Consultar por todas las alergias')
        print('2. Consultar por una alergia')
        print('0. Salir')

        opcion = input("Digite la opcion que desea consultar o 0 para salir: ")

        if opcion == "1":
            print('A continuacion se detalla la informacion de las alergias en la base de datos')
            for alergia in self.alergias_conocidas:
                print(self.alergias_conocidas[alergia], "-", alergia)
        elif opcion == "2":
            alergia = input("Digite la alergia que desea consultar: ")
            try:
                print("El codigo de alergia de", alergia, "es", self.alergias_conocidas[alergia])
            except KeyError:
                print("Esa alergia no se encuentra en la base de datos")
        elif opcion == "0":
            exit()  # Se corrigió el llamado a la función exit
        else:
            print("Esa no es una opcion posible")
                

                 