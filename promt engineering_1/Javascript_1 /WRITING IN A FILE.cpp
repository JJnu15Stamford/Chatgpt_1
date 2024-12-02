WRITING IN A FILE 
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Writing to a file (overwriting the content)
    ofstream outputFile("output.txt");
    if (outputFile.is_open()) {
        outputFile << "Hello, this is a test message.\n";
        outputFile << "Writing data to a file in C++ is simple!";
        outputFile.close();
        cout << "File written successfully!" << endl;
    } else {
        cerr << "Error opening file for writing." << endl;
    }

    // Appending to a file
    ofstream appendFile("output.txt", ios::app);
    if (appendFile.is_open()) {
        appendFile << "\nAppending a new line to the file.";
        appendFile.close();
        cout << "Content appended successfully!" << endl;
    } else {
        cerr << "Error opening file for appending." << endl;
    }

    return 0;
}
