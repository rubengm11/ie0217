#include <iostream>
#include "estudiante.hpp"
#include <string>
using namespace std;

Estudiante::Estudiante(
    const string& nombre, int edad
) : nombre(nombre), edad(edad) {}

void Estudiante::mostrarDatos(){
    cout << "Nombre: " << nombre;
    cout << "Edad: " << edad << endl;
}