// 2019-08
#include <stdio.h>

// filename.h
// extern makes variable global (normally declared in header file)
extern const int global_num;

// #include "filename.h"

const int global_num = 42;
char ch[255]; // array of chars is string
float x;
double y; // double size of float

int main() {
    printf("%d\n", global_num);
    // 42

    printf("%lu\n", sizeof(x));
    // 4
    printf("%lu\n", sizeof(y));
    // 8

    char ch[] = "this is some text";

    x = y = 1.0;
    printf("%f, %f\n", x, y);
    // 1.000000, 1.000000
}