# definicion de la clase
class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# Creacion del objeto
study_room = Room()

# Valores de los atributos
study_room.length = 42.5
study_room.breadth = 30.8

study_room.calculate_area()