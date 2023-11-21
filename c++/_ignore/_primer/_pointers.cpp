int a = 5;

// get memory address of a
cout << &a << endl;
// 0x7ffee707c75c

// pointer variable to store address of a
int* ptr = &a;

// reference: output is address
cout << ptr << endl;
// 0x7ffee707c75c

// dereference: output is value at pointer
cout << *ptr << endl;
// 5

// null pointer
int* np = NULL;

cout << np << endl;
// 0x0