#include <iostream>

// define namespace
namespace my_functions {
    void function() {
        std::cout << "called: my_functions::function" << std::endl;
    }
}

int main() {
    my_functions::function(); // called: my_functions::function
}
