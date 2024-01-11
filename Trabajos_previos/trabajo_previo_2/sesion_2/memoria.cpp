#include <iostream>
using namespace std;

int GlobalVariable = 42;

int main(){ 
    int StackVariable = 10;

    int* heapVariable = new int(20);

    cout << "GlobalVariable: " << GlobalVariable << endl;
    cout << "StackVariable: " << StackVariable << endl;
    cout << "HeapVariable: " << heapVariable << endl;

    delete heapVariable;

    return 0;
}