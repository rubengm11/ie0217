#include "Coche.hpp"

Coche::Coche(int velocidad, int numPuertas) : Vehiculo(velocidad), numPuertas(numPuertas){}

void Coche::abrirPuertas(){
    /* Codigo para abrir puertas*/
    cout << "Abriendo las " << numPuertas << " puertas del coche" << endl;
}