ACCESS VALUES FROM A LIST 
#include <iostream>
using namespace std;

int main() {
    // Creating an array
    int myArray[] = {10, 20, 30, 40, 50};
    int arraySize = sizeof(myArray) / sizeof(myArray[0]);

    // Accessing values using indexing
    cout << "First element: " << myArray[0] << endl;  // Output: First element: 10
    cout << "Second element: " << myArray[1] << endl; // Output: Second element: 20
    cout << "Last element: " << myArray[arraySize - 1] << endl; // Output: Last element: 50

    // Accessing a range of elements using a loop
    cout << "First three elements: ";
    for (int i = 0; i < 3; i++) {
        cout << myArray[i] << " ";
    }
    cout << endl;  // Output: First three elements: 10 20 30

    return 0;
}
