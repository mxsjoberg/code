#include <stdio.h>
#include <stddef.h>

// stringify error messages
#define  error_message(error) \
   printf("error: " #error "\n")

// if not defined (used in header files to avoid multiple inclusion)
#ifndef MESSAGE
#define MESSAGE "This is the message if not already defined."
#endif

// parameterized macros
#define square(x) ((x) * (x))
#define max(x, y) ((x) > (y) ? (x) : (y))

int main() {
   printf("%s\n", __FILE__); // macros.c
   printf("%s\n", __DATE__); // Aug 21 2019
   printf("%s\n", __TIME__); // 01:22:18
   printf("%d\n", __LINE__); // 12
   printf("%d\n", __STDC__); // 1

   error_message("This is an error.");
   // error: "This is an error."

   printf("%s\n", MESSAGE);
   // This is the message if not already defined.

   printf("%d\n", square(2)); // 4
   printf("%d\n", max(4,5)); // 5
}
