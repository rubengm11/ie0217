#include "funciones.hpp"
#include <string>

void mostrarMenu(){
    std::cout << "\nMenu\n";
    std::cout << "\n1. Agregar\n";
    std::cout << "\n2. Listar\n";
    std::cout << "\n3. Eliminar\n";
    std::cout << "\n4. Salir \n";

};


void procesarOpcion(Empleado empleados[], int& numEmpleados){
    int opcion;
    std::cout << "\n Ingrese una opcion: ";
    std::cin >> opcion;

    switch(opcion){
        case 1: 
            agregarEmpleado(empleados, numEmpleados);
            break;

        case 2: 
            listarEmpleados(empleados, numEmpleados);
            break;

        case 3:
            eliminarEmpleado(empleados, numEmpleados);
            break;

        case 4:
            std::cout << "Saliendo del programa \n";
            exit(0);

        default:
            std::cout << "\n Opcion invalida. \n";



    }
}

void agregarEmpleado(Empleado empleados[], int& numEmpleados){
    if (numEmpleados< MAX_EMPLEADOS){
        Empleado nuevoEmpleado;
        nuevoEmpleado.id = numEmpleados + 1;

        std::cout << "Ingrese el nombre: \n";
        std::cin >> nuevoEmpleado.nombre;

        std::cout << "Ingrese el salario: \n";
        std::cin >> nuevoEmpleado.salario;

        empleados[numEmpleados++] = nuevoEmpleado;
        std::cout << "Empleado agregado con exito \n";

    } else {
        std::cout << "Max Empleados alcanzado \n";


    }
}

void listarEmpleados(const Empleado empleados[], int& numEmpleados){
    std::cout << "Lista de empleados \n";

    for (int i = 0; i < numEmpleados; ++i ){
        std::cout << "ID: " << empleados[i].id << ", Nombre: " << empleados[i].nombre << ", Salario: " << empleados[i].salario << "\n"; ///// Aqui faltan cosa
    }




}

void eliminarEmpleado(Empleado empleados[], int& numEmpleados){
    int idEliminar;

    std::cout << "Ingrese el ID: \n";
    std::cin >> idEliminar;

    for (int i=0; i < numEmpleados; ++i){

        if (empleados[i].id == idEliminar){
            for (int j = i; j < numEmpleados - 1; ++j){
                empleados[j] = empleados[j+1];

            }
            --numEmpleados;
            std::cout << "Empleado eliminado con exito \n";
            return;
        }
    }





}