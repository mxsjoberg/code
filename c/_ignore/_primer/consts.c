// 2019-08
#include <stdio.h>

// #define is a preprocessor directive (substitute text, inlining)
#define A 100
#define B 200

int main() {
    // const is an immutable variable
    const int C = 300;
    const int D = 400;

    printf("%d\n", A);
    // 100
    printf("%d\n", B);
    // 200
    printf("%d\n", C);
    // 300
    printf("%d\n", D);
    // 400
}