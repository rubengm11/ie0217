class PowTwo:
    """Clase para implementar un iterador de potencias de dos"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# Crear una instancia de la clase PowTwo con un límite de 3
numbers = PowTwo(3)

# Obtener un iterador de la instancia
iterator = iter(numbers)

# Iterar a través del iterador e imprimir cada elemento
for i in iterator:
    print(i)
