#include <iostream>
using namespace std;

int main() {
    // try-catch
    try {
        // do something

        throw 0;
    } catch (int error) {
        // do something
        
        cout << "Error: " << error << endl;
        // Error: 0
    }
    // default exception
    try {
        if (!true) {
            // do something
        } else {
            // error code
            throw 0;
        }
    } catch (...) {
        cout << "Default exception." << endl;
        // Default exception.
    }
    return 0;
}