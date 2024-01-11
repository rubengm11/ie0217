#include <iostream>
using namespace std;

// Prototipo de ClassB
class ClassB;

// Definicion ClassA
class ClassA {
public:
    // Constructor 
    ClassA() : numA(12) {}

private:
    int numA; 
    friend int add(ClassA, ClassB); // Declaracion de la funcion amiga
};

// Definicion de ClassB
class ClassB {
public:
    // Constructor
    ClassB() : numB(1) {}

private:
    int numB;
    friend int add(ClassA, ClassB); // Declaracion de la funcion amiga
};

// Funcion amiga que puede acceder a los miembros privados de ClassA y ClassB
int add(ClassA objectA, ClassB objectB) {
    return (objectA.numA + objectB.numB);
}

int main() {
    ClassA objectA;
    ClassB objectB;

    cout << "Sum: " << add(objectA, objectB);

    return 0;
}