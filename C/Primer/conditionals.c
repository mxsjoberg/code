// 2019-08
#include <stdio.h>

#define ANSWER 42

int main() {
    int value = 42;

    if (value < 1) {
        // no
    } else if (value == 1) {
        // no
    } else if (value == ANSWER) {
        // yes!
        printf("%d is the answer: %d\n", value, ANSWER);
    } else {
        // no
    }
    // 42 is the answer: 42

    // single line
    printf("%s\n", (value != ANSWER) ? "no" : "this is the answer");
    // this is the answer
}