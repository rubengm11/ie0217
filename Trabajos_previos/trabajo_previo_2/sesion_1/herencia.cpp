#include <iostream>
using namespace std;

// Definicion de la clase Animal
class Animal {
public:
    // Metodo para comer
    void eat() {
        cout << "I can eat!" << endl;
    }

    // Metodo para dormir
    void sleep() {
        cout << "I can sleep!" << endl;
    }
};

// Metodo de la clase Dog que hereda de la clase Animal
class Dog : public Animal {
public:
    // Metodo para ladrar
    void bark() {
        cout << "I can bark! Woof woof!!" << endl;
    }
};


int main() {

    Dog dog1;

    // Llama a los metodos eat y sleep de la clase Animal a traves del objeto dog
    dog1.eat();
    dog1.sleep();

    // Llama al metodo bark de la clase Dog
    dog1.bark();

    return 0;
}
