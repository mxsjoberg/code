// OUTSIDE SCOPE: define recursive function
void recursive() {
   recursive();
}

// EXAMPLE: factorial

// OUTSIDE SCOPE: define recursive function
unsigned long long int factorial(unsigned int i) {
    if (i <= 1) {
        return 1;
    }
    return i * factorial(i - 1);
}

// INSIDE SCOPE: use recursive function
int i = 12;

printf("Factorial of %d is %llu\n", i, factorial(i));
// Factorial of 12 is 479001600