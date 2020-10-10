#include <ctype.h>
#include <string.h>

// indexing
char string[] = "proton";

string[0]           // p
string[3]           // t

// built-in operators
char a = 'a';
char b = 'B';

toupper(a)              // A
tolower(b)              // b

// conditionals
isdigit(a)              // 0 (false)
islower(a)              // 1 (true)
isupper(a)              // 0 (false)

// comparing strings
char first_string[] = "This is a string.";
char second_string[] = "This is a string.";
char third_String[] = "This is another string.";

strcmp(first_string, second_string)         // 0 (equal)
strcmp(first_string, third_String)          // not equal

strlen(first_string)                        // 17

// reverse string
// NOTE: no built in function
char* str_reverse(char *str) {
    char tmp;
    size_t n = 0;
    size_t len = strlen(str);

    for (n = 0; n < (len / 2); n++) {
        tmp = str[n];
        str[n] = str[len - n - 1];
        str[len - n - 1] = tmp;
    }

    return str;
}
str_reverse("test")
// tset