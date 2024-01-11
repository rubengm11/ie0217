#include <iostream>
using namespace std;

// Funcion para imprimir el contenido del arreglo
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

void insertionSort(int array[], int size){
    for (int step = 1; step < size; step++) {
        int key = array[step];
        int j = step - 1;

        // Desplaza los elementos mayores que el elemento actual hacia la derecha
        while (key < array[j] && j >= 0){
            array[j + 1] = array[j];
            --j;
        }

        // Inserta el elemento actual en la posición correcta
        array[j + 1] = key;
    }
}

int main(){
    int data[] = {9, 5, 1, 4, 3};
    int size = sizeof(data) / sizeof(data[0]);

    insertionSort(data, size);

    cout << "Array en orden ascendente" << endl;
    printArray(data, size);

    return 0;
}