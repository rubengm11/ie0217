#include <iostream>
using namespace std;

int main(){
    int num;
    cout << "Ingrese el numero total de estudiantes:" << endl;
    cin >> num;
    float* ptr;

    // Se asigna la memoria con base en el numero de estudiantes ingresado por el usuario
    ptr = new float[num];

    cout << "Ingrese el GPA de los estudiantes" << endl;
    for (int i; i < num; i++){
        cout<< "Estudiante" << i + 1 << ": ";
        cin >> *(ptr + i);
    }

    cout << "Desplegando GPS de los estudiantes" << endl;
    for (int i = 0; i < num; i++){

        cout << "Estudiante" << i + 1 << ": " << *(ptr + i) << endl;
    }

    // Se libera la memoria utilizando el puntero
    delete[] ptr;

    return 0;

}