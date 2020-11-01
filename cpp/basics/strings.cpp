// string as array of characters
char str[] = "proton";

// or with string class
#include <string>

string string_str = "proton";

// indexing
str[0]                                      // p
str[3]                                      // t

// built-in operators
char(toupper(str[0]))                       // P
char(tolower(str[0]))                       // p

// conditionals
isdigit(str[0]);                            // 0 (false)
islower(str[0]);                            // 1 (true)
isupper(str[0]);                            // 0 (false)

// comparisons
char first_string[] = "This is a string.";
char second_string[] = "This is a string.";
char third_string[] = "This is another string.";
char empty_string[] = "";

strcmp(first_string, second_string);        // 1 (equal)
strcmp(first_string, third_String);         // -78 (not equal)

// length of string
strlen(first_string);
// 17

// or with string class
string_str.size();                          // 6
string_str.length();                        // 6

// copy string
strcpy(empty_string, first_string);
// This is a string.

// or with string class
string empty_str = "";
empty_str = string_str;
// proton

// concatenate string
// NOTE: allocate enought to target string
char str_one[255] = "This is a string.";    // 17 + 1 bytes
char str_two[] = "And this too.";           // 13 + 1 bytes

strcat(str_one, str_two);
// This is a string.And this too.

// or with string class
empty_str = string_str + " " + "neutron";
// proton neutron

// reverse string
// NOTE: no built-ins, include algorithm
#include <algorithm>

reverse(string_str.begin(), string_str.end());
// notorp