# Definicion de la clase Person
class Person:
    # constructor de la clase Person
    def __init__(self, name, age):
        # Atributos de la clase
        self.name = name
        self.age = age

    # Método que muestra la información de la persona
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")