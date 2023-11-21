// 2023-10
#include <iostream>

const int numbers[] = { 10, 20, 30, 40, 50 };

int main() {
    for (int i : numbers) {
        std::cout << i << std::endl;
    }
    // 10
    // 20
    // 30
    // 40
    // 50
}