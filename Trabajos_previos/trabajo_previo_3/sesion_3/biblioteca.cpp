#include <iostream>
#include "biblioteca.hpp"
using namespace std;

void Biblioteca::agregarLibro(
    const string& titulo,
    const string& autor
) {
    catalogo.emplace_back(titulo, autor);
}


void Biblioteca::mostrarCatalogo(){
    for (const auto& libro : catalogo) {
        libro.mostrarInfo();
    }
}