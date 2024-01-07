#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP
#include <iostream>
#include <string>

const int MAX_EMPLEADOS = 10;

struct Empleado{
    int id;
    std::string nombre;
    double salario;

};

void mostrarMenu();
void procesarOpcion();
void escogerDificultad();
void iniciarJuego();
void seleccionarIntervalo();


#endif