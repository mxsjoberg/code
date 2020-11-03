// OUTSIDE SCOPE: define namespace
namespace my_functions {
    void first_function() {
        // do something
        cout << "my_functions::first_function" << endl;
    }
    void second_function() {
        // do something
        cout << "my_functions::second_function" << endl;
    }
}

// INSIDE SCOPE: use namespace
my_functions::first_function();
// my_functions::first_function

my_functions::second_function();
// my_functions::second_function

// using
using namespace my_functions;

first_function();
// my_functions::first_function

second_function();
// my_functions::second_function
