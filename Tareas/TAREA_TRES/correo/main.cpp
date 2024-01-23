#include "funciones.hpp"
#include <iostream>

int main() {
    // Crear una instancia del ValidadorCorreoElectronico
    ValidadorCorreoElectronico validador;

    // Solicitar al usuario que ingrese una dirección de correo electrónico
    std::string correo;
    std::cout << "Ingrese la dirección de correo electrónico: ";
    std::cin >> correo;

    // Validar la dirección de correo electrónico y mostrar el resultado
    if (validador.validarCorreo(correo)) {
        std::cout << "La dirección de correo electrónico es válida." << std::endl;
    } else {
        std::cout << "La dirección de correo electrónico no es válida." << std::endl;
    }

    return 0;
}