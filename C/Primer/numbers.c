// 2020-11
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    // expressions
    printf("%d\n",
        12 + 2 * (40 / 4) + 10
    );
    // 42
    
    // built-ins
    printf("%f\n",
        pow(10, 2) /* math.h */
    );
    // 100.000000
    
    // floating-point conversion
    printf("%f\n",
        12.0 + (10 + 20)
    );
    // 42.000000
    
    // promote char to int
    printf("%d\n",
        '*'
    );
    // 42
    
    // type casting
    printf("%f\n",
        (double) 42
    );
    // 42.000000
    
    // integer division
    printf("%d\n",
        42 / 40
    );
    // 1
    
    // integer modulo (remainder)
    printf("%d\n",
        42 % 40
    );
    // 2
    
    // floating-point modulo
    printf("%f\n",
        fmod(42.5, 40.0)
    );
    // 2.500000
    
    // absolute value
    printf("%d\n",
        abs(-42)
    );
    // 42
    
    // rounding value
    printf("%f\n",
        round(42.42)
    );
    // 42.000000
    
    // increment and decrement
    int answer = 41;
    
    answer++;
    printf("%d\n", answer);
    // 42

    answer--;
    printf("%d\n", answer);
    // 41
}