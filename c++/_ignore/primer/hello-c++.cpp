// 2019-08
#include <iostream>

// int main() {
//     std::cout << "hello c++" << std::endl;
// }
int main(int argc, char** argv) {
    // filename
    std::cout << "filename: " << argv[0] << std::endl;
    // arguments
    if (argc > 1) {
        std::cout << "argv: " << std::endl;
        for (int i = 1; i < argc; i++) {
            std::cout << argv[i] << std::endl;
        }
    }
}

// $ g++ hello-c++.cpp -o _hello ; ./_hello
// filename: ./hello-c++
