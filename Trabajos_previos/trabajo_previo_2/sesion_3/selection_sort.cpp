#include <iostream>
using namespace std;

// Funcion para intercambiar dos elementos en un arreglo
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}


void printArray(int array[], int size){
    for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}


void selectionSort(int array[], int size){
    // Itera sobre los elementos del arreglo
    for (int step = 0; step < size - 1; step++){
        int min_idx = step;
        for (int i = step + 1; i < size; i++){
            if (array[i] < array[min_idx])
                min_idx = i;
        }

        // Intercambia el elemento minimo encontrado con el primer elemento no ordenado
        swap(&array[min_idx], &array[step]);
    }
}

int main(){
    int data[] = {20, 12, 10, 15, 2};
    int size = sizeof(data) / sizeof(data[0]);


    selectionSort(data, size);

    cout << "Array ordenado en orden ascendente" << endl;
    printArray(data, size);

    return 0;
}