// arrays are mutable
// NOTE: undefined size will set size to number of elements in array
double numbers[] = { 200.0, -2.2, 1.0, 0.0 };

// array with strings
#define MAX_STRING_SIZE 40
char char_array[][MAX_STRING_SIZE] = { "REMOVE", "RANDOM" };

// or with string class
#include <string>
string names[10] = { "Adam", "John", "Michael", "Susan" };

// indexing
numbers[0]                      // 200
char_array[1]                   // RANDOM
names[2]                        // Michael

// assignment
numbers[0] = 50.0;
numbers[0]                      // 50

// multi-dimensional array
int array_multi[2][10] = {
    { 0, 1, 2, 3, 4 },
    { 5, 6, 7, 8, 9 }
};
array_multi[1][2]               // 7

// NOTE: no built-ins for length

// calculate length based on type
int length = sizeof(numbers) / sizeof(double);
length
// 4