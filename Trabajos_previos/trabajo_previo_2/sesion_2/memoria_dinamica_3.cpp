#include <iostream>
using namespace std;

class Student {
    private:
        int age;

    public:
        // Se inicializa el valor en 12
        Student() : age(12) {}

        // Se imprime la edad
        void getAge(){
            cout << "Age = " << age << endl;
        }
    
};

int main(){

    // Declaracion dinamica de objeto Student
    Student* ptr = new Student();

    ptr->getAge();

    // Liberar memoria
    delete ptr;

    return 0;
}