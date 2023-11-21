// 2019-08
#include <iostream>
#include <string>

int main() {
    std::string input;

    // read from input stream
    // std::cin >> input;
    // std::cout << input << std::endl;
    // > hello c++
    // hello

    // read using getline to get line
    getline(std::cin, input);
    std::cout << input << std::endl;
    // > hello c++
    // hello c++
}