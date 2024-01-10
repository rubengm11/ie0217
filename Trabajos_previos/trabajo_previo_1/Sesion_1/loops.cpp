#include <iostream>
#include <string>
using namespace std;


int main() {
    // for
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
        if (i == 3) {
            break;
        }
    }



    cout << "\n";
    // for con array
    int num_array[] = {1, 2, 3, 4, 5, 6, 7};
    for (int n : num_array) {
        cout << n << " ";
    }

    cout << "\n";

    // while
    int i = 1;
    while (i <= 25 ) {
        if (i <= 15) {
            ++i;
            continue;
        }
        cout << i << " ";
        ++i;
    }




    cout << "\n";
    return 0;
}