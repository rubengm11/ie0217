class SuperClass:
    def super_metod(self):
        print("Super Class method called")


# Clase derivada de superclass
class DerivedClass1 (SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

#clas derivada de DerivedClass1
class DerivedClass2 (DerivedClass1):
    def derived2_method(self):
        print("Derived class 2 method called")

# Creacion del objeto y llamada de sus metodos
d2 = DerivedClass2()
d2.super_metod()
d2.derived1_method()
d2.derived2_method()
