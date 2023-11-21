// 2019-08
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    // a string is an array of chars
    char string[] = "This is some text";
    printf("%c, %c\n", string[0], string[3]);
    // T, s

    // built-ins
    printf("%c\n", toupper('a'));
    // A
    printf("%c\n", tolower('A'));
    // a
    printf("%d\n", isdigit('5'));
    // 1
    printf("%d\n", islower('a'));
    // 1
    printf("%d\n", isupper('A'));
    // 1

    // comparison (lexicographic order)
    char answer[] = "the answer is 42";
    printf("%d\n", strcmp(answer, "the answer is 42"));
    // 0 (equal)
    printf("%d\n", strcmp(answer, "the answer is 96"));
    // -5 (first argument is smaller than second)

    // length of string
    printf("%lu\n", strlen(answer));
    // 16
}