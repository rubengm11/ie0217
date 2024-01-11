#include <iostream>
using namespace std;

// Definicion de la clase Fraccion
class Fraccion {
    int numerador, denominador;

public:
    // Constructor de la clase Fraccion
    Fraccion(int n, int d) : numerador(n), denominador(d) {}

    // Sobrecarga del operador '+'
    Fraccion operator+(const Fraccion &f) {
        // Creación de un objeto Fraccion
        Fraccion resultado(
            numerador * f.denominador + f.numerador,
            denominador * f.denominador
        );
        return resultado;
    }

    void imprimir() {
        cout << numerador << "/" << denominador << endl;
    }
};

int main() {
    Fraccion f1(1, 2);
    Fraccion f2(3, 4);

    // Uso de la sobrecarga del operador '+' para sumar las dos fracciones
    Fraccion f3 = f1 + f2;

    f3.imprimir();

    return 0;
}