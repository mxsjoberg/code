// 2020-11
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    printf(
        "expression: %d\n",
        12 + 2 * (40 / 4) + 10
    );
    // expression: 42
    
    printf(
        "power: %f\n",
        pow(10, 2) /* math.h */
    );
    // power: 100.000000
    
    printf(
        "floating-point conversion: %f\n",
        12.0 + (10 + 20)
    );
    // floating-point conversion: 42.000000
    
    printf(
        "promote char to int: %d\n",
        '*'
    );
    // promote char to int: 42
    
    printf(
        "type casting: %f\n",
        (double) 42
    );
    // type casting: 42.000000
    
    printf(
        "integer division: %d\n",
        42 / 40
    );
    // integer division: 1
    
    printf(
        "integer modulo (remainder): %d\n",
        42 % 40
    );
    // integer modulo (remainder): 2
    
    printf(
        "floating-point modulo: %f\n",
        fmod(42.5, 40.0)
    );
    // floating-point modulo: 2.500000
    
    printf(
        "absolute value: %d\n",
        abs(-42)
    );
    // absolute value: 42
    
    printf(
        "rounding value: %f\n",
        round(42.42)
    );
    // rounding value: 42.000000
    
    int answer = 41;
    
    answer++;
    printf("increment: %d\n", answer);
    // increment: 42

    answer--;
    printf("decrement: %d\n", answer);
    // decrement: 41
}