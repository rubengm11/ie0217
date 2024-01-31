from alergia import Alergia

class TiposDeAlergias(Alergia):
    def __init__(self, lista):
        super().__init__()
        self.nuevas_alergias_usuario = lista
        self.nombres_sin_codigo = []
        self.codigo_sin_nombre = []
        self.nuevas_alergias_revisadas = []

    def analizarAlergia(self):
        for i in range(0, len(self.nuevas_alergias_usuario), 2):
            nombre = self.nuevas_alergias_usuario[i]
            try:
                codigo = int(self.nuevas_alergias_usuario[i + 1])
                if nombre.isalpha() and (int(codigo) > 0 and (int(codigo) & (int(codigo) - 1)) == 0):
                    self.nuevas_alergias_revisadas.append(nombre)
                    self.nuevas_alergias_revisadas.append(codigo)
                elif not nombre.isalpha():
                    self.codigo_sin_nombre.append(codigo)
                elif nombre.isalpha() and not (int(codigo) > 0 and (int(codigo) & (int(codigo) - 1)) == 0):
                    self.nombres_sin_codigo.append(nombre)
            except:
                if nombre in self.alergias_conocidas:
                    codigo = "codigo que cambiara en el futuro"
                    self.nuevas_alergias_revisadas.append(nombre)
                    self.nuevas_alergias_revisadas.append(codigo)
                else:
                    self.nombres_sin_codigo.append(nombre)

        puntuacion = 0
        
        print("lista ingresada por el usuario:", self.nuevas_alergias_usuario)
        

        lista_final_alergias = []
        

        for i in range(0, len(self.nuevas_alergias_revisadas), 2):
            nombre = self.nuevas_alergias_revisadas[i]
            codigo = self.nuevas_alergias_revisadas[i + 1]

            # Verificar si el nombre está en el diccionario y actualizar el código
            if nombre in self.alergias_conocidas:
                nuevo_codigo = self.alergias_conocidas[nombre]
                lista_final_alergias.append(nombre)
                lista_final_alergias.append(nuevo_codigo)
            else:
                lista_final_alergias.extend([nombre, codigo])

        for i in range(1, len(lista_final_alergias), 2):
            code = lista_final_alergias[i]
            puntuacion += code

        print('\nnuevas alergias sin codigo', self.nombres_sin_codigo)
        print('\nnuevos codigos sin nombre', self.codigo_sin_nombre)

        print("\nLa lista de alergias que posee es:", lista_final_alergias)

        print("\nSu puntuacion de alergia es:", puntuacion)

        try:
            print("\nEl porcentaje de acierto en las alergias fue de: ", (len(lista_final_alergias)/len(self.nuevas_alergias_usuario))*100, "\n")
        except:
            print("Se debe ingresar al menos una alergia para calcular el promedio")

            
