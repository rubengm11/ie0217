/**
 * @file funciones.cpp
 * @brief Implementación de las funciones definidas en funciones.hpp
 *
 * Este archivo contiene las implementaciones de las funciones declaradas en funciones.hpp.
 * Detalles adicionales sobre el propósito y funcionamiento de cada función.
 */

#include "funciones.hpp"
#include <string>
#include <ctime>    
#include <cstdlib>  
#include <random>
#include <cmath>
using namespace std;

/**
 * @brief Función que muestra el menu.
 *
 * Despliega en consola las opciones disponibles del programa.
 */
void mostrarMenu(){
    cout << "\n Menu\n";
    cout << "\n1. Modo facil\n";
    cout << "\n2. Modo dificil\n";
    cout << "\n3. Salir\n";

};

/**
 * @brief Función que procesa la opcion ingresada por el usuario.
 *
 * Utiliza un switch case para definir la funcion a llamar con base en la seleccion del usuario.
 */
void procesarOpcion(){
    int opcion;
    cout << "\n Ingrese una opcion: ";
    cin >> opcion;

    switch(opcion){
        case 1: 
            modoFacil();
            break;

        case 2: 
            modoDificil();
            break;

        case 3:
            cout << "Saliendo del programa \n";
            exit(0);

        default:
            cout << "\n Opcion invalida. \n";
            return;

    }
};

// Funcion para el modo de juego facil.
void modoFacil(){
    cout << "\nUsted ha seleccionado el Modo Facil";

    // Se solicita el limite inferior y superior del intervalo
    int limInferior;
    cout << "\n Ingrese el limite inferior del intervalo: ";
    cin >> limInferior;

    int limSuperior;
    cout << "\n Ingrese el limite superior del intervalo: ";
    cin >> limSuperior;

    // Se crea un array a partir de los limites ingresados por el usuario.
    int size = limSuperior - limInferior + 1;
    int* intervalo = new int[size];

    for (int i = 0; i < size; ++i) {
        intervalo[i] = limInferior + i;
    };

    // Se define la cantidad de intentos y se genera un numero al azar de ese intervalo.
    int intentosTotales = size / 3;
    int intentosUsados = 0;

    srand(time(nullptr));

    // Se genera un numero aleatorio utilizando la funcion rand
    int indiceAleatorio = rand() % size;
    int numeroAleatorio = intervalo[indiceAleatorio];
    int numeroUsuario;

    // Se solicita el numero al usuario y se analiza si es mayor, menor o igual al numero correcto.
    // Si la cantidad de intentos es igual a la cantidad maxima, el usuario pierde y vuelve al menu.
    do {
    cout << "Ingresa tu intento: ";
    cin >> numeroUsuario;

    if (numeroUsuario == numeroAleatorio) {
        cout << "¡Felicidades! ¡Adivinaste el número!" << endl;
        break;
    } else {
        cout << "Intento incorrecto. ";
        if (numeroUsuario < numeroAleatorio) {
            cout << "El número es mayor." << endl;
        } else {
            cout << "El número es menor." << endl;
        }}
        intentosUsados++;

        } while (intentosUsados < intentosTotales);
        if (intentosUsados == intentosTotales) {
            cout << "Lo siento, has agotado tus intentos. El número correcto era " << numeroAleatorio << "." << endl;
        }
    
    delete[] intervalo;
    return ;
    
}

// Funcioon para el modo dificil
void modoDificil(){
    cout << "\nUsted ha seleccionado el Modo Dificl";

    // Se solicita el limite inferior y superior del intervalo.
    int limInferior;
    cout << "\n Ingrese el limite inferior del intervalo: ";
    cin >> limInferior;

    int limSuperior;
    cout << "\n Ingrese el limite superior del intervalo: ";
    cin >> limSuperior;

    // Se crea un array con dichos valores
    int size = limSuperior - limInferior + 1;
    int* intervalo = new int[size];

    for (int i = 0; i < size; ++i) {
        intervalo[i] = limInferior + i;
    };

    // Se define la cantidad de intentos y se genera un numero al azar de ese intervalo.
    int intentosTotales = size / 3;
    int intentosUsados = 0;


    srand(time(nullptr));

    int indiceAleatorio = rand() % size;
    int numeroAleatorio = intervalo[indiceAleatorio];
    int numeroUsuario;


    // Se solicita el numero al usuario y se analiza si es esta lejos, muy lejos, cerca o muy cerca del numero correcto con la funcion abs.
    // Si la cantidad de intentos es igual a la cantidad maxima, el usuario pierde y vuelve al menu.
     do {
        cout << "Ingresa tu intento: ";
        cin >> numeroUsuario;

        if (numeroUsuario == numeroAleatorio) {
            cout << "¡Felicidades! ¡Adivinaste el número!" << endl;
            break;
        } else {
            int proximidad = abs(numeroAleatorio - numeroUsuario);


            if (proximidad <= 3) {
                cout << "¡Hirviendo! Estás muy cerca." << endl;
            } else if (proximidad <= 6) {
                cout << "¡Caliente!" << endl;
            } else if (proximidad <= 9) {
                cout << "¡Frío!" << endl;
            } else {
                cout << "¡Congelado! Estás muy lejos." << endl;
            }
        }

        intentosUsados++;

    } while (intentosUsados < intentosTotales);
    if (intentosUsados == intentosTotales) {
            cout << "Lo siento, has agotado tus intentos. El número correcto era " << numeroAleatorio << "." << endl;
        }

    
    
    delete[] intervalo;
    return ;
    
}
