#include <iostream>
#include <vector>

constexpr void print_elements_in_vector(std::vector<int> numbers) {
    for (int number : numbers) {
        std::cout << number << std::endl;
    }
}

int main() {
    std::vector<int> numbers = { 14, 33, 27, 35, 10 };
    // print unsorted
    print_elements_in_vector(numbers); // 14 33 27 35 10

    // bubble sort
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = 0; j < numbers.size() - 1; j++) {
            if (numbers[j] > numbers[j + 1]) {
                int temp = numbers[j];
                // swap positions
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }
    // print sorted
    print_elements_in_vector(numbers); // 10 14 27 33 35
}