#include <iostream>
#include <stack>
using namespace std;

int main(){
    // Se crea un stack de enteros y se introducen valores
    stack<int> numbers;
    numbers.push(1);
    numbers.push(100);
    numbers.push(10);

    cout << "Los numeros son: ";

    while(!numbers.empty()) {
        // Imprimir el elemento superior
        cout << numbers.top() << ", ";
        // Eliminar el elemento superior del stack
        numbers.pop();
    }
    cout << endl;
   

    return 0;
}