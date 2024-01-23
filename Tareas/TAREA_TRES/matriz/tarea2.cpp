#include <iostream>
#include <vector>
#include <complex> 
#include <tuple>
#include <cstdlib>

// Clase Matriz
template <typename T>
class Matriz {

public:
    std::vector<std::vector<T>> datos;
    int filas;
    int columnas;
    int tipo_operacion;
    // Constructor
    Matriz(int filas, int columnas) : filas(filas), columnas(columnas) {
        datos.resize(filas, std::vector<T>(columnas));
    }


    // Método para pedir tamaño y datos de la matriz
    void pedirDatos() {
        std::cout << "Ingrese los datos de la matriz (" << filas << "x" << columnas << "):" << std::endl;
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < columnas; ++j) {
                std::cout << "Fila " << i + 1 << ", Columna " << j + 1 << ": ";
                std::cin >> datos[i][j];
            }
        }
    }

    // Método para validar si es posible realizar la operación entre matrices
    static bool esPosibleOperacion(const Matriz<T>& matriz1, const Matriz<T>& matriz2) {
        if (matriz1.tipo_operacion == 3) {
            return (matriz1.filas == matriz2.columnas);
        } else return (matriz1.filas == matriz2.filas) && (matriz1.columnas == matriz2.columnas);
        
    }

    // Método para realizar operaciones entre matrices utilizando sobrecarga de operadores
    Matriz<T> operator+(const Matriz<T>& otra) const {
        if (!esPosibleOperacion(*this, otra)) {
            throw std::invalid_argument("Las matrices no tienen las mismas dimensiones para la suma.");
            std::exit(EXIT_FAILURE);
        }

        Matriz<T> resultado(filas, columnas);
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < columnas; ++j) {
                resultado.datos[i][j] = datos[i][j] + otra.datos[i][j];
            }
        }
        return resultado;
    }

    // Métodos para la multiplicación y resta de matrices
    Matriz<T> operator*(const Matriz<T>& otra) const {
        if (columnas != otra.filas) {
            throw std::invalid_argument("La multiplicación de matrices no es posible.");
            std::exit(EXIT_FAILURE);
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

    Matriz<T> operator-(const Matriz<T>& otra) const {
        if (!esPosibleOperacion(*this, otra)) {
            throw std::invalid_argument("Las matrices no tienen las mismas dimensiones para la resta.");
            std::exit(EXIT_FAILURE);

        }

        Matriz<T> resultado(filas, columnas);
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < columnas; ++j) {
                resultado.datos[i][j] = datos[i][j] - otra.datos[i][j];
            }
        }
        return resultado;
    }
};

// Clase OperacionCompleja para operaciones con números complejos
class OperacionCompleja {
public:
    // Método para operaciones con números complejos
    static std::complex<double> sumar(std::complex<double> num1, std::complex<double> num2) {
        return num1 + num2;
    }
    // Otros métodos para operaciones complejas pueden ser implementados de manera similar
};

// Función para imprimir una matriz
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

int pedirOperacion(){
    int operacion;
        std::cout << "Ingrese el tipo de operacion que desea: " << std::endl;
        std::cout << "1. Suma " << std::endl;
        std::cout << "2. Resta " << std::endl;
        std::cout << "3. Multiplicacion " << std::endl;
        std::cin >> operacion;
    return operacion;
}


int main() {
    std::tuple<int, int> tamanoMatriz1 = pedirTamanoMatriz();
    int filasMatriz1 = std::get<0>(tamanoMatriz1);
    int columnasMatriz1 = std::get<1>(tamanoMatriz1);

    std::cout << "Tamaño de la primera matriz: " << filasMatriz1 << "x" << columnasMatriz1 << std::endl;

    std::tuple<int, int> tamanoMatriz2 = pedirTamanoMatriz();
    int filasMatriz2 = std::get<0>(tamanoMatriz2);
    int columnasMatriz2 = std::get<1>(tamanoMatriz2);

    std::cout << "Tamaño de la segunda matriz: " << filasMatriz2 << "x" << columnasMatriz2 << std::endl;

    Matriz<int> matriz1(filasMatriz1, columnasMatriz1);
    Matriz<int> matriz2(filasMatriz2, columnasMatriz2);

    matriz1.pedirDatos();
    matriz2.pedirDatos();

    try {
        matriz1.tipo_operacion = pedirOperacion();
        Matriz<int> resultadoSuma = matriz1 + matriz2;
        Matriz<int> resultadoResta = matriz1 - matriz2;
        Matriz<int> resultadoMultiplicacion = matriz1 * matriz2;
        switch (matriz1.tipo_operacion){
        case 1:
            imprimirMatriz(resultadoSuma);
            break;
        
        case 2:
            imprimirMatriz(resultadoResta);
            break;

        case 3:
            imprimirMatriz(resultadoMultiplicacion);
            break;

        default:
            break;
        }

    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    // Ejemplo de uso con números complejos
    Matriz<std::complex<double>> matrizCompleja1(2, 2);
    Matriz<std::complex<double>> matrizCompleja2(2, 2);

    matrizCompleja1.pedirDatos();
    matrizCompleja2.pedirDatos();

    try {
        Matriz<std::complex<double>> resultadoSumaCompleja = matrizCompleja1 + matrizCompleja2;
        imprimirMatriz(resultadoSumaCompleja);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}