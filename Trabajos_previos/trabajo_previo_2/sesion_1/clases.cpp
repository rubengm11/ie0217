#include <iostream>
using namespace std;

// Clase molde
class Molde {
    public:
        double largo;
        double ancho;
        double alto;

        // constructor de la clase molde
        Molde(double largo_p, double ancho_p, double alto_p) : largo(largo_p), ancho(ancho_p), alto(alto_p){
            cout << "Prueba de impresion" << endl;
        }
        // destructor de la clase molde
        ~Molde(){
            cout << "destructor de la clase molde" << endl;
        }

    // Metodo para calcular el area
    double CalcularArea(){
        return largo * ancho;

    }

        // Metodo para calcular el volumen
    double CalcularVolumen(){
        return largo * ancho * alto;


    }

};


int main(){
    int variable_entera;

    // Creacion de un objeto llamado pared de la clase Molde
    Molde pared(10.0, 20.0, 35.0);



    //pared.largo = 20.0;
    //pared.ancho = 13.2;
    //pared.alto = 23,4;

    cout << pared.largo << endl;
    //pared.largo = 25;
    cout << pared.largo << endl;


    // Calculo e impresion del area y volumen del objeto pared
    cout << "El area es: " << pared.CalcularArea() << endl;
    cout << "El voluemn es: " << pared.CalcularVolumen() << endl;

    return 0;
}