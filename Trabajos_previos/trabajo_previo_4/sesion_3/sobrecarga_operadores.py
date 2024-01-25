class Point:
    # Constructor
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    # Metodo para imprimir
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
    # Metodo para sumar
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
# creacion de objeto y suma
p1 = Point(1,2)
p2 = Point(2,3)

print(p1+p2)