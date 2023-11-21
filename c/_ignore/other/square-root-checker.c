#include <stdio.h>
#include <math.h>

int main(void) {
    int base;

    scanf("%d", &base);
    if (base > 1) {
        printf("%.8f\n", sqrt(base));

    } else {
        printf("%s\n", "Invalid base.");
    }
}

// ./main
// 2
// 1.41421356