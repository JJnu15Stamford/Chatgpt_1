READING FROM A FILE 
def main():
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    // Open the file in read mode
    ifstream file("example.txt");

    // Check if the file is open
    if (!file.is_open()) {
        cerr << "Error opening file." << endl;
        return 1; // Exit with an error code
    }

    string line;
    // Read the file line by line
    while (getline(file, line)) {
        cout << line << endl;
    }

    // Close the file
    file.close();
    return 0;
}
