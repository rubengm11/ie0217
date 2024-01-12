#ifndef COCHE_HPP   
#define COCHE_HPP

#include <iostream>

#include <string>
using namespace std;
#include "Vehiculo.hpp"

class Coche  : public Vehiculo{
    public:
        Coche(int velocidad, int numPuertas);
        void abrirPuertas();


    protected:
        int numPuertas;
};

#endif