int a = 5;
int *ip = NULL;

printf("%p\n", ip);
// 0x0

// store address of a in ip
ip = &a;

printf("%p\n", &a);             // 0x7ffee73d9608
printf("%p\n", ip);             // 0x7ffee73d9608
printf("%d\n", *ip);            // 5