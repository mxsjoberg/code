// 2019-08
#include <stdio.h>
#include <string.h>

// structures hold data of different types
typedef struct {
    char chars[255];
    int numbers[10];
    double value;
} Element;

// declare function with struct as argument
void function(Element element);

int main() {
    // declare struct type
    Element element;

    strcpy(element.chars, "this is my first element");
    element.numbers[0] = 1;
    element.numbers[2] = 2;
    element.value = 3.14;

    printf("%s\n", element.chars);
    // this is my first element
    printf("%i\n", element.numbers[2]);
    // 2
    printf("%f\n", element.value);
    // 3.140000

    // specify number of bits (bit fields)
    struct {
        unsigned int x;
        unsigned int y;
    } bigger;
    struct {
        unsigned int x : 1;
        unsigned int y : 1;
    } smaller;

    printf("%lu\n", sizeof(bigger));
    // 8
    printf("%lu\n", sizeof(smaller));
    // 4
}