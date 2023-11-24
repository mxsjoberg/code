#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> numbers = { 1, 2, 3, 4, 5 };
    // binary_search
    bool found = std::binary_search(numbers.begin(), numbers.end(), 4);
    if (found) {
        std::cout << "found value" << std::endl;
    } else {
        std::cout << "not found" << std::endl;
    }
    // found value
}
