// OUTSIDE SCOPE: define structure
struct MyStruct {
    int x;
    int y;
};

// or using alias
typedef struct {
	int x;
	int y;
} MyOtherStruct;

// INSIDE SCOPE: declare variables as struct type
struct MyStruct first;
struct MyStruct second;

// or using alias
MyOtherStruct third, fourth;

// assign values to first
first.x = 2;
first.y = 7;

// assign values to second
second.x = -4;
second.y = 12;

// access values
cout << first.x << "," << first.y << endl;              // 2,7
cout << second.x << "," << second.y << endl;            // -4,12