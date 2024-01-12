#include "MotoCoche.hpp"

int main(){
    MotoCoche miMotoCoche(90, 2, false);

    miMotoCoche.Coche::acelerar();
    miMotoCoche.abrirPuertas();
    miMotoCoche.usarCasco();

    return 0;
}