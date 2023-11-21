// 2023-10
#include <iostream>

int main() {
    try {
        if (1 == 2) {
            // what?
        } else {
            throw 0;
        }
    } catch (int error) {
        std::cout << "error: " << error << std::endl;
        // error: 0
    }
}