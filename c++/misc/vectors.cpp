#include <iostream>
#include <vector>

int main() {
    // vector of ints
    std::vector<int> vec;
    // size
    std::cout << vec.size() << std::endl; // 0

    // push values
    for (int i = 1; i <= 5; i++) {
        vec.push_back(i);
    }
    std::cout << vec.size() << std::endl; // 5

    // access values
    std::cout << vec[3] << std::endl; // 4
}
