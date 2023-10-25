// 2019-08
#import <stdio.h>
#import <stddef.h>

main() {
   printf("%s\n", __FILE__);
   // filename.c
   printf("%s\n", __DATE__);
   // Aug 21 2019
   printf("%s\n", __TIME__);
   // 01:22:18
   printf("%d\n", __LINE__);
   // 12
   printf("%d\n", __STDC__);
   // 1

   // stringify error messages
   #define  error_message(error) \
      printf("error: " #error "\n")

   error_message("This is an error.");
   // error: "This is an error."

   // if not defined
   #if !defined (MESSAGE)
      #define MESSAGE "This is the message if not already defined."
   #endif

   printf("%s\n", MESSAGE);
   // This is the message if not already defined.

   // parameterized macros
   #define square(x) ((x) * (x))
   #define MAX(a,b) ((a) > (b) ? (a) : (b))

   printf("%d\n", square(2));
   // 4
   printf("%d\n", MAX(4,5));
   // 5
}
