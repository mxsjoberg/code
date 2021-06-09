#define MAX_STRING_SIZE 40

// arrays are mutable
double array_one[] = { 200.0, -2.2, 1.0, 0.0 };
char array_two[][MAX_STRING_SIZE] = { "REMOVE", "RANDOM" };

array_one[0]                    // 200.000000
array_two[1]                    // RANDOM

array_one[0] = 50.0;
array_one[0]                    // 50.000000

// multi-dimensional array
int array_multi[2][10] = {
    { 0, 1, 2, 3, 4 },
    { 5, 6, 7, 8, 9 }
};

array_multi[1][2]
// 7

// calculate length based on type
int length = sizeof(array_one) / sizeof(double);
length
// 4