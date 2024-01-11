#include <iostream>
using namespace std;

// Funcion para intercambiar dos elementos en un arreglo
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Funcion para realizar el ordenamiento con Bubble Sort
void bubbleSort(int array[], int size) {
    // Itera sobre todos los elementos del arreglo
    for (int step = 0; step < size - 1; ++step) {
        for (int i = 0; i < size - step - 1; ++i) {
            // Compara elementos adyacentes y los intercambia si estan en el orden incorrecto
            if (array[i] > array[i + 1]) {
                swap(array[i], array[i + 1]);
            }
        }
    }
}

// Funcion para imprimir el contenido del arreglo
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << " " << array[i];
    }
    cout << "\n";
}

int main() {
    int data[] = {-2, 45, 0, 11, -9};

    int size = sizeof(data) / sizeof(data[0]);

    bubbleSort(data, size);

    cout << "Array ordenado en orden ascendente: \n";
    printArray(data, size);

    return 0;
}