#include <errno.h>

// OUTSIDE SCOPE: define error variable
extern int errno;

// INSIDE SCOPE: handle error
FILE *file;

int errnum;
file = fopen("file.txt", "rb");

// error returns -1 or NULL
if (file == NULL) {
    // error code is stored in errno
    errnum = errno;

    // print error code
    fprintf(stderr, "Error code: %d\n", errno);

    // perror: print string representation of error code
    perror("Error as printed by perror");

    // strerror: print pointer to string representation of error code
    fprintf(stderr, "Error opening file: %s\n", strerror(errnum));
} else {
    fclose(file);
}

// EXAMPLE: divide by zero
int dividend = 10;
int divisor = 2;
int quotient;

// check if divisor is zero
if (divisor == 0) {
    fprintf(stderr, "%s\n", "Division by zero, exiting...");
    
    // exit as failure
    exit(EXIT_FAILURE);
}

quotient = dividend / divisor;
fprintf(stderr, "Quotient: %d\n", quotient);
// 5

// exit as success
exit(EXIT_SUCCESS);