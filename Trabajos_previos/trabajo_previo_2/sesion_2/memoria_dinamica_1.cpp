#include <iostream>
using namespace std;


int main(){
    // Se declaran los punteros int y float
    int* pointInt;

    float* pointFloat;

    // Se asigna memoria dinamica
    pointInt = new int;
    pointFloat = new float;

    *pointInt = 45;
    *pointFloat = 45.45f;

    cout << *pointInt << endl;
    cout << *pointFloat << endl;

    // Liberar el espacio solicitado
    delete pointInt;
    delete pointFloat;

    return 0;



}