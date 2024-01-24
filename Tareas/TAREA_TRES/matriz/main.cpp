#include <iostream>
#include "funciones.hpp"

int main() {
    int tipo_matriz;
    std::cout << "Ingrese el tipo de matriz que desea implementar" << std::endl;
    std::cout << "1. Matriz de numeros reales (ints y floats)" << "\n" << "2. Matriz de numeros complejos" << std::endl;
    std::cin >> tipo_matriz;

    // Pedir tamaño de la primera matriz
    std::tuple<int, int> tamanoMatriz1 = pedirTamanoMatriz();
    int filasMatriz1 = std::get<0>(tamanoMatriz1);
    int columnasMatriz1 = std::get<1>(tamanoMatriz1);

    std::cout << "Tamaño de la primera matriz: " << filasMatriz1 << "x" << columnasMatriz1 << std::endl;

    // Pedir tamaño de la segunda matriz
    std::tuple<int, int> tamanoMatriz2 = pedirTamanoMatriz();
    int filasMatriz2 = std::get<0>(tamanoMatriz2);
    int columnasMatriz2 = std::get<1>(tamanoMatriz2);

    std::cout << "Tamaño de la segunda matriz: " << filasMatriz2 << "x" << columnasMatriz2 << std::endl;

    if (tipo_matriz == 1) {
        // Operaciones para matrices de números reales (ints y floats)
        Matriz<int> matriz1(filasMatriz1, columnasMatriz1);
        Matriz<int> matriz2(filasMatriz2, columnasMatriz2);

        matriz1.pedirDatos();
        matriz2.pedirDatos();

        try {
            matriz1.tipo_operacion = pedirOperacion();
            Matriz<int> resultadoSuma = matriz1 + matriz2;
            Matriz<int> resultadoResta = matriz1 - matriz2;
            Matriz<int> resultadoMultiplicacion = matriz1 * matriz2;
            switch (matriz1.tipo_operacion) {
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
    } else if (tipo_matriz == 2) {
        // Operaciones para matrices de números complejos
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
    } else {
        std::cout << "Error: Digite una opción válida" << std::endl;
    }

    return 0;
}