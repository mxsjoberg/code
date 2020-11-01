int a;
for (a = 1; a < 5; a++) {
    // do something
}

// nested
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
        // do something
    }
}

// iterate array
#define ARRAY_SIZE 5

int array[ARRAY_SIZE] = { 1, 2, 3, 4, 5 };
for (int n = 0; n < ARRAY_SIZE; n++) {
    // do something
    cout << n << endl;
}