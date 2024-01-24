#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP

#include <iostream>
#include <vector>
#include <complex> 
#include <tuple>

template <typename T>
class Matriz {
public:
    std::vector<std::vector<T>> datos;
    int filas;
    int columnas;
    int tipo_operacion;

    Matriz(int filas, int columnas);

    void pedirDatos();

    static bool esPosibleOperacion(const Matriz<T>& matriz1, const Matriz<T>& matriz2);

    Matriz<T> operator+(const Matriz<T>& otra) const;

    Matriz<T> operator*(const Matriz<T>& otra) const;

    Matriz<T> operator-(const Matriz<T>& otra) const;
};

class OperacionCompleja {
public:
    static std::complex<double> sumar(std::complex<double> num1, std::complex<double> num2);
};

template <typename T>
void imprimirMatriz(const Matriz<T>& matriz);

std::tuple<int, int> pedirTamanoMatriz();

int pedirOperacion();

#endif