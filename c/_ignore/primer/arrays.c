// 2019-08
#include <stdio.h>

int main() {
    // array of doubles
    double doubles[] = { 200.0, -2.2, 1.0, 0.0 };
    printf("%f\n", doubles[1]);
    // -2.200000
    
    // arrays are mutable
    doubles[1] = 42;
    printf("%f\n", doubles[1]);
    // 42.000000
    
    // array of arrays of char with max size 10 (strings)
    char strings[][10] = { "first", "second" };
    printf("%s\n", strings[1]);
    // second

    // nd-array of ints
    int matrix[2][10] = {
        { 0, 1, 2, 3, 4 },
        { 5, 6, 7, 8, 9 }
    };
    printf("%d\n", matrix[1][2]);
    // 7

    // calculate length based on type (in bytes)
    printf("%lu\n", sizeof(doubles) / sizeof(double));
    // 4
}
