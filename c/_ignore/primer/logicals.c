// 2019-08
#include <stdio.h>
#include <stdbool.h>

int main() {
    const bool YES = true;
    const bool NO = false;

    printf("%d\n", YES || NO);
    // 1
    printf("%d\n", YES && (YES && NO));
    // 0
    printf("%d\n", !YES);
    // 0
    printf("%d\n", !(!YES));
    // 1

    // equality
    printf("%d\n", 1 == 1);
    // 1
    printf("%d\n", 1 != 1);
    // 0
    printf("%d\n", 1 > 0);
    // 1
    printf("%d\n", 1 < 0);
    // 0
    printf("%d\n", 1 >= 1);
    // 1
    printf("%d\n", 1 <= 0);
    // 0
}