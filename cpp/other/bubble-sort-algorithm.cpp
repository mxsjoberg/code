int numbers[] = { 14, 33, 27, 35, 10 };

// print unsorted array
for (int i = 0; i < sizeof(numbers) / sizeof(int); i++) {
    cout << numbers[i] << endl;
}
// 14
// 33
// 27
// 35
// 10

// bubble sort
for (int i = 0; i < sizeof(numbers) / sizeof(int); i++) {
    for (int j = 0; j < sizeof(numbers) / sizeof(int); j++) {
        if (numbers[j] > numbers[j + 1]) {
            int temp = numbers[j];
            // swap positions
            numbers[j] = numbers[j + 1];
            numbers[j + 1] = temp;
        }
    }
}

// print sorted array
for (int i = 0; i < sizeof(numbers) / sizeof(int); i++) {
    cout << numbers[i] << endl;
}
// 10
// 14
// 27
// 33
// 35