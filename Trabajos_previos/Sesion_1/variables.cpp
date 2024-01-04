#include <iostream>
#include <string>
using namespace std;

// Declaracion de variable global
int g;

int main() {
    // Declaracion de variables locales
    int a, b;

    a = 10;
    b = 20;
    g = a + b;

    // Imprimir el resultado
    cout << g;

    // Declaracion y obtencion del valor de x
    int x;
    cout << "\nEscriba un numero: ";
    cin >> x;
    cout << "Su numero es: " << x;
    cout << "\n";

    int var2;
    int var1;

    //  x

    var2 = (var1 == 3) ? 15 : 27;

    cout << "var2 = " << var2 << "\n";



    cout << "\n";
    return 0;
}