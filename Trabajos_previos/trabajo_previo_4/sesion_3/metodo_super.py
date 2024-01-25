# Clase animal
class Animal:
    name = ""

    def eat(self):
        print('Puedo comer')

# Clase perro que hereda de animal
class Dog(Animal):
    def eat(self):
        super().eat()
        print("Me gusta comer huesos")

# Creacion del objeto y modificacion de su atributo nombre, metodo comer.
labrador = Dog()
labrador.eat()
