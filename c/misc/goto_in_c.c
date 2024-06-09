
#include <stdio.h>

#define A 1
#define B 0
#define C 0

int main() {
    // fail switch
    if (!A) {
        goto exit;
    }
    if (!B) {
        goto restart_B;
    }
    if (!C) {
        goto restart_C;
    }
    // no fails
    return 0;

restart_B:
    printf("%s\n", "restarting B");

restart_C:
    printf("%s\n", "restarting C");

exit:
    printf("%s\n", "exiting");

    // some fails
    return -1;
}