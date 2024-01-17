#include <iostream>
#include "libro.hpp"

Libro::Libro(
    const string& titulo, const string& autor
) : titulo(titulo), autor(autor){}

void Libro::mostrarInfo() const {
    cout << "Titulo " << titulo << ", Autor: " << autor << endl;

}
