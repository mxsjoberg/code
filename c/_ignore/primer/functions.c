// 2019-08
#include <stdio.h>

// declare function (normally in header file)
int power(int base, int x);
// define function
int power(int base, int x) {
    int result = 1;
    for (int i=0; i<x; i++) {
        result *= base;
    }
    // success
    return result;
}

int main() {
    printf("%d\n", power(2, 8));
    // 256
}
