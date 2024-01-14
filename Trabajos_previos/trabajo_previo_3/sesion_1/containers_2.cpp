#include <iostream>
#include <map>
using namespace std;

int main(){
    map<int, string> student;

    // Se utilizan [] para acceder a los elementos de ese array
    student[1] = "Jacqueline";
    student[2] = "Blake";

    // Se utiliza insert() para agregar elementos.
    student.insert(make_pair(3, "Denise"));
    student.insert(make_pair(4, "Blake"));

    // Se sobreescriben elementos
    student[5] = "Timoteo";
    student[5] = "Aaron";

    for (int i = 1; i<= student.size(); ++i){
        cout << "Student[" << i << "]: " << student[i]<<endl;
    }

    return 0;
}