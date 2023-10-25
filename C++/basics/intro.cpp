/*
    C++ is a general-purpose programming language developed by Bjarne Stroustrup in 1985.

    https://en.wikipedia.org/wiki/C%2B%2B
*/

#include <iostream>
using namespace std;

int main() {
    // do something
    cout << "hello" << " " << "world" << endl;

    return 0;
}

/* 
    command line arguments
    - argc: number of arguments
    - argv: pointer to array with arguments
*/
int main(int argc, char** argv) {
    // print file name
    cout << "Running: " << argv[0] << endl;
    // print arguments
    if (argc > 1) {
        cout << "Arguments: " << endl;
        
        int i;
        for (i = 1; i < argc; i++) {
            cout << argv[i] << endl;
        }
    }
    // do something
    return 0;
}

/* 
    1. compile and run from command-line:
        
        $ g++ <filename>.cpp -o <filename>
        $ ./<filename>

    2. compile and run with makefile:

        main: <filename>.cpp
            g++ -o main <filename>.cpp
*/

// size in memory
int a;
sizeof(a)
// 4

// pointer
&a
// 0x7ffee52776b8

// conditional (ternary operator): if x < 10, return 30, else return 40
int x = 10;
(x < 10) ? 30 : 40
// 40