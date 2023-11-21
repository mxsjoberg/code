// 2019-08
#include <stdio.h>
#include <string.h>

// union store different types of data in the same memory location
// note that only one member can store data at a time
union Data {
    int number;
    float value;
    char str[20];
} data;

int main() {
    union Data data;

    // size of union is size of largest member
    printf("%lu\n", sizeof(data));
    // 20

    // assign values
    data.number = 42;
    printf("%d\n", data.number);
    // 42

    // subsequent assignments overwrite previous values
    data.value = 12.5;
    printf("%f\n", data.value);
    // 12.500000
    
    printf("%d\n", data.number);
    // 1095237632 (number is overwritten)
    
    // strings are copied with strcpy
    strcpy(data.str, "this is some text");
    printf("%s\n", data.str);
    // this is some text

    printf("%d\n", data.number);
    // 1936287860 (number is overwritten)
    printf("%f\n", data.value);
    // 18492488542240085843427383574528.000000 (value is overwritten)
}