# Clase animal
class Animal:
    name = ""

    def eat(self):
        print('Puedo comer')

# Clase perro que hereda de animal
class Dog(Animal):
    def display(self):
        print('Mi nombre es:', self.name)

# Creacion del objeto y modificacion de su atributo nombre, metodo comer.
labrador = Dog()
labrador.name = "Rohu"
labrador.eat()

labrador.display()