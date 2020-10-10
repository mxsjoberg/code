#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>
#include <errno.h>
#include <stdarg.h>

int main(int argc, char *argv[]) {
    printf("Running: %s\n", argv[0]);

    if (argc > 1) {
        printf("%s\n", "Arguments: ");
        
        int i;
        for (i = 1; i < argc; i++) {
            printf("\t%s\n", argv[i]);
        }
    }

    // do something
    
    return 0;
}