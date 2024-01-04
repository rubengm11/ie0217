#include <iostream>
#include <string>
using namespace std;


int main() {
    int number = 5;

    if (number == 3) {
        cout << "El numero es igual a 3";
    }
    else if (number == 7){
        cout << "El numero es igual a 7";
    } else {
        cout << "El numero no es ni 3 ni 7";
    }

    cout << "\nNumero analizado\n";

    // switch-case
    char oper;
    float num1, num2;
    cout << "Ingrese un operador (+, -, *, /)\n";
    cin >> oper;

    switch (oper) {

        case '+':
            cout << "Suma";
            break;

        case '-':
            cout << "Resta";
            break;

        case '*':
            cout << "Mult";
            break;

        case '/':
            cout << "Div";
            break;

        default:
            cout << "Operador no valido";
            break;

    }
cout << "\n";


    return 0;
}