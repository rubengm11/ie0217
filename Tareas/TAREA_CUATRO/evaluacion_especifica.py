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
            #return self.alergias_usuario


    def mostrar_info(self):
        print('A continuacion se detalla la info del usuario')
        print(f"Puntuacion de alergia: {self.puntuacion}")
        #print(self.alergias_usuario)
        for alergia in self.alergias_usuario:
            print(alergia, ":", self.alergias_conocidas[alergia])

        print("")
        print("")
        super().imprimirInfo()
        