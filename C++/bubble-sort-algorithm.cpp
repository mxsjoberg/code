// 2019-08
#include <iostream>

#define PRINT(arr) \
    for (int number : numbers) { std::cout << number << std::endl; }

int main() {
    int numbers[] = { 14, 33, 27, 35, 10 };
    // print unsorted array
    PRINT(numbers)
    // 14
    // 33
    // 27
    // 35
    // 10

    // bubble sort
    for (int i = 0; i < sizeof(numbers) / sizeof(numbers[0]); i++) {
        for (int j = 0; j < sizeof(numbers) / sizeof(numbers[0]); j++) {
            if (numbers[j] > numbers[j + 1]) {
                int temp = numbers[j];
                // swap positions
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }
    PRINT(numbers)
    // 10
    // 14
    // 27
    // 33
    // 35
}