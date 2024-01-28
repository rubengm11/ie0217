from evaluacion_especifica import EvaluacionEspecifica


class EvaluacionGeneral(EvaluacionEspecifica):
    def __init__(self):
        print('Constructor de evaluacion general')


    def puntuacion_general(self):
        print('hola')

    
    def noEncontrado(self):
        print('Aqui se imprimen las alergias no encontradas')


    def encontrarPromedio(self):
        print('Se calcula y se imprime el promedio de alergias')