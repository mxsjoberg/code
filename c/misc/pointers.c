#include <stdio.h>
#include <stddef.h>

int main() {
    int num = 5;
    int *ip = NULL; // null pointer

    printf("%p\n", ip); // 0x0 (nil)

    // point to address of num
    ip = &num;

    printf("%p\n", &num); // 0x7ffdb78c2664
    printf("%p\n", ip); // 0x7ffdb78c2664

    // dereference (get value at address)
    printf("%d\n", *ip); // 5
}
