// OUTSIDE SCOPE: global (set extern to make visible in all files)
// variable declaration
int x; 						// integer
char c; 					// character
char carr[6]; 				// character array of size 6 (string)
float z;             		// floating point, 4 bytes
double zz; 					// floating point, 8 bytes
bool t = true; 				// boolean (true or false)

// INSIDE SCOPE: local
// variable definition
int x;

// variable initialisation
x = 6;
z = 1.05;
zz = 12.5;

// variable definition and initialisation
char c = 'S';
char carr[] = "String"; 	// undefined size

// multiple variable definition
int x, y;

// multiple variable initialisation
x = y = 6;                  // 6, 6

// multiple variable definition and initialisation
int x = 6, y = 6;

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
