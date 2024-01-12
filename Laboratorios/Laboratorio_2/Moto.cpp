#include "Moto.hpp"
using namespace std;

Moto::Moto(int velocidad, bool tieneCasco):Vehiculo(velocidad), tieneCasco(tieneCasco){}

void Moto::usarCasco(){
    if(tieneCasco){
        cout << "Usando casco mientras conduzco" << endl;

    } else {
        cout << "Alerta! No tiene casco." << endl;
    }
}