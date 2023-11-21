// OUTSIDE SCOPE: define macro as constant
#define LENGTH 10
#define WIDTH 5

// INSIDE SCOPE: use constants as substitute for assigned value
LENGTH                  // 10
WIDTH                   // 5
LENGTH * WIDTH;         // 50

// constant definition and initialisation
// NOTE: constants are immutable
const int const_int = 20;

// EXAMPLE: re-assign to constant
const int const_int = 20;
const_int = -1;
// error: cannot assign to variable 'const_int' with const-qualified type 'const int'