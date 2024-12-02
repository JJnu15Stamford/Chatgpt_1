CREATE A FUNCTION THAT RETURNS VALUES 
#include <iostream>
#include <utility>  // For std::pair
using namespace std;

// Function that returns a pair of integers (sum and difference)
pair<int, int> calculate(int a, int b) {
    int sum = a + b;
    int difference = a - b;
    return make_pair(sum, difference);
}

int main() {
    pair<int, int> result = calculate(10, 5);
    cout << "Sum: " << result.first << endl;         // Output: Sum: 15
    cout << "Difference: " << result.second << endl; // Output: Difference: 5
    return 0;
}
