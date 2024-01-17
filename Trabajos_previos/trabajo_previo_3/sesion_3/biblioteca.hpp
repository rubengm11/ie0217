#ifndef BIBLIOTECA_HPP
#define BIBLIOTECA_HPP

#include <vector>
#include "libro.hpp"
using namespace std;


class Biblioteca {
    public:
        void agregarLibro(
            const string& titulo,
            const string& autor
        );
        void mostrarCatalogo();

    private:
        vector<Libro> catalogo;
};




#endif