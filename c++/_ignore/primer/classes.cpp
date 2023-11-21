// 2019-08
#include <iostream>
#include <string>

// declare class
class MyClass;
// define class
class MyClass {
public:
    int number;
    std::string str;
    // member functions
    int get_secret_number() {
        return secret_number;
    }
    // represent class as string
    std::string __repr__() {
        return "MyClass";
    }
    // constructor is called when an instance of class is created
    MyClass() {
        std::cout << "created instance of class: " << __repr__() << std::endl;
    }
private:
    int secret_number = 42;
};
// define subclass inheriting from MyClass
class MySubclass: public MyClass {
public:
    // override
    std::string __repr__() {
        return "MySubclass";
    }
    // constructor: called when instance of class is created
    MySubclass() {
        std::cout << "created instance of subclass: " << __repr__() << std::endl;
    }
};

int main() {
    // create instance of class
    MyClass my_class;
    // created instance of class: MyClass
    
    // update attributes
    my_class.number = 10;
    my_class.str = "this is some text";

    // access attributes
    std::cout << my_class.number << std::endl;
    // 10
    std::cout << my_class.str << std::endl;
    // this is some text

    // access private attribute via public function
    std::cout << my_class.get_secret_number() << std::endl;
    // 42
    
    // create instance of subclass
    MySubclass my_subclass;
    // created instance of class: MyClass
    // created instance of subclass: MySubclass
    
    my_subclass.number = my_class.get_secret_number();
    std::cout << my_subclass.number << std::endl;
    // 42
}