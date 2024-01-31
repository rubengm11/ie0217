from alergia import Alergia

class EvaluacionEspecifica(Alergia):
    def __init__(self):
        """Constructor de la clase EvaluacionEspecifica."""
        super().__init__()
        self.alergias_usuario = []

    def evaluar_alergias(self, puntuacion):
        """Evalúa las alergias del usuario basándose en la puntuación proporcionada.

        Args:
            puntuacion (int): Puntuación de alergia del usuario.
        """
        self.puntuacion = puntuacion
        if puntuacion > sum(self.alergias_conocidas.values()):
            print('Esa puntuación supera todas las alergias de la base de datos')
        else:
            for alergia, codigo in self.alergias_conocidas.items():
                if self.puntuacion & codigo:
                    self.alergias_usuario.append(alergia)

    def mostrar_info(self):
        """Muestra la información detallada de las alergias del usuario."""
        print('A continuación se detalla la información del usuario')
        print(f"Puntuación de alergia: {self.puntuacion}")
        for alergia in self.alergias_usuario:
            print(alergia, ":", self.alergias_conocidas[alergia])

    def calcularPuntuacion(self, lista_alergias):
        """Calcula la puntuación total de las alergias proporcionadas.

        Args:
            lista_alergias (list): Lista de alergias del usuario.

        Returns:
            None
        """
        alergias_encontradas = []
        alergias_no_encontradas = []
        puntuacion = 0

        for alergia in lista_alergias:
            if alergia in self.alergias_conocidas:
                puntuacion += self.alergias_conocidas[alergia]
                alergias_encontradas.append(alergia)
            else:
                alergias_no_encontradas.append(alergia)

        print("\nSus alergias son:", alergias_encontradas)
        print("Alergias no encontradas: ", alergias_no_encontradas)
        print("Su puntuación de alergia es:", puntuacion)



        
        

        