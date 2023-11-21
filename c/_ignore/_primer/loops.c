// 2019-08
#include <stdio.h>

int main() {
    for (int i=0; i<5; i++) {
        printf("%d ", i);
    }
    // 0 1 2 3 4

    // nested
    for (int i=0; i<2; i++) {
        for (int j=0; j<2; j++) {
            printf("(%d,%d)\n", i, j);
        }
    }
    // (0,0)
    // (0,1)
    // (1,0)
    // (1,1)

    // iterate an array of ints
    // note first number is length of array
    int numbers[6] = { 6, 1, 2, 3, 4, 5 };
    for (int i=1; i<numbers[0]; i++) {
        printf("%d ", numbers[i]);
    }
    // 1 2 3 4 5

    // iterate an array of ints without knowing length
    int items[] = { 1, 2, 3, 4, 5 };
    for (int i = 0; i < (sizeof(items) / sizeof(items[0])); i++) {
        printf("%d ", items[i]);
    }
    // 1 2 3 4 5

    // while
    int n = 0;
    while (n < 5) {
        printf("%d ", n);
        // increment
        n++;
    }
    // 0 1 2 3 4

    // do-while
    n = 0;
    do {
        printf("%d ", n);
        // increment
        n++;
    } while (n < 5);
    // 0 1 2 3 4
}