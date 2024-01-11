#include <iostream>
using namespace std;

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Funcion para imprimir el contenido del arreglo
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

// Funcion que realiza el particionamiento del arreglo
int partition(int array[], int low, int high) {
    int pivot = array[high]; // Se elige el ultimo elemento como pivote
    int i = low - 1;

    // Recorre el arreglo y pone elementos menores que el pivote a la izquierda
    for (int j = low; j <= high - 1; j++) {
        if (array[j] < pivot) {
            i++;
            swap(array[i], array[j]);
        }
    }

    // Pone el pivote en la posicion correcta
    swap(array[i + 1], array[high]);
    return i + 1;
}


void quickSort(int array[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(array, low, high);

        // ordenar los arreglos antes y despues del pivote
        quickSort(array, low, pivotIndex - 1);
        quickSort(array, pivotIndex + 1, high);
    }
}

int main() {
    int data[] = {20, 12, 10, 15, 2};
    int size = sizeof(data) / sizeof(data[0]);


    quickSort(data, 0, size - 1);

    cout << "Array ordenado en orden ascendente: " << endl;
    printArray(data, size);

    return 0;
}