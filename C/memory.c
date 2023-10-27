// 2019-08
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
    - allocate an array of n elements of size s
        void *calloc(int n, int s);

    - release a block of memory at address
        void free(void *address);

    - allocate an array of b bytes (uninitialised)
        void *malloc(int b);

    - re-allocate memory at address (extending to new size s)
        void *realloc(void *address, int s);
*/

// https://www.programiz.com/c-programming/online-compiler/

int main() {
    char name[36];
    char *description; // pointer to char without size limit

    // copy string of 35 bytes into buffer of 36 bytes
    strcpy(name, "Wolfeschlegelsteinhausenbergerdorff");

    // allocate memory dynamically (can result in fragmented memory)
    // description = malloc(10 * sizeof(char));
    // strcpy(description, "A too long text to store in only 10 bytes...");
    // printf("%s\n", description);
    // malloc(): corrupted top size
    // Aborted

    description = malloc(100 * sizeof(char));
    strcpy(description, "A too long text to store in only 10 bytes...");
    printf("%s\n", description);
    // A too long text to store in only 10 bytes...

    // free memory
    free(description);
}