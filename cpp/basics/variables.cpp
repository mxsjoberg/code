// OUTSIDE SCOPE: global or header file
// variable declaration
extern int x;
extern char y[6]; 		// 
extern float z; 		// 4 bytes
extern double a; 		// 8 bytes

// INSIDE SCOPE: local
// variable definition
int x;

// variable definition and initialisation
char y[] = "String";        // String
float z = 1.05;             // 1.05
double a = 12.5;            // 12.5

// variable initialisation
x = 6;

// multiple variable definition
int c, d;

// multiple variable initialisation
c = d = 6;                  // 6, 6

// type modifiers
unsigned int unint; 		// 4 bytes, 0 to 4294967295
signed int siint; 			// 4 bytes, -2147483648 to 2147483647
short int sint; 			// 2 bytes, -32768 to 32767
long int lint; 				// 8 bytes, -2147483648 to 2147483647
long long int llint; 		// 8 bytes, -(2^63) to (2^63)-1
