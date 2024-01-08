#include "funciones.hpp"
#include <string>
#include <ctime>    
#include <cstdlib>  
#include <random>
#include <cmath>

void mostrarMenu(){
    std::cout << "\n Menu\n";
    std::cout << "\n1. Modo facil\n";
    std::cout << "\n2. Modo dificil\n";
    std::cout << "\n3. Salir\n";

};


void procesarOpcion(){
    int opcion;
    std::cout << "\n Ingrese una opcion: ";
    std::cin >> opcion;

    switch(opcion){
        case 1: 
            modoFacil();
            break;

        case 2: 
            modoDificil();
            break;

        case 3:
            std::cout << "Saliendo del programa \n";
            exit(0);

        default:
            std::cout << "\n Opcion invalida. \n";
            return;

    }
}

void modoFacil(){
    std::cout << "\nUsted ha seleccionado el Modo Facil";

    int lim_inferior;
    std::cout << "\n Ingrese el limite inferior del intervalo: ";
    std::cin >> lim_inferior;

    int lim_superior;
    std::cout << "\n Ingrese el limite superior del intervalo: ";
    std::cin >> lim_superior;

    int size = lim_superior - lim_inferior + 1;
    int* intervalo = new int[size];

    for (int i = 0; i < size; ++i) {
        intervalo[i] = lim_inferior + i;
    };


    int intentos_totales = size / 3;
    int intentos_usados = 0;

    std::srand(std::time(nullptr));

    int indiceAleatorio = std::rand() % size;
    int numeroAleatorio = intervalo[indiceAleatorio];
    int numero_usuario;


    do {
    std::cout << "Ingresa tu intento: ";
    std::cin >> numero_usuario;

    if (numero_usuario == numeroAleatorio) {
        std::cout << "¡Felicidades! ¡Adivinaste el número!" << std::endl;
        break;
    } else {
        std::cout << "Intento incorrecto. ";
        if (numero_usuario < numeroAleatorio) {
            std::cout << "El número es mayor." << std::endl;
        } else {
            std::cout << "El número es menor." << std::endl;
        }}
        intentos_usados++;

        } while (intentos_usados < intentos_totales);
        if (intentos_usados == intentos_totales) {
            std::cout << "Lo siento, has agotado tus intentos. El número correcto era " << numeroAleatorio << "." << std::endl;
        }
    
    delete[] intervalo;
    return ;
    
}

void modoDificil(){
    std::cout << "\nUsted ha seleccionado el Modo Dificl";

    int lim_inferior;
    std::cout << "\n Ingrese el limite inferior del intervalo: ";
    std::cin >> lim_inferior;

    int lim_superior;
    std::cout << "\n Ingrese el limite superior del intervalo: ";
    std::cin >> lim_superior;

    int size = lim_superior - lim_inferior + 1;
    int* intervalo = new int[size];

    for (int i = 0; i < size; ++i) {
        intervalo[i] = lim_inferior + i;
    };


    int intentos_totales = size / 3;
    int intentos_usados = 0;


    std::srand(std::time(nullptr));

    int indiceAleatorio = std::rand() % size;
    int numeroAleatorio = intervalo[indiceAleatorio];
    int numero_usuario;

     do {
        std::cout << "Ingresa tu intento: ";
        std::cin >> numero_usuario;

        if (numero_usuario == numeroAleatorio) {
            std::cout << "¡Felicidades! ¡Adivinaste el número!" << std::endl;
            break;
        } else {
            int proximidad = std::abs(numeroAleatorio - numero_usuario);


            if (proximidad <= 3) {
                std::cout << "¡Hirviendo! Estás muy cerca." << std::endl;
            } else if (proximidad <= 6) {
                std::cout << "¡Caliente!" << std::endl;
            } else if (proximidad <= 9) {
                std::cout << "¡Frío!" << std::endl;
            } else {
                std::cout << "¡Congelado! Estás muy lejos." << std::endl;
            }
        }

        intentos_usados++;

    } while (intentos_usados < intentos_totales);
    if (intentos_usados == intentos_totales) {
            std::cout << "Lo siento, has agotado tus intentos. El número correcto era " << numeroAleatorio << "." << std::endl;
        }

    
    
    delete[] intervalo;
    return ;
    
}