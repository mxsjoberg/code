#include <stdio.h>
#include <stdarg.h>

// declare function (normally in header file)
double average(int n, ...);
// define function
double average(int n, ...) {
    va_list valist; /* stdarg.h */
    // return value
    double sum = 0.0;
    // init valist for n arguments
    va_start(valist, n);
    // access arguments
    for (int i=0; i<n; i++) {
        sum += va_arg(valist, int);
    }
    // free memory
    va_end(valist);
    // success
    return sum / n;
}

int main() {
    printf("average of {1,2,3,4,5}: %f\n", average(5, 1, 2, 3, 4, 5));
    // average of {1,2,3,4,5}: 3.000000
}