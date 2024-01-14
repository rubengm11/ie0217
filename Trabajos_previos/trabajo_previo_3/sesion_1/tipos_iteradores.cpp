#include <iostream>
#include <forward_list>
using namespace std;

int main(){
    // lista (forward_list) con valores iniciales
    forward_list<int> nums{1, 2, 3, 4};

    // iterador que apunta al inicio de la lista
    forward_list<int>::iterator itr = nums.begin();

    // Recorrer la lista y multiplicar cada elemento por 2
    while(itr != nums.end()) {
        // Guardar el valor original antes de modificarlo
        int original_value = *itr;
        *itr = original_value * 2;

        itr++;
    }

    for (int num: nums){
        cout << num << ", ";
    }
    cout << endl;

    return 0;
}