#include "funciones.hpp"

// Implementación de la clase Matriz
template <typename T>
Matriz<T>::Matriz(int filas, int columnas) : filas(filas), columnas(columnas) {
    datos.resize(filas, std::vector<T>(columnas));
}

template <typename T>
void Matriz<T>::pedirDatos() {
    std::cout << "Ingrese los datos de la matriz (" << filas << "x" << columnas << "):" << std::endl;
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            std::cout << "Fila " << i + 1 << ", Columna " << j + 1 << ": ";
            std::cin >> datos[i][j];
        }
    }
}

template <typename T>
bool Matriz<T>::esPosibleOperacion(const Matriz<T>& matriz1, const Matriz<T>& matriz2) {
    if (matriz1.tipo_operacion == 3) {
        return 1;
    } else return (matriz1.filas == matriz2.filas) && (matriz1.columnas == matriz2.columnas);
}

template <typename T>
Matriz<T> Matriz<T>::operator+(const Matriz<T>& otra) const {
    if (!esPosibleOperacion(*this, otra)) {
        throw std::invalid_argument("Las matrices no tienen las mismas dimensiones para la suma.");
    }

    Matriz<T> resultado(filas, columnas);
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            resultado.datos[i][j] = datos[i][j] + otra.datos[i][j];
        }
    }
    return resultado;
}

template <typename T>
Matriz<T> Matriz<T>::operator*(const Matriz<T>& otra) const {
    if (columnas != otra.filas) {
        throw std::invalid_argument("La multiplicación de matrices no es posible.");
    }

    Matriz<T> resultado(filas, otra.columnas);
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < otra.columnas; ++j) {
            for (int k = 0; k < columnas; ++k) {
                resultado.datos[i][j] += datos[i][k] * otra.datos[k][j];
            }
        }
    }
    return resultado;
}

template <typename T>
Matriz<T> Matriz<T>::operator-(const Matriz<T>& otra) const {
    if (!esPosibleOperacion(*this, otra)) {
        throw std::invalid_argument("Las matrices no tienen las mismas dimensiones para la resta.");
    }

    Matriz<T> resultado(filas, columnas);
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            resultado.datos[i][j] = datos[i][j] - otra.datos[i][j];
        }
    }
    return resultado;
}

std::complex<double> OperacionCompleja::sumar(std::complex<double> num1, std::complex<double> num2) {
    return num1 + num2;
}

template <typename T>
void imprimirMatriz(const Matriz<T>& matriz) {
    std::cout << "Matriz (" << matriz.filas << "x" << matriz.columnas << "):" << std::endl;
    for (int i = 0; i < matriz.filas; ++i) {
        for (int j = 0; j < matriz.columnas; ++j) {
            std::cout << matriz.datos[i][j] << "\t";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

std::tuple<int, int> pedirTamanoMatriz() {
    int filas, columnas;

    std::cout << "Ingrese el número de filas: ";
    std::cin >> filas;

    std::cout << "Ingrese el número de columnas: ";
    std::cin >> columnas;

    return std::make_tuple(filas, columnas);
}

int pedirOperacion() {
    int operacion;
    std::cout << "Ingrese el tipo de operacion que desea: " << std::endl;
    std::cout << "1. Suma " << std::endl;
    std::cout << "2. Resta " << std::endl;
    std::cout << "3. Multiplicacion " << std::endl;
    std::cin >> operacion;
    return operacion;
}

