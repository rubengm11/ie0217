#include <iostream>
using namespace std;

// Definicion de la clase Distance
class Distance {
private:
    int meter; 

    // Declaracion de la funcion amiga
    friend int addFive(Distance);

public:
    // Constructor
    Distance() : meter(0) {}
};

// Funcion amiga que puede acceder a los miembros privados de la clase Distance
int addFive(Distance d) {
    d.meter += 5; 
    return d.meter; 
}

int main() {
    Distance D;
    cout << "Distance: " << addFive(D);

    return 0;
}