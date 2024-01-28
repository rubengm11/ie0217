from alergia import Alergia

class TiposDeAlergias(Alergia):
    def __init__(self, lista):
        self.nuevas_alergias_usuario = lista
        self.nombres_sin_codigo = []
        self.codigo_sin_nombre = []
        self.diccionario_nuevas_alergias = {}

    def analizarAlergia(self):
        for i in range(0, len(self.nuevas_alergias_usuario), 2):
            nombre = self.nuevas_alergias_usuario[i]
            try:
                codigo = int(self.nuevas_alergias_usuario[i + 1])
                if nombre.isalpha() and (int(codigo) > 0 and (int(codigo) & (int(codigo) - 1)) == 0):
                    self.diccionario_nuevas_alergias[nombre] = codigo
                elif not nombre.isalpha():
                    self.codigo_sin_nombre.append(codigo)
                elif nombre.isalpha() and not (int(codigo) > 0 and (int(codigo) & (int(codigo) - 1)) == 0):
                    self.nombres_sin_codigo.append(nombre)
            except:
                self.nombres_sin_codigo.append(nombre)

        
        print("lista ingresada por el usuario:", self.nuevas_alergias_usuario)
        print('nuevas alergias con codigo', self.diccionario_nuevas_alergias)
        print('nuevas alergias sin codigo', self.nombres_sin_codigo)
        print('nuevos codigos sin nombre', self.codigo_sin_nombre)

            
