#include <iostream>
using namespace std;

// Definicion de la clase Student
class Student {
public:
    double marks1, marks2;
};

// Funcion para crear un objeto de la clase Student
Student createStudent() {
    Student student;

    // Calificaciones 
    student.marks1 = 96.5;
    student.marks2 = 75;

    // Muestra las calificaciones asignadas
    cout << "Marks 1 = " << student.marks1 << endl;
    cout << "Marks 2 = " << student.marks2 << endl;

    // Retorna el objeto Student creado
    return student;
}

int main() {
    Student student1;

    student1 = createStudent();

    return 0;
}