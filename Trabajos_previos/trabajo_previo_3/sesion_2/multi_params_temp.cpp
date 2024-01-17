#include <iostream>
using namespace std;

template<class T, class U, class V = char>
class ClassTemplate{
    private:
        T var1;
        U var2;
        V var3;

    public:
        ClassTemplate(T v1. U v2, V v3) : var1(v1), var2(v2), var3(v3) {}

        void printVar(){
            cout << "Var1 = " << var1 << endl;
            cout << "Var2 = " << var2 << endl;
            cout << "Var3 = " << var3 << endl;
        }
};

int main(){
    ClassTemplate<int, double> obj1(7, 7.7,'c');
    cout << "obj1 values: " << endl;

    obj1.printVar();

    ClassTemplate<double, char, bool> obj2(8.8, 'a', false);
     cout << "obj2 values: " << endl;
     obj2.printVar();


    return 0;
}