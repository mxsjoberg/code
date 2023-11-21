// 2019-08
#include <stdio.h>

// declare recursive function
int factorial(int i);
// define recursive function
int factorial(int i) {
    if (i <= 1) {
        return 1;
    }
    return i * factorial(i - 1);
}

int main() {
    printf("factorial of 12 is %d\n", factorial(12));
    // factorial of 12 is 479001600
}
