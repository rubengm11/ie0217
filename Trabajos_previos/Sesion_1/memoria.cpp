// &var representa la direccion en memoria de var
// Para punteros int* pointVar
// *pointVar para acceder al contenido de esa direccion de mem
// usar ptr->contenido


#include <iostream> // Mayor y menor para lib estandar
#include "sum.hpp"  // Comillas para archivos propios
using namespace std;

struct Distance {
    int feet;
    float inch;
};

int main(){
    Distance *ptr, d;

    ptr = &d;
    cout << "Ingrese distancia en pies: ";
    cin >> ptr->feet;
    cout << "Ingrese distancia en pulgadas: ";
    cin >> ptr->inch;

    cout << ptr->feet << " " << ptr->inch;

    return 0;

}
