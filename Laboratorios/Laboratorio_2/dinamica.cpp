#include <iostream>
using namespace std;


/*.data section*/
int variableGlobal = 10;

/*.text section*/
void funcionGblobal(){
    /*.data */
    static int variableLocalEstatica = 5;

    /* stack sction*/
    int variableLocal = 20;

    cout << "Variable global: " << variableGlobal<< endl;
    cout << "Variable local estatica: " << variableLocalEstatica << endl;
    cout << "Variable local: " << variableLocal << endl;

}

int main(){
    /*stack*/
    int variableLocalMain = 15;

    funcionGblobal();

    cout << "variable local en main: " << variableLocalMain << endl;
    /*heap section*/
    int *variableDinamica = new int;

    *variableDinamica = 25;

    cout << "Variable dinamica: " << *variableDinamica << endl;

    delete variableDinamica;


    return 0;
}