// 2019-08
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

extern int errno;

int main() {
    // pointer to file
    FILE *file;
    // error
    int errnum;
    // open file that does not exist
    file = fopen("file_does_not_exist", "rb"); // error returns -1 or NULL
    if (file == NULL) {
        // store error code
        errnum = errno;
        
        // print error code
        fprintf(stderr, "error code: %d\n", errno);
        // error code: 2

        // perror to print string representation of error code
        perror("");
        // No such file or directory

        // strerror to print pointer to string representation of error code
        fprintf(stderr, "error opening file: %s\n", strerror(errnum));
        // error opening file: No such file or directory
    } else {
        fclose(file);
    }

    // exit codes
    if (1 == 0) {
        // exit as failure (since something must be wrong?)
        exit(EXIT_FAILURE);
    } else {
        exit(EXIT_SUCCESS);
    }
}