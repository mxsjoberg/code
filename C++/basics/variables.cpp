// OUTSIDE SCOPE: variable declaration
// NOTE: set extern to make visible in all files
int x;                          // integer, 4 bytes
char c;                         // character, 1 byte
char c_arr[6];                  // character array of size 6 (string)
float z;                        // floating point, 4 bytes
double z_double;                // floating point, 8 bytes
bool t;                         // boolean (true or false), 1 byte

// INSIDE SCOPE: variable definition
int x;

// variable initialisation
x = 6;                          // 6
c = 65;                         // A (ASCII)
z = 1.05;                       // 1.05
t = true;                       // 1

// or scientific notation
z_double = 10e4;                // 100000

// variable definition and initialisation
char c = 'S';

// character array with undefined size
char c_arr[] = "String";

// multiple variable definition
int x, y;

// multiple variable initialisation
x = y = 6;                      // 6, 6

// multiple variable definition and initialisation
int x = 6, y = 6;

// typedef to create alias
typedef int myint;
myint x = 10, y = 5, z = -20;

cout << x << ", " << y << ", " << z << endl;
// 10, 5, -20

// type modifiers
unsigned int unsigned_int;      // 4 bytes, 0 to 4294967295
signed int signed_int;          // 4 bytes, -2147483648 to 2147483647
short int short_int;            // 2 bytes, -32768 to 32767
long int long_int;              // 8 bytes, -2147483648 to 2147483647
long long int long_long_int;    // 8 bytes, -(2^63) to (2^63)-1

// storage classes
register int register_int;      // make it possible to store local variable in register (instead of RAM)
static int static_int;          // keep local variable in existence during execution
extern int extern_int;          // global variable visible to all program files
