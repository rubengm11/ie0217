#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector <string> languages = {"Python", "C++", "Java"};
    vector<string>::iterator itr;

    for (itr = languages.begin(); itr !=languages.end(); itr++) {
        cout << *itr << ", ";
    }
    cout << endl;

    return 0;

}