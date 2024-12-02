CREATE A FUNCTION THAT ACCEPTS AN ARGUMENT 
#include <iostream>
using namespace std;

// Function definition
int square(int number) {
    return number * number;
}

int main() {
    int result = square(5);  // Call the function with an argument
    cout << "The square of 5 is: " << result << endl;  // Output: The square of 5 is: 25
    return 0;
}
