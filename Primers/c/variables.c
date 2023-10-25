// OUTSIDE SCOPE: global
// variable declaration
extern int x;
extern char y[];
extern float z;
extern double a; // double size of float

// INSIDE SCOPE: local
// variable definition
int x;

// variable definition and initialisation
char y[] = "String";        // String
float z = 1.05;             // 1.050000
double a = 12.5;            // 12.500000

// variable initialisation
x = 6;

// multiple variable definition
int c, d;

// multiple variable initialisation
c = d = 6;                  // 6, 6