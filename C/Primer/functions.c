// declare function
// NOTE: needs to be BEFORE main() when functions are DEFINED AFTER main()
int function(int arg);

// define function
int function(int arg) {
    // do something
    return 0;
}

// EXAMPLE: power function
// declare function
int power(int base, int x);

// main() function
int main(void) {
    // call function
    power(2, 3)
    // 8

    return 0;
}

// define function
int power(int base, int x) {
    /* multiply base with itself x times */

    int result = 1;

    int i;
    for (i = 0; i < x; i++) {
        result = result * base;
    }

    return result;
}

// END EXAMPLE

// variable arguments
#include <stdarg.h>

// OUTSIDE SCOPE: define function with variable arguments
double average(int n, ...) {
    // require stdarg.h
    va_list valist;

    double sum = 0.0;
    int i;

    // initialise valist for n arguments
    va_start(valist, n);

    // access arguments assigned to valist
    for (i = 0; i < n; i++) {
        sum += va_arg(valist, int);
    }

    // clean memory reserved for valist
    va_end(valist);

    return sum / n;
}

// INSIDE SCOPE: use function
printf("Average of 2, 3, 4, 5: %f\n", average(2, 3, 4, 5));
// Average of 2, 3, 4, 5: 3.500000