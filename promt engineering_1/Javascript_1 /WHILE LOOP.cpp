WHILE LOOP 
#include <iostream>
using namespace std;

int main() {
    int count = 0;  // Initialization

    while (count < 5) {  // Condition to check
        cout << "Count is: " << count << endl;  // Code to execute
        count++;  // Increment to avoid an infinite loop
    }

    return 0;
}

FOR LOOP 
# Looping over a range of numbers
for i in range(5):  # range(5) generates [0, 1, 2, 3, 4]
    print("i is:", i)
