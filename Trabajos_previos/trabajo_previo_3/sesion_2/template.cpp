#include <iostream>
using namespace std;

template <typename T>

// Template
T add (T num1, T num2){
    return num1 + num2;
}

int main(){
    int result1;
    double result2;

    // Funcion add con enteros
    result1 = add<int>(2, 3);
    cout << "Resultado entero: " << result1 << endl;

    // Funcion add con doubles
    result2 = add<double>(2.2, 3.5);
    cout << "Resultado double: " << result2 << endl;

    return 0;
}