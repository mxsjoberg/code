#include <iostream>
#include <vector>
#include <string>
#include <format>

int main() {
    // vector of ints
    std::vector<int> numbers;
    // size
    std::cout << numbers.size() << std::endl; // 0
    // push values
    for (int i = 1; i <= 5; i++) {
        numbers.push_back(i);
    }
    std::cout << numbers.size() << std::endl; // 5
    std::cout << numbers[3] << std::endl; // 4

    // vector of strings
    std::vector<std::string> strings = { "hello", "c++" };
    std::cout << strings[0] << " " << strings[1] << std::endl; // hello c++
}
