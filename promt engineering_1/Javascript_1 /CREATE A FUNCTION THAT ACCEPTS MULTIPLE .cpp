CREATE A FUNCTION THAT ACCEPTS MULTIPLE ARGUMENTS
#include <iostream>
#include <cstdarg>
using namespace std;

// Function to multiply a variable number of arguments
int multiplyNumbers(int numArgs, ...) {
    int result = 1;
    va_list args;
    va_start(args, numArgs);

    for (int i = 0; i < numArgs; i++) {
        result *= va_arg(args, int);
    }

    va_end(args);
    return result;
}

int main() {
    int result = multiplyNumbers(4, 2, 3, 4, 5);
    cout << "The product is: " << result << endl;  // Output: The product is: 120
    return 0;
}
