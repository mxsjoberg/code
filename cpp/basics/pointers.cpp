int a = 5;
int *ip = NULL;

cout << ip << endl;
// 0x0

// store address of a in ip
ip = &a;

cout << &a << endl;             // 0x7ffeebe5a76c
cout << ip << endl;             // 0x7ffeebe5a76c
cout << *ip << endl;            // 5