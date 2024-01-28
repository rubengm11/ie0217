from alergia import Alergia

class EvaluacionEspecifica(Alergia):
    def __init__(self, puntuacion):
        super().__init__()
        self.puntuacion = puntuacion
        self.alergias_usuario = []


    def evaluar_alergias(self):
        if self.puntuacion > sum(self.alergias_conocidas.values()):
             print('Esa puntuacion supera todas las alergias de la base de datos')
        else:
            for alergia, codigo in self.alergias_conocidas.items():
                if self.puntuacion & codigo:
                    self.alergias_usuario.append(alergia)


    def mostrar_info(self):
        print('A continuacion se detalla la info del usuario')
        print(f"Puntuacion de alergia: {self.puntuacion}")
        for alergia in self.alergias_usuario:
            print(alergia, ":", self.alergias_conocidas[alergia])

    def calcularPuntuacion(self, list):
        alergias_encontradas = []
        alergias_no_encontradas = []
        for alergia in list:
            if alergia in self.alergias_conocidas:
                self.puntuacion += self.alergias_conocidas[alergia]
                alergias_encontradas.append(alergia)
            else:
                alergias_no_encontradas.append(alergia)
        print("\nSus alergias son:", alergias_encontradas)
        print("Alergias no encontradas: ", alergias_no_encontradas)
        print("Su puntuacion de alergia es:", self.puntuacion)
        