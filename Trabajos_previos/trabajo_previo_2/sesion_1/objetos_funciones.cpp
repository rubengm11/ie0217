#include <iostream>
using namespace std;

// definicion de la clase Student
class Student {
public:
    double marks;

    // Constructor de la clase Student
    Student(double m) {
        marks = m;
    }
};


void calculeteAverage(Student s1, Student s2) {
    // Calculo del promedio
    double average = (s1.marks + s2.marks) / 2;

    // Muestra el promedio de las calificaciones
    cout << "Average marks = " << average << endl;
}

int main() {
    // Creacion de dos objetos de la clase Student
    Student student1(88.0), student2(56.0);

    // Llama a la funcion para calcular el promedio
    calculeteAverage(student1, student2);

    return 0;
}