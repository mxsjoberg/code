// 2019-08
#import <stdio.h>
#import <stddef.h>

main() {
    int num = 5;
    // null pointer
    int *ip = NULL;

    printf("%p\n", ip);
    // 0x0 (nil)

    // point to address of num
    ip = &num;

    printf("%p\n", &num);
    // 0x7ffdb78c2664
    printf("%p\n", ip);
    // 0x7ffdb78c2664

    // dereference (get value at address)
    printf("%d\n", *ip);
    // 5
}
