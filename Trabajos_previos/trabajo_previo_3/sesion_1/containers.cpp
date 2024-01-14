#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
using namespace std;

int main() {

    // usando vector
    vector<int> numbers = {1, 100, 10, 70, 100};
    cout << "Los numeros son: ";
    for (auto &num: numbers) {
        cout << num << ", ";
    }

    // usando set
    set<int> numbers2 = {1, 100, 10, 70, 100};
    cout << "\n" << "Los numeros son: ";
    for (auto &num: numbers2) {
        cout << num << ", ";
    }
    cout << endl;

    // unordered_set
    unordered_set<int> numbers3 = {1, 100, 10, 70, 100};
    cout << "\n" << "Los numeros son: ";
    for (auto &num: numbers3) {
        cout << num << ", ";
    }
    cout << endl;

    return 0;
}