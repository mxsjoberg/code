#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> numbers = { 1, 2, 3, 4, 5 };
    // multiply each element in numbers using for_each
    std::for_each(numbers.begin(), numbers.end(), [](int &number) {
        number *= 2;
    });
    // for_each
    std::for_each(numbers.begin(), numbers.end(), [](int number) {
        std::cout << number << std::endl;
    });
    // 2 4 6 8 10
}
