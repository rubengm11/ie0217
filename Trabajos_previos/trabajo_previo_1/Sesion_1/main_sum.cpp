#include <iostream> // Mayor y menor para lib estandar
#include "sum.hpp"  // Comillas para archivos propios
using namespace std;

// Se deben compilar los archivos, el orden no importa

int main(){
    int num1 = 2;
    int num2 = 7;

    int result = sum(num1, num2);

    cout << result;
    cout << "\n";



    return 0;
}