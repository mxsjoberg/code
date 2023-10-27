// declare function: name, return, and parameters
// NOTE: needs to be before main() when functions are defined after main()
void function();
// NOTE: void is no return

// define function: function body
void function() {
    // do something
}

// default arguments
int function(int i = 1) {
    return i;
}

/* EXAMPLE: power function ---- */
/* ---------------------------- */
int power(int base, int x);

int main() {
    // call function
    power(2, 3)
    // 8

    return 0;
}

int power(int base, int x) {
    /* multiply base with itself x times */

    int result = 1;
    for (int i = 0; i < x; i++) {
        result = result * base;
    }

    return result;
}
/* ---------------------------- */

// function overloading: same name but different types
int function(int x);
float function(float x);
double function(double x, double y);