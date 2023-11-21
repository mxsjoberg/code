// 2019-08
#include <iostream>
#include <string>
#include <ctype.h>

const std::string text = "hello c++";

int main() {
    std::cout << text[0] << text[3] << std::endl;
    // hl

    std::cout << isdigit('4') << std::endl;
    // 1
    std::cout << isupper(text[0]) << std::endl;
    // 0
    std::cout << islower(text[0]) << std::endl;
    // 1

    std::cout << text.size() << std::endl;
    // 9
    std::cout << text.length() << std::endl;
    // 9

    std::cout << text + " and 42" << std::endl;
    // hello c++ and 42
}