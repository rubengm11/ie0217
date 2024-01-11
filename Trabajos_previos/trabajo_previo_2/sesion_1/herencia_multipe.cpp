#include <iostream>
using namespace std;

// definicion de la clase Animal
class Animal {
public:
    // Metodo que muestra un mensaje
    void info() {
        cout << "I am an animal." << endl;
    }
};

// Definicion de la clase Dog que hereda de Animal
class Dog : public Animal {
public:
    // Metodo bark que muestra un mensaje
    void bark() {
        cout << "I am a Dog. Woof woof." << endl;
    }
};

// Definicion de la clase Cat que hereda de Animal
class Cat : public Animal {
public:
    // Metodo meow que muestra un mensaje
    void meow() {
        cout << "I am a Cat. Meow." << endl;
    }
};

int main() {
    Dog dog1;
    cout << "Dog Class: " << endl;

    dog1.info();  

    dog1.bark();


    Cat cat1;
    cout << "\nCat Class: " << endl;
    

    cat1.info();  
    cat1.meow();

    return 0;
}