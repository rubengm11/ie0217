#include "funciones.hpp"
#include <iostream>
#include <regex>

// Implementación del método para validar una dirección de correo electrónico
bool ValidadorCorreoElectronico::validarCorreo(const std::string& correo) {
    try {
        // Verifica si la cadena contiene el carácter '@'
        if (!tieneArroba(correo)) {
            throw std::invalid_argument("La dirección de correo electrónico debe contener un '@'.");
        }

        // Expresión regular para validar el formato de la dirección de correo electrónico
        std::regex patron("^([a-zA-Z0-9_.-]{1,15})@([a-zA-Z]+\\.[a-zA-Z]{2,})$");

        // Comprueba si la cadena cumple con el formato de la expresión regular
        return std::regex_match(correo, patron);
    } catch (const std::invalid_argument& e) {
        // Captura excepciones y muestra un mensaje de error
        std::cerr << "Error: " << e.what() << std::endl;
        return false;
    }
}

// Implementación del método privado para verificar si la cadena contiene el carácter '@'
bool ValidadorCorreoElectronico::tieneArroba(const std::string& correo) const {
    return correo.find('@') != std::string::npos;
}