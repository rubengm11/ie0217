/**
 * @file main.cpp
 * @brief Programa principal que utiliza las funciones definidas en funciones.cpp
 *
 * Este archivo contiene la lógica principal del programa, que utiliza las funciones
 * definidas en funciones.cpp.
 */


#include <iostream>
#include "funciones.hpp"

int main() {
    while (1)
    {
        mostrarMenu();
        procesarOpcion();
    }
    
    return 0;
}