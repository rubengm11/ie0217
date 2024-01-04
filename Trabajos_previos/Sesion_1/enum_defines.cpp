#include <iostream>
using namespace std;

// Defines en mayusc

#define NUMERO_FAVORITO 56

enum seasons {
    verano = 15,
    invierno = 67,
    otonno = 90,

};


int main(){
    seasons s;

    s = invierno;

    cout << s << "\n";

    cout << NUMERO_FAVORITO << "\n";

    return 0;
}