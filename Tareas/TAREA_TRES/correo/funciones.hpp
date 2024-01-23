#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP

#include <string>

class ValidadorCorreoElectronico {
public:
    // Método para validar una dirección de correo electrónico
    bool validarCorreo(const std::string& correo);

private:
    // Método privado para verificar si la cadena contiene el carácter '@'
    bool tieneArroba(const std::string& correo) const;
};

#endif