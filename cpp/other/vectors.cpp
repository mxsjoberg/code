#include <vector>

// vector to store int
vector<int> vec;

// size of vector
cout << vec.size() << endl;
// 0

// push values into vector
for (int i = 1; i <= 5; i++) {
    vec.push_back(i);
}

// new size of vector
cout << vec.size() << endl;
// 5

// access value in vector
cout << vec[0] << endl;
// 1