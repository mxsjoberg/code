// 2019-08
#include <iostream>

// define namespace
namespace env {
    void first() {
        std::cout << "called: first() in env" << std::endl;
    }
    void second() {
        std::cout << "called: second() in env" << std::endl;
    }
}

int main() {
    env::first();
    // called: first() in env
    env::second();
    // called: second() in env
}
