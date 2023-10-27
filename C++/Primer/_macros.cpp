cout << __FILE__ << endl;               // test.cpp
cout << __DATE__ << endl;               // Nov  3 2020
cout << __TIME__ << endl;               // 14:10:52
cout << __LINE__ << endl;               // 14
cout << __STDC__ << endl;               // 1

// OUTSIDE SCOPE: define macro
#define error_message(e) cout << "Error: " << e << endl;

// INSIDE SCOPE: use macro
error_message("This is an error.");
// Error: This is an error.

// conditional: if not defined
#ifndef MESSAGE
   #define MESSAGE "This is a message."
#endif

cout << MESSAGE << endl;
// This is a message.

// conditional: if defined
#define DEBUG
#ifdef DEBUG
    cout << "DEBUG is defined." << endl;
#endif
// DEBUG is defined.

// function-like macros
#define square(x) ((x) * (x))
#define MAX(a,b) ((a) > (b) ? (a) : (b))

cout << square(2) << endl;              // 4
cout << MAX(4,5) << endl;               // 5