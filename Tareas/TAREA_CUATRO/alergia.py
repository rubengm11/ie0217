class Alergia:
        def __init__(self):
            self.alergias_conocidas = {"huevos" : 1, "cacahuetes" : 2, "mariscos":4, "fresas":8, "tomates" : 16,
                                    "chocolate" : 32, "polen" : 64, "gatos" : 128, "sardina" : 256, "gluten": 512}
            self.alergias_nuevas = []


        def crearAlergia(self):
            print('Creando una alergia')


        def imprimirInfo(self):
             print('A continuacion se detalla la informacion de las alergias en la base de datos')
             for alergia in self.alergias_conocidas:
                  print(self.alergias_conocidas[alergia], "-", alergia)