// OUTSIDE SCOPE: global
// variable declaration
extern int x;
extern char y[6];
extern float z;             // 4 bytes
extern double a;            // 8 bytes

// INSIDE SCOPE: local
// variable definition
int x;

// variable initialisation
x = 6;

// variable definition and initialisation
char y[] = "String";
float z = 1.05;
double a = 12.5;

// multiple variable definition
int c, d;

// multiple variable initialisation
c = d = 6;                  // 6, 6

// multiple variable definition and initialisation
int c = 6, d = 6;

// type modifiers
unsigned int unint;         // 4 bytes, 0 to 4294967295
signed int siint;           // 4 bytes, -2147483648 to 2147483647
short int sint;             // 2 bytes, -32768 to 32767
long int lint;              // 8 bytes, -2147483648 to 2147483647
long long int llint;        // 8 bytes, -(2^63) to (2^63)-1

// storage classes
register int rint;          // make it possible to store local variable in register (instead of RAM)
static int stint;           // keep local variable in existence during execution
extern int eint;            // global variable visible to all program files
