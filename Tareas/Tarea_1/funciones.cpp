#include "funciones.hpp"
#include <string>

void mostrarMenu(){
    std::cout << "\nMenu\n";
    std::cout << "\n1. Escoger dificultad\n";
    std::cout << "\n2. Iniciar juego\n";
    std::cout << "\n3. Seleccionar intervalo\n";
    std::cout << "\n4. Salir \n";

};


void procesarOpcion(){
    int opcion;
    std::cout << "\n Ingrese una opcion: ";
    std::cin >> opcion;

    switch(opcion){
        case 1: 
            escogerDificultad();
            break;

        case 2: 
            iniciarJuego();
            break;

        case 3:
            seleccionarIntervalo();
            break;

        case 4:
            std::cout << "Saliendo del programa \n";
            exit(0);

        default:
            std::cout << "\n Opcion invalida. \n";



    }
}

void escogerDificultad(){
    
}

void iniciarJuego(){
    
}

void seleccionarIntervalo(){

}