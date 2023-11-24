#include <algorithm>
#include <vector>
#include <iostream>

bool twice (int a, int b) { return a * 2 == b; }

int main() {
    std::vector<int> numbers = { 50, 40, 10, 20, 20 };
    // adjacent_find
    auto iter = std::adjacent_find(numbers.begin(), numbers.end(), twice);
    if (iter != numbers.end()) {
        std::cout << *iter << ", " << *(iter + 1) << std::endl;
    } else {
        std::cout << "no adjacent pairs" << std::endl;
    }
    // 10, 20
}
