#include <iostream>
#include <string>
using namespace std;

int add(int, int);

void displayNum(int n1, float n2) {
    cout << "El entero es " << n1;
    cout << "\n";
    cout << "El double es " << n2;
    cout << "\n";


}

int main(int argc, char* argv[]) {
    
    int num1 = 5;
    double num2 = 24.4;
    displayNum(num1, num2);


    cout << "argc: " << argc;
    cout << "\n";
    cout << "argv[0]: " << argv[0];
    cout << "\n";
    cout << "argv[1]: " << argv[1];
    cout << "\n";
    cout << "argv[2]: " << argv[2];
    cout << "\n";
    cout << "argv[3]: " << argv[3];


    int x = add (15,25);
    cout << "\n";
    cout << "La suma es: " << x;


    cout << "\n";
    return 0;
}

int add(int a, int b) {
    return (a + b);
}