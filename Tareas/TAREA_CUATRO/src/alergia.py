class Alergia:
        def __init__(self):
            self.alergias_conocidas = {"huevos" : 1, "cacahuetes" : 2, "mariscos":4, "fresas":8, "tomates" : 16,
                                    "chocolate" : 32, "polen" : 64, "gatos" : 128, "sardina" : 256, "gluten": 512}
            self.alergias_nuevas = []


        def crearAlergia(self):
             print("Creando una alergia")


        def imprimirInfo(self):
            print('\nBienvenido a la base de datos de alergias')
            print('1. Consultar por todas las alergias')
            print('2. Consultar por una alergia')

            opcion = input("Digite la opcion que desea consultar o 0 para salir: ")

            if (opcion == "1"):
                print('A continuacion se detalla la informacion de las alergias en la base de datos')
                for alergia in self.alergias_conocidas:
                    print(self.alergias_conocidas[alergia], "-", alergia)
            elif(opcion == "2"):
                alergia = input("Digite la alergia que desea consultar: ")
                try: 
                    print("El codigo de alergia de", alergia, "es", self.alergias_conocidas[alergia])
                except:
                     print("Esa alergia no se encuentra en la base de datos")
            elif(opcion=="0"):
                 exit
            else: 
                 print("Esa no es una opcion posible") 
                

                 