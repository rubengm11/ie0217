#include <iostream>
#include <cstdlib>
using namespace std;

int main(){

    // Se asigna memoria de size int a un int ptr
    int* ptr = (int*)malloc(sizeof(int));

    *ptr = 5;

    cout << *ptr << endl;

    return 0;
}