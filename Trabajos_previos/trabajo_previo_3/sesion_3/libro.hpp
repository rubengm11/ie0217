#ifndef LIBRO_HPP
#define LIBRO_HPP
#include <string>
using namespace std;

class Libro{
    public:
        Libro(const string& titulo,const string& autor);
        void mostrarInfo()const;

    private:
        string titulo;
        string autor;
};



#endif