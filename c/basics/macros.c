printf("%s\n", __FILE__);       // test.c
printf("%s\n", __DATE__);       // Aug 21 2019
printf("%s\n", __TIME__);       // 01:22:18
printf("%d\n", __LINE__);       // 16
printf("%d\n", __STDC__);       // 1

// stringize
// OUTSIDE SCOPE: define macro
#define  error_message(e)  \
   printf("Error: " #e "\n")

// INSIDE SCOPE: use macro
error_message("This is an error.");
// Error: This is an error.

// defined
// OUTSIDE SCOPE: define macro
#if !defined (MESSAGE)
   #define MESSAGE "This is a message."
#endif

// INSIDE SCOPE: use macro
printf("%s\n", MESSAGE);
// This is a message.

// parameterized macros
// OUTSIDE SCOPE: define macro
#define square(x) ((x) * (x))
#define MAX(a,b) ((a) > (b) ? (a) : (b))

printf("%d\n", square(2));                  // 4
printf("%d\n", MAX(4,5));                   // 5