#ifndef VEHICULO_HPP
#define VEHICULO_HPP

#include <iostream>

#include <string>
using namespace std;

class Vehiculo {
    public:
        Vehiculo(int velocidad);
        void acelerar();
        void frenar();


    protected:
        int velocidad;
};

#endif