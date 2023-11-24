// smart pointers handle allocation and deletion of memory

#include <memory>
#include <iostream>
#include <vector>

class MyClass {
    std::unique_ptr<std::vector<int>> data; // unique_ptr is a smart pointer
public:
    MyClass(const int size) { data = std::make_unique<std::vector<int>>(size); } // allocate memory with make_unique
    void print_data() {
        for (auto i : *data) { std::cout << i << std::endl; }
    }
};

void function_using_data() {
    MyClass my_class(5); // lifetime tied to scope
    my_class.print_data();
} // my_class is destroyed here

int main() {
    function_using_data(); // 0 0 0 0 0
}
