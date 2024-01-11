#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int *ptr;
    ptr = (int *)calloc(5, sizeof(int));
    if (!ptr) {
        cout << "Asignacion de memoria faliida" << endl;
        exit(1);
    }
    cout << "Inicializando valores" << endl;

    for (int i = 0; i < 5; i++){
        ptr[i] = i * 2 + 1;
    }
    cout << "Valores inicializados" << endl;

    for (int i = 0; i < 5; i++){
        cout << *(ptr+i) << endl;
    }
    free(ptr);
    return 0;
}