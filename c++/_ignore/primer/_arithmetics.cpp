10 + 20                         // 30
20 - 10                         // 10
10 * 20                         // 200
20 / 10                         // 2

// floating point conversion
10.0 + (10 + 20)                // 40

// NOTE: char is promoted to int value
'c' + 10
// 109 (ascii value of c is 99)

// floating point conversion using type casting
(double) 10.0 + (10 + 20)       // 40
(double) 20.0 - (10 + 10)       // 0
(double) 10.0 * (10 * 2)        // 200

// common division error
30 / 20                         // 1
(double) 30 / 20                // 1.5

// integer divison, quotient
20 / 20                         // 1
30 / 20                         // 1
40 / 20                         // 2

// modulo, remainder
10 % 20                         // 10

// increment and decrement
int a = 10;

a++                             // 11
a--                             // 9

// max and min
max(10, 20)                     // 20
min(10, 20)                     // 10

// include cmath for more
#include <cmath>

// power
pow(10, 2)                      // 100

// module, remainder on floating point
fmod(12.5, 10.0)                // 2.5

// absolute value
abs(-20)                        // 20

// rounding
round(2.945)                    // 3
round(2.495)                    // 2

// NOTE: no built-ins for round to decimal places

// bitwise operators
int A = 60;                     // 0011 1100
int B = 13;                     // 0000 1101

A & B                           // 12, 0000 1100
A | B                           // 61, 0011 1101
A ^ B                           // 49, 0011 0001
~A                              // -61, 1100 0011
A << 2                          // 240, 1111 0000
A >> 2                          // 15, 0000 1111